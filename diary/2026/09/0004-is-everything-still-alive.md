---
entry: 0004
title: "Is everything still alive?"
date: 2026-09-13
tags:
  - uptime-kuma
  - monitoring
  - docker
  - networking
  - freebox
  - uptime
status: complete
---

# 0004 — Is everything still alive?

![Uptime Kuma](https://img.shields.io/badge/Uptime_Kuma-Monitoring-5CDD8B?logo=uptimekuma&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?logo=ubuntu&logoColor=white)
![Monitoring](https://img.shields.io/badge/Monitoring-Uptime-2E8B57)
![Network](https://img.shields.io/badge/Network-Connectivity-0078D4)

After [0003 — I only wanted the warning to go away](0003-i-only-wanted-the-warning-to-go-away.md) things were starting to accumulate.

And I had created enough moving parts to start wondering:

**Is everything actually still running?**

## 👀 Looking at Portainer isn't monitoring

Until now, checking whether something was working was fairly straightforward.

Open it.

If the page loaded, great.

If it didn't, start investigating.

Portainer could also tell me whether a container was running.

But there is an important difference between:

```text
Container: running
```

and:

```text
Service: actually working
```

A container can be running while the application inside it isn't responding properly.

The server can be running while the network isn't.

The router can be running while the internet connection isn't.

Apparently I needed something whose entire job was to ask:

**Are you alive?**

Repeatedly.

Forever.

## 💚 Enter Uptime Kuma

That led me to **Uptime Kuma**.

Naturally, it became another Docker container.

```text
Ubuntu Server
 │
 └── Docker
      ├── Portainer
      ├── Home Assistant
      ├── Caddy
      └── Uptime Kuma
```

I now had software monitoring the software running on the server that was running the monitoring software.

This seemed completely reasonable (not).

## 🖥️ Start with the homelab

The obvious first targets were the services I already had.

Portainer.

Home Assistant.

And Uptime Kuma itself.

That last one felt slightly strange.

```text
Uptime Kuma
     │
     ├── Is Portainer alive?
     │
     ├── Is Home Assistant alive?
     │
     └── Am I alive?
```

But it gave me one place where I could quickly see the state of the homelab.

Green was good.

Red was going to become somebody's problem.

Unfortunately, that somebody was me.

## 🌐 What about the network?

Once I could monitor containers, another question appeared.

The homelab didn't exist in isolation.

It depended on the network.

So I added the **Freebox**.

Now I could see whether my router was reachable.

Then I thought:

Wait.

The Freebox being reachable doesn't necessarily mean I have internet access.

So I added an external internet check as well.

Now the distinction became much clearer:

```text
Ubuntu Server
     │
     ├── Home Assistant     ●
     ├── Portainer          ●
     ├── Uptime Kuma        ●
     │
     ├── Freebox            ●
     │
     └── Internet           ●
```

For the first time, if something stopped working, I could start narrowing down **where** it had stopped working.

That felt useful.

## 🌍 If I'm monitoring things...

I also had a website outside the homelab.

So naturally:

**Why not monitor that too?**

The scope was expanding.

Uptime Kuma was no longer just checking Docker containers.

It was becoming a small overview of the things I depended on:

```text
Monitoring
 │
 ├── Homelab
 │    ├── Portainer
 │    ├── Home Assistant
 │    └── Uptime Kuma
 │
 ├── Network
 │    ├── Freebox
 │    └── Internet
 │
 └── External
      └── Website
```

One container had gone from:

> Tell me if Home Assistant is working.

to:

> Tell me if my infrastructure, network and external services are working.

The pit was becoming organised.

## 🔐 Monitoring HTTPS introduced another problem

There was, however, a slight complication.

I had just spent all that time creating internal HTTPS using my own Caddy Certificate Authority.

My Mac trusted it.

Uptime Kuma did not necessarily share my Mac's enthusiasm.

From Kuma's point of view, some of my beautifully secured internal services were using certificates issued by a Certificate Authority it didn't know.

So something could work perfectly in my browser...

and appear unhealthy in monitoring.

Once again:

```text
"It works."
```

turned out to depend on **who was asking**.

Another reminder that trust isn't universal.

Every client has its own trust store and its own view of what constitutes a valid certificate.

The certificate rabbit hole from the previous entry had followed me into this one.

## 📊 Green dots are surprisingly addictive

There was something very satisfying about seeing everything together.

```text
Portainer        ● UP
Home Assistant   ● UP
Uptime Kuma      ● UP
Freebox          ● UP
Internet         ● UP
Website          ● UP
```

It wasn't doing anything particularly complicated.

But I no longer needed to open five different things to answer a basic question.

I could look at one screen and understand the state of the system.

And once I had that...

I immediately wanted to organise it better.

I started thinking in groups.

**Homelab internals.**

**Connectivity.**

**External services.**

Apparently even my monitoring needed information architecture.

## 🤔 What I thought at the time

This was probably the first point where the homelab started feeling like a **system** rather than a collection of experiments.

There were applications.

There was networking.

There was HTTPS.

There was monitoring.

And the different pieces were beginning to depend on each other.

I also started to realise that simply knowing whether something was **up** wasn't the same as knowing whether it was **healthy**.

Uptime Kuma could tell me that the Ubuntu server was reachable.

But what was the CPU doing?

How much RAM was being used?

How much disk space was left?

How many containers were running?

Monitoring availability had answered one question.

And, predictably, created several more.

## 🧠 What I learned

A running container doesn't necessarily mean a healthy application.

A reachable router doesn't necessarily mean a working internet connection.

Monitoring different layers separately makes troubleshooting much easier.

Internal certificates need to be trusted by monitoring systems too, not just by my browser.

And a simple status page can make a growing collection of services feel much more manageable.

Most importantly:

**once you start measuring whether things are working, you immediately want to measure how well they're working.**

## 🕳️ How much deeper did the pit get?

I started with:

```text
"Is Home Assistant still running?"
```

I ended with:

```text
                    Uptime Kuma
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       Homelab        Network        External
          │              │              │
     ┌────┼────┐      ┌──┴──┐           │
     │    │    │      │     │           │
    HA   Port. Kuma  Freebox Internet  Website
```

Everything was green.

Excellent.

But now that I knew everything was **up**, another question was becoming difficult to ignore:

**What is the server actually doing?**

CPU.

Memory.

Disk.

Network.

Containers.

Uptime.

I wanted numbers.

And preferably...

a nice dashboard.

⛏️ *The pit had discovered observability.*