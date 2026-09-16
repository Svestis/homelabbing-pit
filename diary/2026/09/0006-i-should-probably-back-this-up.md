---
entry: 0006
title: "I should probably back this up"
date: 2026-09-15
status: complete
tags:
  - kopia
  - backups
  - docker
  - disaster-recovery
  - migration
---

# 0006 — I should probably back this up

![Kopia](https://img.shields.io/badge/Kopia-Backups-blue)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?logo=ubuntu&logoColor=white)

By the end of [0005 — I wanted a dashboard](0005-i-wanted-a-dashboard.md), the homelab was starting to look suspiciously organised.

I had services.

I had monitoring.

I had metrics.

I had a dashboard.

I could open one page and admire the increasingly elaborate collection of things I had convinced myself were necessary.

Then a considerably less entertaining thought occurred to me:

> *What happens if I lose all of this?*

## Running something is not the same as keeping it

Until this point, most of my attention had been on getting things running.

Create a container.

Configure it.

Fix whatever I had misunderstood.

Make it accessible.

Add HTTPS.

Monitor it.

Put it on the dashboard.

Repeat.

But every service was also accumulating something much more important than its container:

**state.**

Home Assistant had configuration.

Uptime Kuma had monitors.

Portainer had its data.

Homepage had configuration.

Caddy had certificates and state.

The containers themselves were replaceable.

The data wasn't.

That distinction suddenly mattered quite a lot.

## I had already started backing things up

Home Assistant had actually given me an early warning.

I had already created a backup of its data and discovered that even something as simple as making a tar archive could turn into a Linux permissions lesson when some of the files were owned by root.

So technically, I had a backup.

One backup.

Created manually.

For one service.

This did not feel like a particularly convincing disaster recovery strategy.

## Enter Kopia

I started looking for something that could handle backups properly rather than relying on increasingly optimistic uses of `tar`.

That led me to **Kopia**.

The attraction wasn't just:

> *make copies of files.*

I wanted something I could build an actual backup strategy around.

Snapshots.

Retention.

Verification.

A repository that wasn't tied to one individual Docker container.

Something that could eventually survive the homelab changing underneath it.

Because another idea had also started appearing more frequently:

> *This VM probably isn't going to be the final home of all this.*

## The directory structure suddenly mattered more

By now I had already been organising the homelab around `/opt/homelab`.

That decision became considerably more useful once backups entered the picture.

```text
/opt/homelab/
├── compose/
├── data/
└── backups/
```

The separation was becoming clearer.

`compose/` described how things should run.

`data/` contained the persistent state that actually mattered.

`backups/` gave me somewhere to deal with protecting it.

For the first time, the directory structure wasn't just about keeping things tidy.

It was starting to become part of the recovery plan.

## What am I actually trying to recover?

This turned out to be a much better question than:

> *What folders should I back up?*

If the Ubuntu VM disappeared tomorrow, I didn't necessarily care about recovering the VM exactly as it was.

Ubuntu could be installed again.

Docker could be installed again.

Containers could be pulled again.

What I really cared about was whether I could reconstruct the homelab without reconstructing **months of configuration by hand**.

That meant protecting the things that were difficult or annoying to recreate.

Configuration.

Application data.

Databases.

Certificates and state where appropriate.

And, increasingly, the structure I was using to manage everything.

## Backup and migration started becoming the same conversation

This also changed how I thought about eventually moving away from the VM.

Until now, migration sounded like:

> *One day I'll buy a dedicated machine and move everything.*

Which is not much of a plan.

Backups made the question more concrete.

If the important state was stored predictably, backed up properly, and the Docker configuration was preserved, then moving to another machine didn't necessarily mean starting again.

The future server could be different.

The operating environment could change.

The storage could change.

But the services didn't have to forget who they were.

That was reassuring.

It was also a dangerous realization, because it made buying more hardware sound increasingly reasonable.

## A backup is only useful if it can come back

There was another uncomfortable realization.

Seeing:

```text
Backup completed successfully
```

is nice.

It is not the same thing as knowing that the backup can actually restore anything.

So the goal couldn't simply be to make Kopia produce successful snapshots.

Eventually I would need to understand:

- what was being backed up,
- where the repository lived,
- what retention I wanted,
- how to verify snapshots,
- how restoration worked,
- and how portable the whole setup would be when the homelab eventually moved somewhere else.

In other words, installing the backup software was the easy part.

I had apparently discovered another subsystem.

## The pit now needed an escape ladder

There was something slightly ironic about all this.

The more time I spent making the homelab useful, the more important it became to protect the time I had already spent making the homelab useful.

Backups weren't another shiny service to put on the dashboard.

They were insurance against having to repeat the entire diary.

And given how many rabbit holes it had already taken to get here, that seemed worthwhile.

## 🕳️ How much deeper did the pit get?

**Before:**

```text
Ubuntu Server
└── Docker
    ├── Portainer
    ├── Home Assistant
    ├── Caddy
    ├── Uptime Kuma
    ├── Homepage
    └── Glances
```

**After:**

```text
Ubuntu Server
├── Docker
│   ├── Portainer
│   ├── Home Assistant
│   ├── Caddy
│   ├── Uptime Kuma
│   ├── Homepage
│   ├── Glances
│   └── Kopia
│
└── Backups
    └── Kopia repository
```

I had spent several days figuring out how to put more things into the pit.

It was probably time to figure out how to get them back out.

⛏️ **The pit now had an escape ladder.**