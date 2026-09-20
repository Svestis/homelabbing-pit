---
entry: II02
title: "Kopia woke up before the clock"
date: 2026-09-20
status: resolved
tags:
  - kopia
  - backups
  - systemd
  - time-sync
  - ubuntu
  - reboot
  - troubleshooting
---

# II02 — Kopia woke up before the clock

![Kopia](https://img.shields.io/badge/Kopia-Backups-blue)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?logo=ubuntu&logoColor=white)
![systemd](https://img.shields.io/badge/systemd-Startup-5C5C5C)
![Status](https://img.shields.io/badge/Status-Resolved-brightgreen)

Back in [0006 — I should probably back this up](../2026/09/0006-i-should-probably-back-this-up.md), I installed Kopia because backups seemed like something that should happen reliably.

Preferably without me thinking about them.

There was only one small problem.

After rebooting the server, Kopia wasn't starting properly.

Excellent.

## 🔴 The backup system didn't come back

A reboot should have been fairly uneventful.

Ubuntu comes back, then
docker, then related services and lastly Kopia.

Except that last part wasn't happening as expected.

The backup system I had installed specifically so I wouldn't have to worry about losing things had developed its own reliability problem.

There is probably a lesson in there somewhere.

## The strange part

Kopia itself wasn't fundamentally broken.

The problem appeared during startup.

That distinction mattered.

```text
Start Kopia later
       │
       └── works

Reboot
   │
   └── Kopia starts
           │
           └── problem
```

Which meant the question stopped being:

> *What's wrong with Kopia?*

and became:

> *What's different immediately after boot?*

## 🕐 Apparently the server needs to know what time it is

The answer turned out to involve something I had given approximately zero thought to until this point:

**system time.**

When Ubuntu booted, the system clock wasn't necessarily ready and synchronized at exactly the moment Kopia tried to start.

Kopia was coming up before the system had finished establishing the correct time.

And apparently my backup system cared about chronology considerably more than I had anticipated.

The startup sequence effectively looked like this:

```text
Ubuntu boots
     │
     ├── Network starts
     │
     ├── System time is still settling...
     │
     └── Kopia starts
             │
             └── too early
```

So Kopia wasn't simply failing after a reboot.

It was starting at the wrong point in the boot process.

## Order matters

This was my introduction to another useful distinction.

A service being configured to start automatically does not necessarily mean:

> *Start when everything I depend on is actually ready.*

It means the operating system has a startup sequence and dependencies need to be expressed properly.

That turned what initially looked like a Kopia problem into a host-level problem.

```text
Kopia
  │
  │ depends on
  ▼
Correct system time
  │
  │ depends on
  ▼
Time synchronization
  │
  │ happens during
  ▼
System startup
```

Another layer underneath the thing I thought I was troubleshooting.

Naturally.

## ## The fix wasn't "restart Kopia"

Restarting Kopia after the machine had finished booting could get things working again.

But that wasn't really a fix.

If every reboot required:

```text
1. Wait for server
2. Notice backups aren't working
3. Restart Kopia
4. Pretend this is automation
```

then I had built a backup system that depended on me remembering to repair it.

Not ideal.

The actual problem was the startup relationship.

Kopia didn't just need Ubuntu to be running.

It needed Docker.

It needed the network.

And, apparently, it needed the server to agree with the rest of the world about what time it was.

So instead of fixing Kopia, I fixed **when Kopia was allowed to start**.

## 🔧 Teaching Kopia to wait

I created a small systemd service:

```ini
[Unit]
Description=Start Kopia after system clock synchronization
Requires=docker.service chrony.service
After=docker.service chrony.service network-online.target
PartOf=docker.service

[Service]
Type=oneshot
ExecStart=/usr/bin/chronyc waitsync 60 0.01
ExecStart=/usr/bin/docker start kopia
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
WantedBy=docker.service
```

The important bit was this:

```ini
ExecStart=/usr/bin/chronyc waitsync 60 0.01
```

I wasn't simply telling systemd:

> *Start Kopia after Chrony.*

That would only tell me that the time synchronization service had started.

It wouldn't necessarily mean the clock had actually synchronized yet.

Instead, `chronyc waitsync` made the startup process actually **wait for synchronization**.

Only then:

```ini
ExecStart=/usr/bin/docker start kopia
```

Kopia was allowed to start.

So the boot sequence became:

```text
Ubuntu boots
     │
     ▼
Network comes online
     │
     ▼
Docker + Chrony
     │
     ▼
Wait for clock synchronization
     │
     ▼
Start Kopia
     │
     ▼
Backups
```

Which is considerably better than:

```text
Ubuntu boots
     │
     ├── Chrony is doing something
     │
     └── KOPIA GO GO GO
```

## Why the clock actually mattered

This wasn't just about making the startup sequence aesthetically pleasing.

My backup monitoring was using timestamps to decide whether the backups were healthy.

It checked the latest successful snapshots and compared them with the current time.

A snapshot could be:

```text
missing
too old
or
apparently from the future
```

That last one is a surprisingly philosophical failure mode for a backup system.

So correct system time wasn't merely something Ubuntu should eventually figure out.

It was part of determining whether the backup system itself was healthy.

## The reboot test

With the new service in place, I rebooted again.

This time the sequence was deliberate:

```text
Docker ready
     │
Chrony running
     │
Clock synchronized
     │
Kopia starts
     │
Backup monitoring works
```

No manual restart.

No waiting for the machine and then fixing the thing that was supposed to be automatic.

Kopia simply waited for the dependency it actually cared about.

Which is considerably closer to what I had meant by:

> *automatic backups.**

## A reboot is apparently a test

This incident also changed how I thought about reboots.

Until now, getting something running usually felt like the finish line.

But:

```text
service works
```

and:

```text
service still works after reboot
```

are two different tests.

A homelab can look perfectly healthy for weeks while quietly depending on some manual action I performed once and completely forgot about.

Restarting the machine exposes those assumptions rather efficiently.

Slightly too efficiently.

## 🧠 What I learned

Startup order matters.

A service can work perfectly once the system is fully running and still fail during boot.

Dependencies aren't only about which software is installed.

Sometimes a service depends on the **state of the system** being ready first.

And apparently even something as fundamental as:

```text
What time is it?
```

has a startup process.

Most importantly, I learned that rebooting the server is a surprisingly effective way of asking:

> *Did I actually configure this properly?*

## 🕳️ How much deeper did the pit get?

I started with:

```text
"Why didn't Kopia start?"
```

I ended with:

```text
Ubuntu boots
     │
     ▼
Network
     │
     ▼
Time synchronization
     │
     ▼
Kopia
     │
     ▼
Backups
```

The backup software wasn't really the problem.

The clock wasn't really the problem either.

The problem was that one of them had arrived before the other.

I had built automatic backups.

Then I had to teach them to wait.

⛏️ **Apparently even the pit has a schedule.**