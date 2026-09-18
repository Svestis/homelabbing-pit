---
entry: 0009
title: "Do I need a NAS?"
date: 2026-09-18
status: complete
tags:
  - nas
  - storage
  - immich
  - kopia
  - backups
  - architecture
---

# 0009 — Do I need a NAS?

![NAS](https://img.shields.io/badge/NAS-Storage-4A5568)
![Immich](https://img.shields.io/badge/Immich-Photos-4250AF?logo=immich&logoColor=white)
![Kopia](https://img.shields.io/badge/Kopia-Backups-blue)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?logo=ubuntu&logoColor=white)

[0007 — My photos live here now](0007-my-photos-live-here-now.md) had left me with a question I had very deliberately avoided answering:

**Where is all this data eventually going to live?**

My Ubuntu VM still had a 50 GB virtual disk.

That was perfectly fine when the homelab was mostly configuration files, containers and dashboards.

Then Immich arrived.

Suddenly 50 GB looked less like storage and more like a countdown.

## I probably need a NAS

That seemed like the obvious answer.

A NAS would give me proper storage outside the VM.

Immich could keep its photos there,
Kopia could have somewhere sensible to put backups, future services could use it too.

Problem solved.

So naturally, I started looking at NAS options.

And almost immediately managed to turn:

> *I need more storage.*

into:

> *What should the architecture of the entire homelab be?*

## Storage and backups are not the same thing

Kopia had already made me think about what I actually needed to preserve.

Immich made that considerably less theoretical.

But adding more disks doesn't automatically make anything safe.

```text
More storage
     ≠
A backup
```



And if the NAS itself became the only place containing the photos, then I had mostly succeeded in moving the problem into a different box.

Excellent.

## Then there was the future server

There was another awkward detail.

The Ubuntu VM was never really supposed to become permanent.

It started as an experiment inside UTM on my Mac.

Now it was running:

```text
Ubuntu Server
├── Home Assistant
├── Portainer
├── Caddy
├── Uptime Kuma
├── Homepage
├── Glances
├── Kopia
└── Immich
```

And I was considering buying another machine just to give that temporary machine somewhere to put its data.

Which raised a fairly obvious question:

**If I'm eventually buying dedicated hardware anyway, should storage be part of that machine?**

## One box or two?

The architecture in my head had now split into two possibilities.

Something like:

```text
Dedicated Server
      │
      ├── Services
      └── Compute

NAS
 │
 ├── Photos
 ├── Data
 └── Backups
```

Or:

```text
Dedicated Server
      │
      ├── Services
      ├── Compute
      ├── Storage
      └── Backups
```

The first gives storage its own dedicated machine.

The second is considerably simpler.

At least until that one machine dies.

Then simplicity becomes a slightly different experience.

## Apparently I need an architecture before I need a NAS

This was the point where buying something immediately stopped making sense.

I didn't actually know enough yet, I didn't know what the eventual dedicated server would be, I didn't know how much storage I really needed, I didn't know whether compute and storage should live together, I didn't know what the final backup destination should look like, and I definitely didn't know whether buying a NAS now would solve the eventual problem or simply become another piece of hardware I would later design around.

So, unusually, I didn't buy anything.

I kept thinking.

## The 50 GB VM remains

Which means the current architecture is still wonderfully inappropriate:

```text
Mac
 │
 └── UTM
      │
      └── Ubuntu Server
           │
           └── 50 GB
                │
                └── increasingly ambitious plans
```

But the NAS question did clarify something.

The next big change probably isn't another Docker container.

It's the machine underneath them.

The VM has been an excellent place to build the homelab.

I'm becoming considerably less convinced that it should be where the homelab eventually lives.

## 🕳️ How much deeper did the pit get?

**Before:**

```text
"I installed Immich."
```

**After:**

```text
"I installed Immich."
        │
        ▼
"I need storage."
        │
        ▼
"Maybe a NAS?"
        │
        ▼
"Wait, what is the future server?"
        │
        ▼
"Should compute and storage be separate?"
        │
        ▼
"I should probably design this first."
```

For once, the pit produced a new piece of infrastructure that consumes absolutely no electricity:

**a question mark.**

⛏️ *The NAS remains theoretical.*