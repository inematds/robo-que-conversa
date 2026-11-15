# robo-que-conversa — qual kit comprar para ter um robô com IA que conversa com as pessoas

[![Seu robô que conversa](guia/assets/banner.jpg)](https://inematds.github.io/robo-que-conversa/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

Este guia é uma **pesquisa de compra** para quem quer um robô que conversa com as pessoas usando inteligência artificial (IA). Ele compara 9 kits em três grupos: robôs de mesa que mexem a cabeça, placas com tela para montar um assistente de voz, e robôs com rodas, câmera, microfone e alto-falante. Para cada um você vê o preço em dólar, o que vem na caixa, se funciona sozinho e qual IA ele usa. Os dados são de 14/11/2026: **nada foi comprado nem testado ainda**, e os preços mudam. É só ler; quem quiser tem um pequeno programa que filtra os kits pelo que você precisa.

## 📖 Guia

Guia completo (grupos, tabelas, preços e qual comprar): **https://inematds.github.io/robo-que-conversa/guia/**

## O que tem aqui

| Arquivo | Para quê |
|---|---|
| [FATOS.md](FATOS.md) | Cada número com fonte e data (fonte única do guia e do vídeo) |
| [dados/produtos.json](dados/produtos.json) | Os 9 kits: preço em US$, rodas, câmera, microfone, voz, tela, bateria, Wi-Fi, IA, link |
| [escolher.py](escolher.py) | Filtra os kits pelo que você precisa (só Python 3, sem instalar nada) |
| [test_escolher.py](test_escolher.py) | 8 testes do filtro |
| [guia/](guia/) | A página (PT, `en/`, `es/`) |

```bash
git clone https://github.com/inematds/robo-que-conversa.git
cd robo-que-conversa
python3 escolher.py --rodas --camera --ate 200   # PiCar-X e miniAuto Pro
python3 -m unittest test_escolher                # Ran 8 tests ... OK
```

## O processo, do início ao fim

| # | Passo | Comando | Quem |
|---|---|---|---|
| 1 | Pesquisar os anúncios e as fichas dos fabricantes | links do pedido + sites oficiais | 🧠 sessão com o Nei |
| 2 | Gravar cada número com fonte e data | `FATOS.md` | 🧠 |
| 3 | Atualizar os dados dos kits | `dados/produtos.json` | 🧠 |
| 4 | Testar o filtro | `python3 -m unittest test_escolher` | ⚙️ |
| 5 | Capa e banners (Codex) | `gerar-capa.cjs` e `gerar-banner.sh` (skill projetos-landing-guia) | ⚙️ |
| 6 | Guia PT e traduções EN/ES | `guia/index.html`, `guia/en/`, `guia/es/` | 🧠 + ⚙️ `inema-traduz` |
| 7 | Revisor independente | Agent novo pelo runbook `revisor-independente.md` | 🤖 |
| 8 | Publicar | `git push` (GitHub Pages pelo Actions) | ⚙️ |
| 9 | Vídeo explicativo 16:9 e 9:16 no lives6 | `~/projetos/explicavideos/textos/robo-que-conversa/roda.sh` | 🤖 `claude -p` |
| 10 | Vídeo no guia, portal e Telegram INEMA.ROBOT | vigia `continua` (fase 2) | 🤖 |

---
INEMA.CLUB · https://inema.club
