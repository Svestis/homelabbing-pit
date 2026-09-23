---
entry: HD001
project: home-display
title: "I just wanted the photos somewhere we could see them"
date: 2026-09-22
type: journal
status: complete
tags:
  - home-display
  - immich
  - photos
  - docker
  - python
  - javascript
---

# HD001 — I just wanted the photos somewhere we could see them

![Home Display](https://img.shields.io/badge/Home_Display-Photos-000000)
![Immich](https://img.shields.io/badge/Immich-Photos-4250AF?logo=immich&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker&logoColor=white)

The idea for a Home Display had already appeared in [0008 — The homelab needs a screen](../../entries/0008-the-homelab-needs-a-screen.md).

But the first version I actually wanted to use came from somewhere much more personal.

My girlfriend had lost her cat; his name was **Brioche** but everyone called him **Boulis**.

We had photos of him and a lot of them were now safely sitting in Immich.

I wanted them somewhere we would actually see them.

*For Brioche — Boulis.*

*So the photos wouldn't just sit in storage.*

## I just wanted the photos somewhere we could see them

The idea was simple.

Take a selection of photos from Immich and put them on a screen.

I created a dedicated album in Immich specifically for the display.

The Home Display could then pull images from that album and rotate through them automatically.

```text
Immich
│
└── Home Display album
        │
        ▼
   Home Display
        │
        ▼
      Browser
        │
        ▼
      Photos
```

Every **20 seconds**, another photo.

That was enough to turn the photo library from somewhere I could go looking for memories into something that could quietly show them to us.

## A photo should still look like a photo

I didn't want the screen to feel like a web page with an image sitting inside it.

The photo needed to be the display.

But photos are inconveniently committed to having different shapes but the screen remained stubbornly rectangular.

So rather than stretching or aggressively cropping everything, the display kept the photo itself intact and used an ambient blurred version around it.

```text
┌─────────────────────────────────────┐
│                                     │
│        blurred photo backdrop       │
│                                     │
│       ┌─────────────────────┐       │
│       │                     │       │
│       │        photo        │       │
│       │                     │       │
│       └─────────────────────┘       │
│                                     │
│        blurred photo backdrop       │
│                                     │
└─────────────────────────────────────┘
```

The photos also had subtle movement rather than simply appearing as completely static images.

Nothing dramatic.

Just enough animation to make the display feel alive without turning Boulis into a PowerPoint presentation.

## It needed controls, apparently

Automatic rotation was fine until I actually wanted to interact with it.

Sometimes I wanted to stay on a photo, move on or go back.

So the display gained touch controls.

```text
Previous
   │
   ├── Pause / Resume
   │
   ├── Next
   │
   └── Brightness
```

The controls stayed out of the way until I interacted with the display.

The slideshow could be paused and resumed.

I could move backwards or forwards manually.

And because a bright screen in a dark room is an excellent way of discovering that something needs another setting, I added a dimmer too.

## The screen also needed to know when to calm down

Manual dimming solved one problem.

It didn't solve me having to remember to use it.

The display was meant to sit there rather than demand attention, so brightness also became dependent on the time of day.

During the night, the display automatically dimmed itself.

```text
Day
│
└── normal display

Night
│
└── automatically dimmed
```

The manual slider was still there when I wanted control.

But the screen could now make itself considerably less enthusiastic at night without being asked.

One less thing to remember.

## There was already a drawer with nothing in it

By this point I had also added a pull-down drawer.

It contained absolutely nothing.

The idea was that I should be able to pull down from the top of the display and get some quick information without turning the photo screen itself into a dashboard.

Things like:

- the time,
- the date,
- maybe the weather.

The important part was keeping that information separate.

The normal display remained about the photos.

If I wanted information, I could ask for it.

```text
┌─────────────────────────────┐
│        quick glance         │
│                             │
│    time / date / weather    │
├─────────────────────────────┤
│                             │
│                             │
│            photo            │
│                             │
│                             │
└─────────────────────────────┘
```

For now, though:

```text
Pull down
    │
    ▼
┌─────────────────┐
│                 │
│     nothing     │
│                 │
└─────────────────┘
```

Excellent foundation.

## And apparently it needed a home

The photo display wasn't the only interface I had started building.

A double tap opened a separate **Home** view.

At this point, Home was ambitious enough to say:

```text
Home

Choose a section below
```

There just wasn't very much to choose yet.

That was fine.

I wasn't trying to build everything at once.

I wanted the photo display to work first.

And it did.

## Underneath it was becoming a small application

The implementation was deliberately fairly simple.

The frontend was built with:

```text
HTML
CSS
JavaScript
```

A small Python backend handled the server-side part and talked to Immich.

```text
Dedicated Immich album
        │
        ▼
      Python
        │
        ▼
 HTML + CSS + JavaScript
        │
        ▼
      Browser
```

The application ran in Docker with the rest of the homelab, and Git gave me a way to develop it, push changes and update the deployed version without manually moving files around.

So what appeared on the screen as:

```text
photo
```

was actually becoming:

```text
Immich
   │
   ▼
Python
   │
   ▼
Home Display
   │
   ▼
Docker
   │
   ▼
Browser
   │
   ▼
photo
```

## The first version did what I wanted

There was plenty of empty space in the project.

Literally, in the case of the drawer.

But that wasn't a problem.

The display could already do the thing I had actually built it for.

It could take photos we cared about and put them somewhere we would see them.


Sometimes the useful part of self-hosting isn't having another service; It's finding something meaningful to do with the things you're already hosting.

## 🕳️ How much deeper did the pit get?

**Before:**

```text
Immich
└── Photos
    └── safely stored
```

**After:**

```text
Immich
└── Home Display album
        │
        ▼
   Home Display
   ├── Photo slideshow
   │   ├── 20-second rotation
   │   ├── Previous / Next
   │   ├── Pause / Resume
   │   └── Animation
   │
   ├── Brightness
   │   ├── Manual dimmer
   │   └── Automatic night dimming
   │
   ├── Pull-down drawer
   │   └── absolutely nothing
   │
   └── Home
       └── somewhere for things to go
```

The photos were already safe in Immich.

Now they had somewhere to live outside it too.

⛏️ **The pit became a little more personal.**

*For Boulis.*