---
entry: 0002
title: "Okay, but what do I actually host?"
date: 2026-09-11
tags:
  - home-assistant
  - docker
  - homekit
  - smart-home
  - containers
status: complete
---

# 0002 — Okay, but what do I actually host?

![Home Assistant](https://img.shields.io/badge/Home_Assistant-18BCF2?logo=homeassistant&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![HomeKit](https://img.shields.io/badge/HomeKit-Smart_Home-000000?logo=apple&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?logo=ubuntu&logoColor=white)

At the end of [0001 — It started with an Ubuntu VM](0001-it-started-with-an-ubuntu-vm.md), I had managed to create a perfectly functional Docker server.

There was only one small problem.

It wasn't actually doing anything useful.

I had Ubuntu.

I had Docker.

I had Portainer.

I had a nice web interface where I could admire my almost completely empty collection of containers.

So the obvious question was:

**What should I actually host?**

## 🏠 Something I would actually use

I already had smart devices around the house.

Most of them were living quite happily in Apple's ecosystem.

But if I now had my own server running 24/7, home automation seemed like exactly the sort of thing it should be doing.

That led me to **Home Assistant**.

And this felt different from installing Portainer.

Portainer existed to manage the server.

Home Assistant gave the server a reason to exist.

## 🐳 Another container enters the pit

By now, Docker was becoming the obvious way to add things.

So Home Assistant became another container.

The basic architecture was still reassuringly simple:

```text
Mac
 │
 └── UTM
      │
      └── Ubuntu Server
           │
           └── Docker
                ├── Portainer
                └── Home Assistant
```

Except this container had something Portainer didn't.

My house.

Suddenly the little Ubuntu VM running inside my Mac could see and interact with things in the physical world around it.

That was considerably more interesting than `hello-world`.

## 🍎 Surely everything will just appear...

A lot of my existing smart-home setup revolved around Apple Home and HomeKit.

So naturally, I hoped Home Assistant would discover everything and I would spend the next ten minutes clicking **Add**.

That was optimistic.

Nothing appeared.


At one point Home Assistant was telling me:

> No unpaired devices could be found.

Which introduced me to an important lesson about smart-home ecosystems:

**"Compatible" and "immediately available to Home Assistant" are not necessarily the same thing.**

My Meross bedside lamp, for example, was already a native HomeKit device.

That didn't automatically mean Home Assistant could simply take control of it.

Apparently devices have relationships too.

## 🔎 Integrations, integrations, integrations

Once I started exploring Home Assistant properly, I realised that the real power wasn't just controlling a light from another interface.

It was bringing different ecosystems together.

I started looking through integrations for things I already had:

- iCloud
- HomeKit
- Matter
- Apple-related devices and services
- Meross devices
- weather
- sensors

This was the first time the homelab started connecting things that hadn't necessarily been designed to work together.

And, naturally, every integration introduced another thing to understand.

## 💾 Wait... where does the data live?

Home Assistant also introduced another concept that suddenly mattered much more:

**persistent data.**

A container itself could disappear and be recreated.

My Home Assistant configuration should not disappear with it.

So I needed to start thinking about the difference between:

```text
Container
    │
    │ disposable
    ▼

Application data
    │
    │ definitely not disposable
    ▼
Persistent storage
```

That seems obvious now.

It was much less obvious when I had only just started using Docker.

My homelab was no longer just a collection of things I could delete without thinking.

It was beginning to contain **state**.

## 🤔 What I thought at the time

Before Home Assistant, if the VM disappeared, I would mostly have lost an experiment.

Now I was configuring devices, integrations and settings that I didn't particularly want to configure again.

For the first time I had something on the server that I actually cared about keeping.

That would eventually create another question:

**Should I be backing this stuff up?**

But apparently I wasn't ready to worry about that yet.

There were more immediate problems to create first.

## 🧠 What I learned

Home Assistant taught me quite a bit more than home automation.

Docker containers are disposable.

Their data often isn't.

Hardware access from inside a container introduces another layer of permissions and capabilities.

Smart-home standards such as HomeKit and Matter don't magically make every device available everywhere.

And running something yourself is very different from simply using a cloud service.

When it works, you control it.

When it doesn't work...

You also control that.

## 🕳️ How much deeper did the pit get?

I started with:

```text
"What should I host?"
```

I ended with:

```text
Mac
 └── UTM
      └── Ubuntu Server
           ├── SSH
           └── Docker
                ├── Portainer
                └── Home Assistant
                     ├── HomeKit
                     ├── integrations
                     ├── devices
                     ├── persistent data
                     └── Bluetooth problems
```

The server was finally doing something useful.

I could access Portainer in a browser.

I could access Home Assistant in a browser.

Everything was working.

Well...

Almost everything.

There was one little thing that kept bothering me every time I opened Portainer:

**Why is my browser warning me that this connection isn't secure?**

⛏️ *And somewhere in the distance, Caddy was waiting.*