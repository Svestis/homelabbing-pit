---
entry: 0001
title: "It started with an Ubuntu VM"
date: 2026-09-10
tags:
  - ubuntu
  - utm
  - ssh
  - docker
  - portainer
status: complete
---

# 0001 — It started with an Ubuntu VM

![Ubuntu](https://img.shields.io/badge/Ubuntu-Server-E95420?logo=ubuntu&logoColor=white)
![UTM](https://img.shields.io/badge/UTM-Virtual_Machine-5A67D8)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Portainer](https://img.shields.io/badge/Portainer-13BEF9?logo=portainer&logoColor=white)
![SSH](https://img.shields.io/badge/SSH-OpenSSH-000000?logo=openssh&logoColor=white)

I wasn't planning to build a homelab.

I had a Mac, some curiosity, and the idea that having a Linux server around might be useful.

Nothing complicated. Nothing permanent.

Just an Ubuntu Server VM running on my Mac.

That was supposed to be the project;
it was not...
## 🖥️ One little Ubuntu VM

I started with **Ubuntu Server running in UTM** on my Mac.

The VM was nothing particularly exciting:

- 4 CPU cores
- 8 GB RAM
- 50 GB storage
- Ubuntu Server
- No dedicated hardware
- No grand infrastructure plan

The idea was simply to learn, experiment, and have somewhere I could run things without cluttering up macOS.

Even getting that far introduced things I hadn't really needed to think about before.

Virtual networking. Network interfaces. IP addresses. SSH. Package management. Services.

At one point I was staring at the Ubuntu installer wondering why it was talking about **Ethernet when my Mac wasn't connected to Ethernet**.

A small indication of what was coming.

## 🔑 The first satisfying moment

I installed OpenSSH Server and tried connecting to the VM from Terminal on my Mac.

It was a tiny thing, but it changed how the VM felt.

I wasn't opening UTM anymore and interacting with a virtual computer.

I had a **server**.

I could leave Ubuntu sitting there and manage it remotely from my Mac.

And once you have a server, there is an obvious question:

**What can I run on it?**

That question was probably the entrance to the pit.

## 🐳 Enter Docker

I didn't want every experiment to mean installing applications directly into Ubuntu, modifying the system, and eventually forgetting what I had changed.

Containers seemed like the answer.

So I installed Docker.

Then came:

```bash
docker run hello-world
```

And it worked.

At this point the setup was still wonderfully simple:

```text
Mac
 │
 └── UTM
      │
      └── Ubuntu Server
           │
           └── Docker
```

This would have been an excellent place to stop.

I did not stop.

## 📦 Containers need managing

Docker immediately created another question.

If I'm going to have multiple containers running, how do I keep track of them?

Of course, there was container for that.

So the first real service arrived:

**Portainer.**

Suddenly I had a web interface where I could see containers, images, volumes, networks and logs.

The server was no longer an empty Ubuntu installation.

It had infrastructure.

```text
Mac
 │
 └── UTM
      │
      └── Ubuntu Server
           │
           └── Docker
                │
                └── Portainer
```

And that felt surprisingly good.

## 🤔 What I thought at the time

The setup still seemed temporary.

If something went horribly wrong, I could delete the VM and start again.

That freedom made it very easy to say:

> I'll just try one more thing.

I would eventually discover that this sentence is extremely dangerous in a homelab.

## 🧠 What I learned

A few concepts suddenly became much less abstract.

I understood the difference between the host, VM and containers much better once I was actually using all three.

I understood why SSH is such a fundamental part of managing Linux servers.

Docker started making sense as something more useful than a technology I'd simply read about.

And perhaps most importantly, I learned that getting something running immediately makes you want to improve it.

Once Portainer was available, I wanted something worth managing with it.

## 🕳️ How much deeper did the pit get?

I started with:

```text
"I'll create an Ubuntu VM."
```

I ended with:

```text
Mac
 └── UTM
      └── Ubuntu Server
           ├── SSH
           └── Docker
                └── Portainer
```

Not bad.

Still completely under control.

Obviously.

The only problem was that I now had a perfectly functional Docker server with almost nothing running on it.

So naturally, the next question was:

**What should I host?**

⛏️ *The digging had begun.*