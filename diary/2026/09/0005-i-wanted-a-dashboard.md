---
entry: 0005
title: "I wanted a dashboard"
date: 2026-09-14
status: complete
tags:
  - homepage
  - glances
  - monitoring
  - dashboard
  - docker
  - metrics
---

# 0005 — I wanted a dashboard

![Homepage](https://img.shields.io/badge/Homepage-Dashboard-blue?logo=homepage&logoColor=white)
![Glances](https://img.shields.io/badge/Glances-Monitoring-green)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?logo=ubuntu&logoColor=white)

At the end of [0004 — Is everything still alive?](0004-is-everything-still-alive.md), I finally had monitoring.

Uptime Kuma could tell me whether Home Assistant was reachable, whether Portainer was alive, whether the Freebox was responding, whether the Internet existed, and whether my website was still out there somewhere.

Lots of reassuring green dots.

Naturally, this wasn't enough.

## Green is good, but what is the server actually doing?

Knowing that a service is *up* is useful.

It doesn't tell me how much CPU the server is using.

Or how much memory is left.

Or how full the disk is getting.

Or what the load looks like.

Or how long the server has been running.

Or how many Docker containers I've somehow accumulated.

I had reached the inevitable next stage of monitoring:

> *Yes, everything is alive. Now give me numbers.*

So I started looking at **Glances**.

## Enter Glances

Glances gave me the system-level information that Uptime Kuma wasn't designed to provide.


The sort of information that immediately makes a server feel considerably more serious than it did five minutes earlier.

There was only one problem.

I didn't particularly want another page that I had to remember to open.

I already had Home Assistant.

Portainer.

Uptime Kuma.

And now Glances.

The homelab was beginning to develop a small collection of browser tabs.

What I really wanted was somewhere to put everything.

## Apparently I need a homepage for my Homepage

That led me to **Homepage**.

The idea was simple: one dashboard containing links to the things running in the homelab.

I split things into groups that made sense to me.

The internal homelab services could live together.

The network and connectivity checks could live together.

Everything would finally have one obvious place to start.

At first, that meant cards for things like:

- Portainer
- Home Assistant
- Uptime Kuma
- the Ubuntu server
- the Freebox
- Internet connectivity
- my external website

It was already much nicer than remembering URLs.

Then I made the mistake of wondering whether the Ubuntu card could show the Glances data directly.

## One server card became a small project

I didn't just want a link labelled **Ubuntu Server**.

I wanted the card to actually tell me something.

And, because apparently plain numbers were no longer sufficient, I wanted CPU, memory, and disk usage to have circular gauges with live values.

At some point I had gone from:

> *I should probably monitor whether my services are alive.*

to:

> *The disk gauge could look better.*

This felt like progress.

## Two different kinds of monitoring

This was also where the distinction between **availability monitoring** and **system monitoring** became much clearer.

Uptime Kuma answered:

> **Can I reach it?**

Glances answered:

> **What is the machine doing?**

Homepage then gave me somewhere to bring those answers together.

They weren't competing tools after all.

They were different views of the same increasingly unnecessary amount of infrastructure.

## The homelab finally had a front door

By this point, opening the dashboard gave me a quick view of the environment instead of making me visit every service individually.

That changed how the whole thing felt.

The homelab was no longer just a collection of containers I happened to know were running.

It had a front door.

A slightly over-engineered front door, admittedly.

But a front door.

And for a brief moment, I could open one page, look at the services, look at the server metrics, see a reassuring collection of green indicators, and think:

> *This is actually becoming quite organised.*

Which, historically, is usually when I decide to add something else.

## 🕳️ How much deeper did the pit get?

**Before:**

```text
Ubuntu Server
└── Docker
    ├── Portainer
    ├── Home Assistant
    ├── Caddy
    └── Uptime Kuma
```

**After:**

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

I started because I wanted to know whether everything was still alive.

I ended with a dashboard showing me how alive it was.

⛏️ **The pit now had a control panel.**