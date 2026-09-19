---
entry: 0010
title: "I should probably manage the host too"
date: 2026-09-19
status: complete
tags:
  - cockpit
  - ubuntu
  - server-management
  - monitoring
  - docker
  - infrastructure
---

# 0010 — I should probably manage the host too

![Cockpit](https://img.shields.io/badge/Cockpit-Server_Management-0066CC)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?logo=ubuntu&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker&logoColor=white)
![SSH](https://img.shields.io/badge/SSH-OpenSSH-000000?logo=openssh&logoColor=white)

By [0009 — Do I need a NAS?](0009-do-i-need-a-nas.md), I was thinking about what the next server might look like.

Which made me look slightly more critically at how I was managing the server I already had.

Docker had Portainer, monitoring had Uptime Kuma, metrics had Glances, everything had Homepage.

Ubuntu itself had...

```bash
ssh
```

## SSH had been there from the beginning

SSH was one of the first things I configured in [0001](0001-it-started-with-an-ubuntu-vm.md).

And it had worked perfectly well.

Need to update Ubuntu?

SSH.

Check a service?

SSH.

Look at disk usage?

SSH.

Restart something?

SSH.

Investigate why something had decided not to work?

SSH.

There was nothing particularly wrong with this.

But the rest of the homelab had gradually acquired interfaces, monitoring and visibility while the machine underneath all of it was still mostly being managed through a terminal.

Apparently the host wanted a UI too.

## Enter Cockpit

That led me to **Cockpit**.

Unlike most of the things I had added so far, Cockpit wasn't another application for Docker to run.

It was for the Ubuntu host itself.

That distinction mattered.

```text
Ubuntu Server
│
├── Cockpit ───────► host
│
└── Docker
    ├── Portainer
    ├── Home Assistant
    ├── Caddy
    ├── Uptime Kuma
    ├── Homepage
    ├── Glances
    ├── Kopia
    └── Immich
```

Portainer could tell me what Docker was doing.

Cockpit could tell me what the machine running Docker was doing.

Another layer had acquired an interface.

## Didn't I already have Glances?

Yes.

Naturally, I had managed to install something with some overlap.

Glances already showed me CPU, memory, load, disks and network activity.

Homepage was already displaying some of those metrics.

But Cockpit wasn't really replacing either of them.

The distinction was becoming something like:

```text
Uptime Kuma
    └── Is it reachable?

Glances
    └── What is the machine doing?

Portainer
    └── What is Docker doing?

Cockpit
    └── Let me manage the machine.
```

That last one was the part I had been missing.

## The host is infrastructure too

It was easy to forget about Ubuntu because most of my attention went to the services running on top of it.

The stack was really closer to:

```text
Applications
     │
     ▼
Containers
     │
     ▼
Docker
     │
     ▼
Ubuntu
     │
     ▼
The tiny VM I keep asking to do more things
```

I had spent quite a lot of time managing the top half.

Cockpit made the bottom half considerably more visible.

## This wasn't about avoiding the terminal

I didn't suddenly want to replace SSH.

The terminal was still useful.

In plenty of cases it was still the fastest way to do something.

Cockpit just gave me another view of the same machine.

For quick checks and routine management, having a web interface was convenient.

For everything else:

```bash
ssh
```

wasn't going anywhere.

Which felt like a much better arrangement than pretending one tool needed to replace the other.

## The management layer was getting crowded

There was now a slightly ridiculous number of ways to look at one small Ubuntu VM.

```text
Homepage
   │
   └── Where is everything?

Uptime Kuma
   │
   └── Is everything up?

Glances
   │
   └── What are the metrics?

Portainer
   │
   └── What are the containers doing?

Cockpit
   │
   └── What is Ubuntu doing?

SSH
   │
   └── Fine. I'll do it myself.
```

This looked like duplication.

Some of it probably was.

But each tool was answering a slightly different question.

And for now, that was useful.

## I had finally reached the bottom of the stack

Or at least what currently passed for the bottom.

The homelab had started with Ubuntu.

Then I immediately built upward.

It had taken ten diary entries before I came back down and thought:

> *Maybe I should manage Ubuntu properly too.*

Better late than never.

## 🕳️ How much deeper did the pit get?

**Before:**

```text
Ubuntu Server
     │
     └── "I'll just SSH into it."
```

**After:**

```text
Ubuntu Server
├── Cockpit
├── SSH
│
└── Docker
    ├── Portainer
    ├── Home Assistant
    ├── Caddy
    ├── Uptime Kuma
    ├── Homepage
    ├── Glances
    ├── Kopia
    └── Immich
```

I had started looking for a better way to manage the host.

I ended up giving the management layer another management interface.

Completely different.

⛏️ **The pit now had a cockpit - but is it ready for takeoff?**