
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
| 📖 Diary | `0010` | 2026-09-19 | [I should probably manage the host too](diary/2026/09/0010-i-should-probably-manage-the-host-too.md) |
| 📖 Diary | `0009` | 2026-09-18 | [Do I need a NAS?](diary/2026/09/0009-do-i-need-a-nas.md) |
| 📖 Diary | `0008` | 2026-09-17 | [The homelab needs a screen](diary/2026/09/0008-the-homelab-needs-a-screen.md) |

<!-- LATEST:END -->


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

```text
homelabbing-pit/
├── diary/
│   ├── README.md
│   ├── YYYY/
│   │   └── MM/                # the main descent
│   ├── incidents/             # things broke
│   └── troubleshooting/       # why did that happen?
│
├── architecture/              # diagrams and architecture snapshots
├── assets/                    # images and other repository assets
├── scripts/                   # keeping the pit organised
└── telemetry/                 # the pit is talking to the world
```

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
