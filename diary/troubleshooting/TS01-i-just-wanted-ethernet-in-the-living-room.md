---
entry: TS01
title: "I just wanted Ethernet in the living room"
date: 2026-09-16
status: resolved
category: networking
tags:
  - ethernet
  - rj45
  - raspberry-pi
  - network-switch
  - wifi-extender
  - cabling
  - network-testing
  - troubleshooting
---

# TS01 — I just wanted Ethernet in the living room

![Ethernet](https://img.shields.io/badge/Ethernet-Gigabit-0078D4)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-4-C51A4A?logo=raspberrypi&logoColor=white)
![TP-Link](https://img.shields.io/badge/TP--Link-Networking-4ACBD6?logo=tplink&logoColor=white)
![RJ45](https://img.shields.io/badge/RJ45-Structured_Cabling-555555)
![Status](https://img.shields.io/badge/Status-Resolved-success)

> [!NOTE]
> **Problem:** Getting reliable Ethernet connectivity into the living room  
> **Hardware:** TP-Link RE705X, TP-Link TL-SG108E and Raspberry Pi 4  
> **Tools:** RJ45 cable tester and a lot of trial and error  
> **Result:** Existing Ethernet restored and the apartment cabling finally started making sense


The plan seemed straightforward.

I wanted better network connectivity in the living room.

The Freebox wasn't there anymore, but I had devices that would benefit from Ethernet and I wanted the option of connecting more things there in the future.

So naturally, I bought more networking hardware.

## 📦 New toys

The first additions were:

- **TP-Link RE705X** Wi-Fi 6 range extender
- **TP-Link TL-SG108E** managed Gigabit switch

The idea was to improve connectivity and give myself several Ethernet ports in the living room.

Something roughly like:

```text
Network
   │
   ▼
TP-Link RE705X
   │
   ▼
TP-Link TL-SG108E
   │
   ├── Device
   ├── Device
   ├── Device
   └── ...
```

A Wi-Fi extender.

A switch.

A few Ethernet cables.

How complicated could this possibly become?

## 🥧 Enter the Raspberry Pi

I also had a **Raspberry Pi 4** available.

That made it a convenient little test machine.

Instead of trying to diagnose the network through whatever device happened to be connected, I could plug the Pi into different points and see what actually happened.

So the Pi became my network guinea pig.

```text
Ethernet
   │
   ▼
Raspberry Pi 4
   │
   ▼
"Do I have a network?"
```

Move it.

Plug it in.

Test.

Change something.

Test again.

For troubleshooting, having a small device that I could easily move around was surprisingly useful.

And this is where the original plan started changing.

## 🤔 Wait... there is already Ethernet here

There were Ethernet sockets in the apartment walls.

More importantly, the Freebox had **previously been in the living room and connected through one of them**.

That raised an obvious question.

Why was I trying to work around the lack of Ethernet with Wi-Fi...

when the apartment already had Ethernet cabling?

If that existing run could be restored, the setup could instead become:

```text
Freebox / Network
       │
       │ existing in-wall Ethernet
       ▼
Living room RJ45
       │
       ▼
TP-Link TL-SG108E
       │
       ├── Raspberry Pi
       ├── Device
       ├── Device
       └── ...
```

That would be much better.

There was only one problem.

The Ethernet connection wasn't behaving properly.

## 🧱 The mystery inside the wall

From the living room I could see:

```text
RJ45 socket
    │
    │
    │  somewhere inside the wall...
    │
    ▼
???
```

And inside the communications cabinet I had several cables and modules that looked remarkably similar.

Some were connected.

Some were loose.

There was DTI equipment.

And none of them came with a helpful label saying:

```text
HELLO.
I AM THE LIVING ROOM.
```

So what started as:

> Let's connect a switch in the living room.

became:

> Where does this socket actually go?

## ☎️ And what exactly is a DTI?

The cabinet wasn't simply an Ethernet patch panel.

There was also telephone infrastructure, including the DTI.

That meant not every cable or socket I could see was necessarily part of the Ethernet network I was trying to build.

So before fixing anything, I first had to separate:

```text
Telephone infrastructure
```

from:

```text
Ethernet infrastructure
```

This is one of those things that seems obvious once you understand the cabinet.

Before that, it is mostly a collection of white cables disappearing into a wall.

## 🔎 Time to trace cables

Guessing wasn't getting me very far.

So I used an RJ45 cable tester.

The method was simple:

```text
Wall socket
    │
    │
 [REMOTE]


 [MASTER]
    │
    │
Cabinet cable
```

If I had found the correct cable, the tester should step consistently through:

```text
1 2 3 4 5 6 7 8
```


Just the tester and the cable run.

Suddenly I could stop guessing and actually trace what was hidden inside the walls.

## 💡 1... 2... 3... 4...

The tester quickly became the most useful tool in the investigation.

A healthy run should give me all eight conductors consistently:

```text
1 → 1
2 → 2
3 → 3
4 → 4
5 → 5
6 → 6
7 → 7
8 → 8
```

So I started testing combinations.

One socket.

One cabinet cable.

Then another.

Then another.

This was essentially networking by elimination.

And slowly, the anonymous cables started acquiring identities.

## 🛏️ We have a bedroom

One of the runs eventually tested cleanly.

All eight conductors.

Consistently.

That gave me something surprisingly satisfying:

```text
UNKNOWN CABLE
      ↓
   testing
      ↓
BEDROOM
```

For the first time, one of the mystery connections had a name.

So I labelled it.

Because I had absolutely no intention of solving the same mystery twice.

## 🤨 But another cable wasn't behaving

Not every test was as cooperative.

One path gave inconsistent results.

With one combination I was seeing only:

```text
6 / 8
```

while another combination produced:

```text
8 / 8
```

That was important.

The tester wasn't simply telling me:

> This is the wrong cable.

It was helping isolate **which part of the path was unreliable**.

One of the cables we'd been using during testing was behaving intermittently.

So it was taken out of the equation.

That immediately made the results much more consistent.

## 🧪 Known-good cables matter

This was probably the most useful lesson from the whole exercise.

When troubleshooting something like:

```text
wall socket
    ↓
in-wall cable
    ↓
cabinet termination
    ↓
patch cable
    ↓
switch/router
```

there are several individual things that can fail.

If the patch cable you're using to test the wall cable is itself unreliable, the results become extremely confusing, while the actual problem may be sitting in your hand.

Once the questionable cable was removed and a known-good one was used, the picture became much clearer.

## 🔧 And then we found the actual problem

Eventually the investigation brought me back to the Ethernet termination itself.

The wiring looked correct.

The colours looked right.

Nothing immediately screamed:

```text
I AM BROKEN.
```

But Ethernet doesn't particularly care whether something *looks* connected.

It cares whether the conductors are actually making proper electrical contact.

So the module had to come apart.

This led to another slightly uncomfortable moment:

**Do I actually need to cut this cable to get it out?**

Thankfully, no.

The conductors could be released and the termination corrected without cutting away the cable just to free it.

Once the connection was properly restored and tested again:

```text
1 2 3 4 5 6 7 8
✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
```

We had Ethernet.

## 🟢 Ethernet restored

The important part was that the original assumption turned out to be correct.

The apartment **did already have a usable Ethernet path to the living room**.

The infrastructure hadn't disappeared.

It just needed troubleshooting.

And now the network could use the existing structured cabling instead of depending entirely on a wireless workaround.

```text
Network cabinet
      │
      │ in-wall Ethernet
      ▼
Living room
      │
      ▼
TP-Link TL-SG108E
      │
      ├── Raspberry Pi 4
      ├── Device
      ├── Device
      └── Future bad decisions
```

The switch suddenly made considerably more sense.

## 🏷️ Label everything

By this point I'd spent enough time figuring out where anonymous cables went that another rule became obvious:

**Nothing identified should ever become unidentified again.**

So known runs get labels.

```text
BEDROOM
LIVING ROOM
...
```

And anything unrelated to the Ethernet setup can be identified and kept out of the way.

Future me should be able to open this cabinet and understand it without repeating the archaeology.

At least that's the theory.

## 🤔 What I thought at the time

Originally, I was trying to solve a connectivity problem by adding equipment.

A Wi-Fi extender.

A managed switch.

A Raspberry Pi for testing.

Then I realised that the apartment already contained part of the solution inside the walls.

That changed the problem completely.

Instead of:

```text
How do I get Ethernet into the living room?
```

the question became:

```text
Why doesn't the Ethernet that's already in the living room work?
```

And then that question broke down into smaller ones:

```text
Which cable is which?

Does this run have continuity?

Do all eight conductors work?

Is this patch cable reliable?

Is the wall termination correct?

Is the cabinet termination correct?
```

Those were much easier questions to answer.

## 🧠 What I learned

Don't build around existing infrastructure before checking whether that infrastructure can simply be fixed.

A Raspberry Pi makes a very convenient portable network test machine.

A managed switch gives me room to expand the wired network once the underlying connection actually works.

A basic RJ45 tester can tell me considerably more than visual inspection.

All eight conductors matter for Gigabit Ethernet.

An intermittent test cable can make a perfectly good permanent cable run look faulty.

Known-good components are essential when troubleshooting by elimination.

And a termination that looks correct can still have a bad electrical connection.

Most importantly:

**sometimes the best network upgrade is fixing the cable that's already in the wall.**

## 🕳️ How much deeper did the pit get?

I started with:

```text
"I need better connectivity in the living room."
```

So I bought:

```text
TP-Link RE705X
      +
TP-Link TL-SG108E
      +
Raspberry Pi 4
```

And somehow ended up here:

```text
Wi-Fi / Ethernet problem
          │
          ▼
    Raspberry Pi tests
          │
          ▼
"Wait, the apartment has Ethernet"
          │
          ▼
 Communications cabinet
          │
          ├── DTI
          ├── mystery cables
          ├── RJ45 testing
          ├── intermittent cable
          ├── terminations
          └── labels
          │
          ▼
   Ethernet restored
          │
          ▼
    Living room switch
```

I bought hardware to work around a networking problem.

Then I discovered the network I wanted was already inside the walls.

Then I fixed it.

The extender and switch may have started the investigation, but the most useful piece of equipment turned out to be a cable tester.

And the Raspberry Pi?

It had accidentally acquired another job:

**network test equipment.**

Perfect.

⛏️ *The pit has now expanded into the walls.*