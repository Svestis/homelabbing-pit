---
entry: 0011
title: "The VM was never supposed to become a server"
date: 2026-09-22
status: complete
tags:
  - ubuntu
  - utm
  - server
  - hardware
  - architecture
  - homelab
---

# 0011 — The VM was never supposed to become a server

![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?logo=ubuntu&logoColor=white)
![UTM](https://img.shields.io/badge/UTM-Virtual_Machine-000000)
![Status](https://img.shields.io/badge/Status-Reconsidering_the_hardware-yellow)

By [0010 — I should probably manage the host too](0010-i-should-probably-manage-the-host-too.md), I had finally given the Ubuntu host its own management interface.

Which made one detail increasingly difficult to ignore.

The host wasn't actually a server.

It was still this:

```text
Mac
└── UTM
    └── Ubuntu Server
```

Four CPU cores with 8 GB of RAM and 50 GB of storage.

A VM I created to learn things.

Apparently it had other plans.

## This was supposed to be temporary

Back in [0001](0001-it-started-with-an-ubuntu-vm.md), the idea was fairly innocent.

What actually happened was:

```text
Ubuntu Server
│
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
├── Cockpit
└── SSH
```

The experiment had acquired responsibilities.

Quite a few of them.

At some point I had stopped asking:

> *What can I learn with this VM?*

and started asking:

> *Is the server up?*

That seemed significant.

## The VM was doing surprisingly well

The annoying part was that nothing was particularly wrong.

The VM worked.

Docker was happy.

The services were happy.

I was happy.

Mostly.

Then [Immich arrived](0007-my-photos-live-here-now.md), and the 50 GB disk started looking considerably less generous.

Backups became important.

Home Assistant was becoming part of the house.

Monitoring was watching everything.

And Cockpit had just given me a proper interface for managing the host underneath it all.

I was treating the VM like permanent infrastructure.

It was probably time to admit that it wasn't.

## The Mac would also like its computer back

There was another fairly obvious problem.

The machine underneath all of this was still my Mac.

```text
MacBook
│
├── My computer
│
└── Apparently also a datacenter
```

The homelab existed because the Mac existed.

If the Mac was off, moved, restarted or needed for something else, the infrastructure came with it.

That had been perfectly reasonable when the whole thing was an experiment.

It felt less reasonable now that the experiment had backups, monitoring, home automation and a photo library.

The pit was becoming permanent.

The machine underneath it wasn't.

## Fine. I need a real machine.

That conclusion was easy.

The next question was not.

What exactly should replace it?

My first thought was a small dedicated computer.

Then I started thinking about storage.

Then the NAS question from [0009](0009-do-i-need-a-nas.md) came back.

Then virtualisation entered the conversation.

Then expandability.

Then power consumption.

Then networking.

Then backups.

The simple question:

> *What computer should I buy?*

had become:

> *What should the homelab actually run on?*

Much better.

## One machine or several?

There were suddenly several ways this could go.

```text
The next homelab
│
├── Mini PC
│
├── Used corporate desktop
│
├── Dedicated server + NAS
│
└── One machine doing both
```

A mini PC would be small and efficient.

A used corporate machine could offer more expansion for not much money.

A separate NAS would keep storage separate from compute.

One larger machine could potentially do both.

And somewhere in there was also the question of whether the next machine should run Ubuntu directly or whether this was the point where something like Proxmox started making sense.

I had successfully turned buying one computer into an architecture exercise.

## At least now I knew what I was looking for

Not the exact machine.

That part was still very much unresolved.

But the VM had taught me something more useful than a shopping list.

I now knew what the homelab was actually doing.

The next machine needed enough compute and memory for the services already here, room for more, proper storage options, sensible power consumption, reliable networking and a backup strategy that didn't depend on optimism.

Most importantly, it needed to be a machine whose actual job was:

```text
run the homelab
```

rather than:

```text
be my computer
└── also run the homelab somehow
```
## So I started looking

There was no reason to rush - nothing needed replacing today.

Which meant I could look around, compare options and wait for something that actually made sense.

Naturally, this resulted in me looking at a lot of computers.

Mini PCs.

Old corporate desktops.

Newer machines.

French listings.

Swiss listings.

Machines I needed.

Machines I probably didn't need.

Machines that became interesting entirely because somebody had reduced the price.

The architecture discussion was apparently becoming a marketplace problem.

That sounded like something for another entry.

## 🕳️ How much deeper did the pit get?

**Before:**

```text
Mac
└── UTM
    └── Ubuntu Server
        └── the homelab
```

**After:**

```text
Mac
└── UTM
    └── Ubuntu Server
        └── the homelab
                │
                └── needs somewhere permanent to live
```

I started with a VM because I didn't have a server.

Eleven entries later, I apparently need a server because of the VM.

Progress.

⛏️ **The pit was looking for a permanent address.**