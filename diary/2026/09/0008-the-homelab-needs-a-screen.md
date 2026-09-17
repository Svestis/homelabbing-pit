---
entry: 0008
title: "The homelab needs a screen"
date: 2026-09-17
status: paused
tags:
  - home-display
  - raspberry-pi
  - home-assistant
  - dashboard
  - guest-wifi
  - qr-code
---

# 0008 — The homelab needs a screen

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Display-A22846?logo=raspberrypi&logoColor=white)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Smart%20Home-18BCF2?logo=homeassistant&logoColor=white)
![Status](https://img.shields.io/badge/Status-Paused-yellow)

By the end of [0007 — My photos live here now](0007-my-photos-live-here-now.md), the homelab had become considerably more useful.

It automated, monitored,
and backed things up.

It had a dashboard - it even had my photos.

There was just one minor inconvenience.

Almost everything I had built required me to take out a device and open a browser.

Apparently this was unacceptable.

## It started with a QR code

I already had a QR code for the guest Wi-Fi.

Scan it and you're connected.

Simple.

The obvious solution would have been to print it.

Naturally, I started wondering whether I could put it on a screen instead.

A small display somewhere in the house could show the guest Wi-Fi QR code permanently.

Just:

> *Scan this.*

That was the entire requirement.

For approximately five minutes.

## What if the screen did more?

If I was going to have a screen connected to the homelab anyway, displaying one static QR code seemed like a waste.

It could show the time, maybe the weather,
maybe some Home Assistant information, maybe whether the Internet was up, maybe useful household information, maybe controls, maybe status information from the homelab, maybe...


The guest Wi-Fi display had lasted about as long as most of my original project scopes.

I was no longer thinking about a QR-code display.

I was thinking about a **Home Display**.

## The Raspberry Pi returns

A Raspberry Pi made sense for this.

Perfect.

The idea started taking shape around a small display with the Pi contained behind it, so from the outside there would effectively be:

```text
┌─────────────────────────────┐
│                             │
│        Home Display         │
│                             │
│       ┌───────────┐         │
│       │           │         │
│       │  Wi-Fi QR │         │
│       │           │         │
│       └───────────┘         │
│                             │
│    Home / network status    │
│                             │
└─────────────────────────────┘
              │
           USB power
```
At least aesthetically, I was trying to show restraint.

## Home Assistant already knew things

The obvious source for much of the display was Home Assistant.

So rather than creating an entirely independent system, the display could eventually become another way of presenting information the existing infrastructure already knew.

That was appealing.

The homelab wouldn't just be something I administered anymore.

It would start becoming something physically present in the house.

## Then I made it its own service

Because apparently having a screen wasn't enough, the project started getting its own place in the homelab too.

```text
/opt/homelab/compose/home-display/
```

There is a particular moment in every project where an idea stops being:

> *Wouldn't this be cool?*

and becomes:

> *Why does this have a directory now?*

We had reached that moment.

## The interesting part wasn't actually the screen

The more I thought about it, the more useful the project became as an architectural exercise.

The display itself could be relatively disposable.

If a Raspberry Pi died, I didn't want the information or logic to disappear with it.

Ideally, the homelab would provide what the display needed, while the Pi would mostly be responsible for presenting it.

Something closer to:

```text
Home Assistant ─┐
                │
Homelab ────────┼──► Home Display ──► Raspberry Pi + screen
                │
Network status ─┘
```

That separation would make the physical display just another client of the homelab rather than an isolated little project stuck to a wall.

Which was a surprisingly serious architecture discussion for something that began as:

> *Where should I put the Wi-Fi QR code?*

## And then I paused it

Unlike most of the projects so far, this one didn't immediately reach:

```text
status: complete
```

The idea was there, the structure had started, the physical form factor was being considered.

But there were still hardware decisions and implementation details to settle.

And other parts of the homelab were demanding attention.

So the Home Display went into a state I suspect the pit will become very familiar with:

**paused.**

Just sitting there waiting for me to decide that *today is apparently the day we're doing this again.*

## Paused is also progress

I'm actually keeping this one in the diary precisely because it isn't finished.

If this repository only recorded things after they worked, it would give a fairly misleading impression of how the homelab developed.

Projects start.

Priorities change.

Problems appear.

Hardware is awaited.

Ideas evolve.

Some things sit unfinished while something completely unrelated suddenly becomes more interesting.

That's part of the story too.

And eventually, when the Home Display comes back, there will be a record of where the idea actually started.

With a guest Wi-Fi QR code.

That I could have printed.

## 🕳️ How much deeper did the pit get?

**Before:**

```text
The homelab
    │
    └── mostly lives in browsers
```

**After:**

```text
The homelab
    │
    ├── Services
    ├── Monitoring
    ├── Backups
    ├── Photos
    │
    └── Home Display
            │
            ├── Guest Wi-Fi QR
            ├── Home Assistant
            ├── Network status
            └── Raspberry Pi + screen
                    │
                    └── eventually...
```

I wanted somewhere to display the guest Wi-Fi QR code.

Printing remains technically available.

⛏️ **The pit is attempting to acquire a screen.**

*For now, it remains paused.*