---
entry: II01
title: "Well, that didn't take long"
date: 2026-09-13
tags:
  - uptime-kuma
  - freebox
  - networking
  - monitoring
  - outage
  - troubleshooting
status: complete
---

# II01 — Well, that didn't take long

![Uptime Kuma](https://img.shields.io/badge/Uptime_Kuma-Monitoring-5CDD8B?logo=uptimekuma&logoColor=white)
![Freebox](https://img.shields.io/badge/Freebox-Network-E2001A)
![Network](https://img.shields.io/badge/Network-Troubleshooting-0078D4)
![Status](https://img.shields.io/badge/Internet-DOWN-critical)

In the previous entry ([0004 — Is everything still alive?](0004-is-everything-still-alive.md)), I installed Uptime Kuma because I wanted to know when something stopped working.

The homelab was being monitored.

The Freebox was being monitored.

The internet connection was being monitored.

Everything was green.

And then my internet connection died.

*Thank you, [Free](https://www.free.fr/).*

Well...

**That didn't take long.**

## 🔴 Something is down

Suddenly, there was no internet.

The obvious first reaction was to blame the router.

But this time I had something I hadn't had before.

Monitoring.

Uptime Kuma was showing me something interesting:

```text
Freebox      ● UP
Internet     ● DOWN
```

The Freebox itself was alive.

My server could reach it.

The local network was functioning.

But traffic wasn't getting out to the internet.

That distinction immediately narrowed the problem down.

For once, installing another container had actually made my life easier.

## 6️⃣ Step 6

Looking at the Freebox gave me another clue.

It was stuck at:

```text
Étape 6
Authentification
```

Or, in Freebox terminology:

**Step 6.**

The box had successfully progressed far enough to establish the connection at the lower levels, but it wasn't completing authentication with Free's network.

Restarting it seemed like the obvious first step.

So I restarted it.

And waited.

```text
Step 1
   ↓
Step 2
   ↓
Step 3
   ↓
Step 4
   ↓
Step 5
   ↓
Step 6
   ↓
Step 6
   ↓
Step 6
   ↓
...
```

Excellent.

## 🕵️ Is it me or is it Free?

At this point the question changed.

Was something wrong with **my setup**, or was there a wider problem with Free?

That is a surprisingly important distinction when troubleshooting a network.

I had recently been changing things in the homelab.

There were now plenty of things I could potentially have broken myself.

But the evidence didn't really point toward the homelab.

```text
Local network      ✓
Freebox reachable  ✓
Homelab            ✓
Internet           ✗
Freebox Step 6     ✗
```

The problem was upstream.

For once, the pit appeared to be innocent.

## 📡 Monitoring layers suddenly made sense

When I added the Freebox and Internet as separate monitors, it had felt slightly excessive.

Why monitor both?

Surely if the internet goes down, the Freebox is down.

Nope.

This outage demonstrated exactly why they were useful as separate checks.

If I had monitored only an external internet endpoint, I would have seen:

```text
Internet ● DOWN
```

Useful, but not particularly informative.

Instead I had:

```text
Home Assistant   ● UP
Portainer        ● UP
Uptime Kuma      ● UP

Freebox          ● UP
Internet         ● DOWN
```

That told a much better story.

My tiny monitoring setup had accidentally become a troubleshooting tool.

## ⏱️ And now we wait

There wasn't much more for me to fix locally.

So I did something that is remarkably difficult when you have just discovered homelabbing:

**Nothing.**

I waited.

And kept checking.

Because apparently installing monitoring doesn't stop you from manually checking the monitoring every few minutes.

## 🟢 And we're back

Eventually, the internet connection returned.

And Uptime Kuma reflected exactly what had happened:

```text
Freebox      ● UP
Internet     ● UP
```

Back to green.

No container needed rebuilding.

No Caddy configuration needed changing.

No Docker network needed investigating.

Nothing in the homelab had actually broken.

Which was almost disappointing.

Almost.

## 🤔 What I thought at the time

The timing was funny.

I had installed monitoring because theoretically, one day, something might go wrong.

The network apparently took that as a challenge.

But the outage also immediately justified one of the decisions I'd just made.

Monitoring the router and internet separately wasn't redundant.

They represented different layers of the system.

And knowing **which layer is still working** is often more useful than simply knowing that something isn't.

## 🧠 What I learned

"Internet down" doesn't necessarily mean "router down."

A device being reachable on the local network says nothing about whether its upstream connection is healthy.

Monitoring different layers makes troubleshooting much faster:

```text
Application
     ↓
Container
     ↓
Server
     ↓
Local network
     ↓
Router
     ↓
ISP
     ↓
Internet
```

If you can determine where the chain stops working, you have already eliminated everything below it.

I also learned another important lesson:

**Monitoring becomes considerably more interesting when something actually breaks.**

## 🕳️ How much deeper did the pit get?

I started with:

```text
"Why is my internet down?"
```

I ended with:

```text
                 Uptime Kuma
                      │
          ┌───────────┴───────────┐
          │                       │
       LOCAL                    UPSTREAM
          │                       │
   Homelab      ● UP         Freebox   ● UP
   Services     ● UP         Internet  ● DOWN
          │                       │
          └────── not here ───────┘
                                  │
                              problem
                                  ↑
```

For once, I hadn't created the problem.

Better still, the homelab I'd been building helped me understand it.

Eventually:

```text
Freebox      ● UP
Internet     ● UP
```

Everything returned to green.

I looked at Uptime Kuma.

The monitoring worked.

The incident was over.

And having watched all those little status indicators for hours, I naturally started thinking:

**These dashboards could look better...**

⛏️ *Apparently even an internet outage can lead to another homelab project.*