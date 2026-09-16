---
entry: 0003
title: "I only wanted the warning to go away"
date: 2026-09-12
tags:
  - caddy
  - https
  - tls
  - reverse-proxy
  - certificates
  - home-assistant
  - portainer
status: complete
---

# 0003 — I only wanted the warning to go away

![Caddy](https://img.shields.io/badge/Caddy-Reverse_Proxy-1F88C0?logo=caddy&logoColor=white)
![Portainer](https://img.shields.io/badge/Portainer-13BEF9?logo=portainer&logoColor=white)
![Home Assistant](https://img.shields.io/badge/Home_Assistant-18BCF2?logo=homeassistant&logoColor=white)
![HTTPS](https://img.shields.io/badge/HTTPS-TLS-2E8B57?logo=letsencrypt&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

On [0002 — Okay, but what do I actually host?](0002-okay-but-what-do-i-actually-host.md) everything was working.

Portainer was running.

Home Assistant was running.

I could open both from my Mac.

There was just one thing bothering me.

My browser didn't particularly trust what I had built.

## ⚠️ That little browser warning

Portainer was available over HTTPS, but it was using a self-signed certificate.

Technically, the connection was encrypted.

Practically, my browser was still showing me a security warning.

I could have accepted the warning and moved on.

That would have been reasonable.

Instead, I thought:

**Can I make this look properly trusted?**

This turned out to be another one of those questions where the answer is:

> Yes.

followed immediately by:

> How much time do you have?

## 🔐 Apparently I need certificates now

Until this point, HTTPS was something websites had.

You visited a website.

There was a little padlock.

Everything happened somewhere in the background.

Now I was the person responsible for the background.

I started learning about:

- TLS certificates
- certificate authorities
- certificate chains
- private keys
- self-signed certificates
- trusted root certificates

All because I didn't like a browser warning.

The pit had found another subject.

## 🌐 Enter Caddy

I wanted something that could sit in front of my services and handle HTTPS cleanly.

That led me to **Caddy**.

The idea was straightforward:

```text
Browser
   │
   │ HTTPS
   ▼
 Caddy
   │
   ├── Portainer
   │
   └── Home Assistant
```

Instead of remembering ports and accessing services directly, Caddy could become the front door.

That also meant I could start giving services proper internal names.

Something like:

```text
portainer.home.arpa
ha.home.arpa
```

This was much nicer than:

```text
<server-ip>:<random-port>
```

Suddenly the homelab was starting to feel less like a collection of containers and more like actual infrastructure.

## 🏠 `.home.arpa`

For the internal domain, I settled on:

```text
home.arpa
```

So services could have names such as:

```text
portainer.home.arpa
ha.home.arpa
```

There was something disproportionately satisfying about typing:

```text
https://portainer.home.arpa
```

and seeing my own service appear.

Of course, getting the name to resolve was another matter.

At one point:

```text
server not found
```

made an appearance.

Because apparently having a hostname and having the network know what that hostname means are two separate things.

Another lesson learned.

## 🏛️ I accidentally became a Certificate Authority

Public websites can obtain certificates from public certificate authorities.

My services were internal.

Nobody on the public internet needed to know that `portainer.home.arpa` existed.

Caddy could create its own local Certificate Authority and issue certificates for my internal services.

There was only one problem.

My Mac had absolutely no reason to trust a Certificate Authority that had just appeared inside an Ubuntu VM.

So I exported Caddy's root CA certificate and added it to the trusted certificates on my Mac.

And then something rather satisfying happened.

The warning disappeared.

```text
Mac
 │
 │ trusts
 ▼
Caddy Local CA
 │
 │ issues certificates for
 ▼
*.home.arpa
```

My browser trusted my internal HTTPS.

I had created my own little chain of trust.

At home.

For a server running inside my Mac.

Perfectly normal behaviour.

## 🔒 Portainer gets a proper certificate

Portainer had originally been serving its own self-signed certificate.

Now that Caddy had a trusted local CA, I could do better.

I used the certificate and key generated through Caddy for Portainer.

The browser warning that started this entire adventure was finally gone.

Mission accomplished.

This would have been another excellent place to stop.

I did not stop.

## 🏠 Home Assistant should use HTTPS too

If Portainer could have a nice internal address, obviously Home Assistant should have one as well.

So:

```text
https://ha.home.arpa
```

was next.

Caddy would receive the HTTPS request and proxy it to Home Assistant.

Simple.

```text
Browser
   │
   │ HTTPS
   ▼
 Caddy
   │
   │ HTTP
   ▼
Home Assistant
```

Except Home Assistant was not particularly impressed by this arrangement.

Instead of my dashboard, I got:

```text
400 Bad Request
```

Excellent.

## 🔄 Welcome to reverse proxies

The problem was that Home Assistant could see requests arriving from Caddy rather than directly from my Mac.

And Home Assistant doesn't blindly trust reverse proxies.

Which is a good thing.

It just wasn't a particularly convenient thing at that exact moment.

I needed to configure Home Assistant to understand that it was behind a trusted proxy.

That meant adding settings for forwarded requests and trusted proxy addresses.

Something along the lines of:

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - <ip addr>
```

Now another concept entered the homelab vocabulary:

**reverse proxy trust.**

Caddy wasn't simply forwarding traffic.

It was also passing information about where the original request came from.

And Home Assistant needed to know whether it could trust that information.

## 🧅 There is always another layer

This was becoming a pattern.

Every solution revealed another layer underneath it.

```text
Application
    ↓
Container
    ↓
Docker
    ↓
Network
    ↓
Reverse proxy
    ↓
TLS
    ↓
Certificates
    ↓
Certificate Authority
    ↓
Trust
```

I had only wanted the warning to disappear.

## 🧠 What I learned

HTTPS isn't simply an on/off switch.

A certificate can encrypt a connection without being trusted by the client.

Trust ultimately comes from Certificate Authorities.

For a completely internal homelab, running a private CA can make sense.

A reverse proxy gives services a single, consistent entry point and lets them have memorable internal hostnames.

But putting something behind a reverse proxy can change what the application sees about incoming connections.

And when an application complains about a proxy it doesn't trust, that's usually a security feature rather than something to work around blindly.

Most importantly:

**cosmetic annoyances are capable of producing surprisingly large infrastructure projects.**

## 🕳️ How much deeper did the pit get?

I started with:

```text
"I don't like this browser warning."
```

I ended with:

```text
Mac
 │
 │ trusts
 ▼
Caddy Local CA
 │
 ▼
Caddy
 ├── https://portainer.home.arpa
 │        │
 │        └── Portainer
 │
 └── https://ha.home.arpa
          │
          └── Home Assistant
```

The browser warning was gone.

The services had proper names.

HTTPS worked internally.

Home Assistant understood the reverse proxy.

Everything was starting to look surprisingly professional.

Which naturally created a new problem.

I now had several services running...

**How would I know if one of them went down?**

⛏️ *Time to start monitoring the things I had created.*