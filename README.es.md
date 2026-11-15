# robo-que-conversa — qué kit comprar para tener un robot con IA que conversa con las personas

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Tu robot que conversa](guia/assets/banner-es.jpg)](https://inematds.github.io/robo-que-conversa/guia/es/)

## Qué es

Esta guía es una **investigación de compra** para quienes quieren un robot que converse con las personas usando inteligencia artificial (IA). Compara 9 kits en tres grupos: robots de escritorio que mueven la cabeza, placas con pantalla para montar un asistente de voz y robots con ruedas, cámara, micrófono y altavoz. Para cada uno puedes ver el precio en dólares, qué incluye la caja, si funciona por sí solo y qué IA usa. Los datos son del 14/11/2026: **todavía no se compró ni probó nada**, y los precios cambian. Solo tienes que leer; quien quiera también cuenta con un pequeño programa que filtra los kits según lo que necesita.

## 📖 Guía

Guía completa (grupos, tablas, precios y cuál comprar): **https://inematds.github.io/robo-que-conversa/guia/es/**

## Qué hay aquí

| Archivo | Para qué sirve |
|---|---|
| [FATOS.md](FATOS.md) | Cada número con fuente y fecha (fuente única de la guía y del video) |
| [datos/produtos.json](dados/produtos.json) | Los 9 kits: precio en US$, ruedas, cámara, micrófono, voz, pantalla, batería, Wi-Fi, IA, enlace |
| [escolher.py](escolher.py) | Filtra los kits según lo que necesitas (solo Python 3, sin instalar nada) |
| [test_escolher.py](test_escolher.py) | 8 pruebas del filtro |
| [guia/](guia/) | La página (PT, `en/`, `es/`) |

```bash
git clone https://github.com/inematds/robo-que-conversa.git
cd robo-que-conversa
python3 escolher.py --rodas --camera --ate 200   # PiCar-X y miniAuto Pro
python3 -m unittest test_escolher                # Ran 8 tests ... OK
```

## El proceso, de principio a fin

| # | Paso | Comando | Quién |
|---|---|---|---|
| 1 | Investigar los anuncios y las fichas de los fabricantes | enlaces del pedido + sitios oficiales | 🧠 sesión con Nei |
| 2 | Registrar cada número con fuente y fecha | `FATOS.md` | 🧠 |
| 3 | Actualizar los datos de los kits | `dados/produtos.json` | 🧠 |
| 4 | Probar el filtro | `python3 -m unittest test_escolher` | ⚙️ |
| 5 | Portada y banners (Codex) | `gerar-capa.cjs` y `gerar-banner.sh` (skill projetos-landing-guia) | ⚙️ |
| 6 | Guía PT y traducciones EN/ES | `guia/index.html`, `guia/en/`, `guia/es/` | 🧠 + ⚙️ `inema-traduz` |
| 7 | Revisor independiente | Agent nuevo mediante el runbook `revisor-independente.md` | 🤖 |
| 8 | Publicar | `git push` (GitHub Pages mediante Actions) | ⚙️ |
| 9 | Video explicativo 16:9 y 9:16 en lives6 | `~/projetos/explicavideos/textos/robo-que-conversa/roda.sh` | 🤖 `claude -p` |
| 10 | Video en la guía, el portal y Telegram INEMA.ROBOT | vigia `continua` (fase 2) | 🤖 |

---
INEMA.CLUB · https://inema.club
