
<p align="center">
  <img src="assets/homelabbing-pit.png" alt="Homelabbing Pit" width="100%">
</p>

> 
> 
> 
> 
> It started with an Ubuntu VM.  
> There is always one more service.

My descent into the bottomless pit of homelabbing.

This is where I keep track of what I built, what I tried, what broke, what I learned, what I changed my mind about, and all the rabbit holes I fell into along the way.

This isn't meant to be a tutorial or a polished guide. It's the story of my homelab as it evolves — including the mistakes, questionable decisions, and *"while I'm here, I might as well..."* moments.

## 🕳️ Latest from the pit

<!-- LATEST:START -->

> 🤖 **Generated automatically:** The latest entries from across the pit.

| Type | # | Date | Entry |
|---|---:|---|---|
| 📖 Diary | `0011` | 2026-09-22 | [The VM was never supposed to become a server](diary/entries/0011-the-vm-was-never-supposed-to-become-a-server.md) |
| 🚨 Incident | `II02` | 2026-09-20 | [Kopia woke up before the clock](diary/incidents/II02-kopia-woke-up-before-the-clock.md) |
| 📖 Diary | `0010` | 2026-09-19 | [I should probably manage the host too](diary/entries/0010-i-should-probably-manage-the-host-too.md) |

<!-- LATEST:END -->

> 🔎 **Looking for something?** `Ctrl+F` / `⌘F` your way through, or head straight to the [**full index**](#everything-in-the-pit).

## ⛏️ Start digging

There are a few different ways things end up documented here.

### 📖 [The diary](diary/)

The main story.

Follow the homelab from the first Ubuntu VM through everything I built, added, changed, learned, and probably didn't need.

### 🚨 [Infrastructure incidents](diary/incidents/)

Things that broke without being invited to.

Outages, failures, unexpected behaviour, and those moments when the infrastructure decides it would also like to contribute to the diary.

### 🔧 [Troubleshooting](diary/troubleshooting/)

Problems that became investigations of their own.

The rabbit holes involving cables, networking, configuration, documentation, questionable assumptions, and eventually — hopefully — an explanation.

### 🧪 [Projects](diary/projects/)

Things that refused to fit into a single diary entry.

Longer-running builds, experiments, designs and enhancements that keep evolving while the main diary moves on.

## 🏗️ What is this running on?

The pit currently looks roughly like this:

<p align="center">
  <img src="assets/the-pit.png" alt="The Pit" width="100%">
</p>


This is deliberately a snapshot rather than a specification.

The homelab keeps changing. That's rather the point.

## 🗂️ Repository map

<pre>
homelabbing-pit/
├── <a href="diary/">diary/</a>
│   ├── <a href="diary/README.md">README.md</a>                 # where the story starts
│   ├── <a href="diary/entries/">entries/</a>                  # the main descent
│   ├── <a href="diary/incidents/">incidents/</a>                # things broke
│   ├── <a href="diary/troubleshooting/">troubleshooting/</a>          # why did that happen?
│   └── <a href="diary/projects/">projects/</a>                 # things that kept growing
│
├── <a href="architecture/">architecture/</a>              # diagrams and architecture snapshots
├── <a href="assets/">assets/</a>                    # images and other repository assets
├── <a href="scripts/">scripts/</a>                   # keeping the pit organised
└── <a href="telemetry/">telemetry/</a>                 # the pit is talking to the world
</pre>

The indexes under `diary/` are generated automatically from the metadata in each entry.

The stories themselves are very much written by a human who probably should have stopped adding services several containers ago.

## 🧭 Is there a roadmap?

Not really.

There are ideas.

There are plans.

There are things I definitely don't need.

And there is an alarming amount of overlap between those three categories.

## 🕳️ Current status

Still digging. ⛏️

<a id="everything-in-the-pit"></a>
# 🗂️ Everything in the pit

Looking for something specific?

This is the complete index of everything documented in the pit.

<!-- PIT-INDEX:START -->

> 🤖 **Generated automatically:** This index is rebuilt from repository metadata.

| Type | # | Date | Entry |
|---|---:|---|---|
| 📖 Diary | `0011` | 2026-09-22 | [The VM was never supposed to become a server](diary/entries/0011-the-vm-was-never-supposed-to-become-a-server.md) |
| 🚨 Incident | `II02` | 2026-09-20 | [Kopia woke up before the clock](diary/incidents/II02-kopia-woke-up-before-the-clock.md) |
| 📖 Diary | `0010` | 2026-09-19 | [I should probably manage the host too](diary/entries/0010-i-should-probably-manage-the-host-too.md) |
| 📖 Diary | `0009` | 2026-09-18 | [Do I need a NAS?](diary/entries/0009-do-i-need-a-nas.md) |
| 📖 Diary | `0008` | 2026-09-17 | [The homelab needs a screen](diary/entries/0008-the-homelab-needs-a-screen.md) |
| 🔧 Troubleshooting | `TS01` | 2026-09-16 | [I just wanted Ethernet in the living room](diary/troubleshooting/TS01-i-just-wanted-ethernet-in-the-living-room.md) |
| 📖 Diary | `0007` | 2026-09-16 | [My photos live here now](diary/entries/0007-my-photos-live-here-now.md) |
| 📖 Diary | `0006` | 2026-09-15 | [I should probably back this up](diary/entries/0006-i-should-probably-back-this-up.md) |
| 📖 Diary | `0005` | 2026-09-14 | [I wanted a dashboard](diary/entries/0005-i-wanted-a-dashboard.md) |
| 🚨 Incident | `II01` | 2026-09-13 | [Well, that didn't take long](diary/incidents/II01-freebox-step-6.md) |
| 📖 Diary | `0004` | 2026-09-13 | [Is everything still alive?](diary/entries/0004-is-everything-still-alive.md) |
| 📖 Diary | `0003` | 2026-09-12 | [I only wanted the warning to go away](diary/entries/0003-i-only-wanted-the-warning-to-go-away.md) |
| 📖 Diary | `0002` | 2026-09-11 | [Okay, but what do I actually host?](diary/entries/0002-okay-but-what-do-i-actually-host.md) |
| 📖 Diary | `0001` | 2026-09-10 | [It started with an Ubuntu VM](diary/entries/0001-it-started-with-an-ubuntu-vm.md) |

<!-- PIT-INDEX:END -->
