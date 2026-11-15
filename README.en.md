# robo-que-conversa — which kit to buy for a conversational AI robot

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Your conversational robot](guia/assets/banner-en.jpg)](https://inematds.github.io/robo-que-conversa/guia/en/)

## What it is

This guide is a **buying guide** for anyone who wants a robot that talks with people using artificial intelligence (AI). It compares 9 kits in three groups: tabletop robots that move their heads, boards with screens for building a voice assistant, and robots with wheels, a camera, a microphone, and a speaker. For each one, you can see the price in dollars, what’s included in the box, whether it works on its own, and which AI it uses. The data is from 11/14/2026: **nothing has been purchased or tested yet**, and prices change. Just read the guide; there’s also a small program that filters the kits based on what you need.

## 📖 Guide

Complete guide (groups, tables, prices, and which one to buy): **https://inematds.github.io/robo-que-conversa/guia/en/**

🎬 Video: https://www.youtube.com/watch?v=hGNsx_B-JKA · Short: https://youtube.com/shorts/gg5jEXzIjes

## What’s included

| File | What it’s for |
|---|---|
| [FATOS.md](FATOS.md) | Every number with its source and date (the sole source for the guide and video) |
| [dados/produtos.json](dados/produtos.json) | The 9 kits: price in US$, wheels, camera, microphone, voice, screen, battery, Wi-Fi, AI, link |
| [escolher.py](escolher.py) | Filters the kits based on what you need (Python 3 only; nothing to install) |
| [test_escolher.py](test_escolher.py) | 8 filter tests |
| [guia/](guia/) | The page (PT, `en/`, `es/`) |

```bash
git clone https://github.com/inematds/robo-que-conversa.git
cd robo-que-conversa
python3 escolher.py --rodas --camera --ate 200   # PiCar-X e miniAuto Pro
python3 -m unittest test_escolher                # Ran 8 tests ... OK
```

## The process, from start to finish

| # | Step | Command | Who |
|---|---|---|---|
| 1 | Research the listings and manufacturers’ specifications | links from the request + official websites | 🧠 session with Nei |
| 2 | Record each number with its source and date | `FATOS.md` | 🧠 |
| 3 | Update the kit data | `dados/produtos.json` | 🧠 |
| 4 | Test the filter | `python3 -m unittest test_escolher` | ⚙️ |
| 5 | Cover and banners (Codex) | `gerar-capa.cjs` and `gerar-banner.sh` (skill projetos-landing-guia) | ⚙️ |
| 6 | PT guide and EN/ES translations | `guia/index.html`, `guia/en/`, `guia/es/` | 🧠 + ⚙️ `inema-traduz` |
| 7 | Independent reviewer | New agent via the `revisor-independente.md` runbook | 🤖 |
| 8 | Publish | `git push` (GitHub Pages via Actions) | ⚙️ |
| 9 | 16:9 and 9:16 explainer videos on lives6 | `~/projetos/explicavideos/textos/robo-que-conversa/roda.sh` | 🤖 `claude -p` |
| 10 | Video on the guide, portal, and INEMA.ROBOT Telegram | `continua` watchdog (phase 2) | 🤖 |

---
INEMA.CLUB · https://inema.club
