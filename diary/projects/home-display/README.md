---
project: home-display
title: "Home Display"
description: "A home dashboard built for the living-room TV."
status: active
started: 2026-09-17
---

# 🖥️ Home Display

> I wanted some useful information on the TV. It escalated.

Home Display is a dashboard built for the living-room TV and, increasingly, another excuse to connect more things to the homelab.

It started as a fairly simple idea: put useful information somewhere visible without having to open an app, reach for a phone, or remember which dashboard contains what.

Then I started having ideas.

> 🔎 **Looking for something specific?** Jump straight to the [**Project index**](#project-index).

[← Back to projects](../)

---

## 🕳️ How this started

Home Display first appeared in the main diary when I started wondering what else the homelab could actually do around the house.

The television was already there, the Raspberry Pi was available and apparently that was enough justification to start another project.

The original experiment became:

**[0008 — The homelab needs a screen](../../entries/0008-the-homelab-needs-a-screen.md)**

That entry captures the moment the project started.

This page follows what happened after it refused to remain a single diary entry.

---

## 🎯 What I wanted

The basic idea is still fairly simple.

A display that can sit on the TV and provide useful information at a glance.

That means it should:

- work well from across the room;
- prioritise information rather than interaction;
- fit naturally into the rest of the homelab;
- surface things that are actually useful around the house;
- avoid becoming yet another dashboard that needs constant attention;
- remain simple enough that it can keep evolving without being rebuilt every week.

The last requirement is going particularly well.

---

## 🏗️ How it fits into the pit

Home Display is its own application, but it is also part of the wider homelab.

```text
                    THE PIT
                       │
                       │
                ┌──────▼──────┐
                │ Home Display │
                └──────┬──────┘
                       │
              information at a glance
                       │
                 ┌─────▼─────┐
                 │    TV     │
                 └───────────┘
```

This project documents how Home Display fits into the homelab and how it evolves over time.

Implementation details that are not useful to the story of the Pit stay outside this repository.

---

<a id="project-index"></a>

## 🧭 Inside the project

The project has somewhere to put things that would otherwise end up scattered through the main diary.

<pre>
home-display/
├── <a href="./README.md">README.md</a>          # you are here
├── <a href="./journal/">journal/</a>           # milestones, changes and decisions
├── <a href="./designs/">designs/</a>           # screenshots, mockups and visual experiments
└── <a href="./examples/">examples/</a>          # sanitised examples worth keeping
</pre>
Not every Home Display change deserves a numbered entry in the main homelab diary.

Things that belong specifically to this project can stay here instead.

---

## 🗂️ Project index

Everything documented inside this project will appear here automatically.

<!-- PROJECT-INDEX:START -->

> 🤖 **Generated automatically:** This index is rebuilt from project metadata.

| Type | # | Date | Entry | Status |
|---|---:|---|---|---|

<!-- PROJECT-INDEX:END -->

---

## 🖼️ Evolution

The project is still evolving.

What started as a display experiment has gradually become a place to explore how information from the homelab and the outside world can be presented in a way that actually works on a television.

That includes questions around:

- layout and information density;
- readability from across the room;
- weather and environmental information;

- photo collection display
- network related info
- server related info
- energy related info

- useful household information;
- visual hierarchy;
- what deserves to be on screen at all;
- and how much information is too much information.

Some ideas survive.

Some become screenshots.

Some become lessons.

---

## 🧪 Experiments

Not everything tried here is intended to become permanent.

This is where Home Display can explore new cards, data sources, layouts, visualisations and integrations before deciding whether they actually deserve to stay.

Experiments that become substantial enough can get their own notes in the project journal or supporting material under `designs/` and `examples/`.

---

## 📖 Project journal

The project journal follows the significant changes, decisions and occasional rabbit holes that happen after the original diary entry.

For now, the story starts here:

**[0008 — The homelab needs a screen](../../entries/0008-the-homelab-needs-a-screen.md)**

As the project evolves, its own milestones can live under [`journal/`](journal/).

---

## 🔗 Related

- 📖 [0008 — The homelab needs a screen](../../entries/0008-the-homelab-needs-a-screen.md)
- 🧪 [Projects](../README.md)

---

[← Back to projects](../)
