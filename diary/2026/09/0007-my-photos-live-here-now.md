---
entry: 0007
title: "My photos live here now"
date: 2026-09-16
status: complete
tags:
  - immich
  - photos
  - docker
  - self-hosting
  - storage
  - backups
---

# 0007 — My photos live here now

![Immich](https://img.shields.io/badge/Immich-Photos-4250AF?logo=immich&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker&logoColor=white)
![Kopia](https://img.shields.io/badge/Kopia-Backups-blue)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?logo=ubuntu&logoColor=white)

At the end of [0006 — I should probably back this up](0006-i-should-probably-back-this-up.md), I had finally started thinking about protecting the homelab instead of just adding things to it.

This was responsible.

Sensible, even.

Naturally, the next thing I did was add something that would eventually require considerably more storage.

## So far, the homelab mostly ran the homelab

Looking at what I had built, most of the services had one thing in common.

They existed largely to manage, monitor, secure, or display other parts of the homelab.


But I wanted to try something different.

Something where the homelab wasn't just infrastructure.

Something I would actually use.

That led me to **Immich**.

## Apparently my photos live here now

Immich is a self-hosted photo and video management platform.

Which sounded simple enough.

Run some containers.

Point it at some storage.

Upload some photos.

Done.

By this point I really should have known better.

Still, the idea was compelling.

Instead of treating the server as somewhere that merely ran infrastructure, I could use it to host an actual personal application.

A photo library seemed like a good place to start.

So Immich joined the pit.

## This one was different

Installing another monitoring tool is fairly low stakes.

If I break Glances, I temporarily can't see some graphs.

If I break Homepage, I temporarily lose my convenient collection of links.

Photos are different.

The moment I started thinking about putting an actual photo library into the homelab, several things suddenly became much more important.

Storage.

Persistence.

Backups.

Recovery.

And the uncomfortable realization that my little Ubuntu VM still had a **50 GB virtual disk**.

That had seemed perfectly reasonable when I created it.

It seemed rather less ambitious now.

## Containers are still the easy part

Immich also reinforced something I had started learning with the other services.

The container isn't really the valuable part.

Containers can be recreated.

Suddenly the distinction I had been thinking about in [0006](0006-i-should-probably-back-this-up.md) wasn't theoretical anymore.

If this was going to contain photos I cared about, then:

> *I have a backup.*

needed to eventually mean considerably more than:

> *Kopia says the snapshot completed.*

Restoration mattered.

Storage location mattered.

And understanding exactly what needed to survive mattered.

## 50 GB was starting to look adorable

When I created the Ubuntu VM, I gave it 50 GB of storage.

For Ubuntu, Docker, and a few services, that was plenty.

For a photo library?

Not so much.

This was the first service that made storage capacity feel like an architectural problem rather than a number I had selected while creating a virtual machine.

If the homelab continued in this direction, I would eventually need to answer questions like:

- Where should bulk data actually live?
- Should storage be separate from compute?
- Do I need a NAS?
- Should the future dedicated server also provide storage?
- What exactly should Kopia protect?
- How much of this VM should I really be treating as permanent?

These were all excellent questions.

I answered none of them immediately.

I installed Immich instead.

## Self-hosting started to mean something different

There was also a subtle shift happening.

Until now, the project had mostly been:

> *Can I build this?*

Immich introduced another question:

> *Would I actually trust myself to run this?*

That's a much higher bar.

A dashboard being unavailable for an afternoon is annoying.

A personal photo library disappearing because I misunderstood Docker volumes would be something else entirely.

Running useful services meant the homelab couldn't just be interesting.

It had to become dependable.

Which felt suspiciously like responsibility.

## And now the backup system has a job

The timing was almost too perfect.

I had just added Kopia because I thought I should have a proper backup strategy.

Then I immediately installed something that made having a proper backup strategy considerably more important.

So the relationship between the services was becoming clearer.

Immich wasn't just another container.

It was exactly the kind of application that justified the work I had started doing around persistent data and backups.

The pit was beginning to develop dependencies.

Not Docker dependencies.

**Consequences.**

## The little VM was becoming a real server

There was another problem I was increasingly unable to ignore.

This was still a virtual machine running on my Mac.

The same VM that had started as an experiment.

The same one I had given a few CPU cores, some memory, and a 50 GB disk because:

> *That should be enough.*

It was now running home automation, reverse proxying, monitoring, dashboards, backups, and a photo platform.

At some point the phrase:

> *I'll eventually move this to a dedicated machine.*

had stopped sounding like a hypothetical future improvement.

It was starting to sound like capacity planning.

That could wait.

Probably.

## 🕳️ How much deeper did the pit get?

**Before:**

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
│   ├── Kopia
│   └── Immich
│
├── Backups
│   └── Kopia repository
│
└── Data
    └── Photos are apparently my responsibility now
```

I had started the homelab by asking what I could run.

Immich made me start asking whether I could keep it.

Those are very different questions.

⛏️ **The pit now contained things I actually cared about.**