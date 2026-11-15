#!/usr/bin/env python3
"""Escolhe o kit de robô que conversa a partir do que você precisa.

Uso:
  python3 escolher.py                       # pergunta no terminal
  python3 escolher.py --rodas --camera --ate 200
  python3 escolher.py --tabela              # mostra todos

Lê dados/produtos.json (pesquisa de 14/11/2026, nada testado). Só biblioteca padrão.
"""
import argparse
import json
import sys
from pathlib import Path

DADOS = Path(__file__).resolve().parent / "dados" / "produtos.json"


def carregar(caminho=DADOS):
    return json.loads(Path(caminho).read_text(encoding="utf-8"))["produtos"]


def filtrar(produtos, rodas=False, camera=False, mexe=False, pronto=False, ate=None):
    """Devolve os produtos que atendem tudo o que foi pedido, do mais barato ao mais caro.
    Só entra quem conversa sozinho (microfone + voz)."""
    saida = []
    for p in produtos:
        if not (p["microfone"] and p["voz"]):
            continue
        if rodas and not p["rodas"]:
            continue
        if camera and not p["camera"]:
            continue
        if mexe and not p["mexe"]:
            continue
        if pronto and not p["pronto"]:
            continue
        if ate is not None and p["usd"] > ate:
            continue
        saida.append(p)
    return sorted(saida, key=lambda p: p["usd"])


def sim(v):
    return "sim" if v else "não"


def mostrar(lista):
    if not lista:
        print("Nenhum kit atende tudo isso. Tire uma exigência ou aumente o orçamento.")
        return
    for i, p in enumerate(lista, 1):
        extra = f" · precisa: {p['precisa']}" if p.get("precisa") else ""
        print(f"{i}. {p['nome']} — {p['preco_txt']}")
        print(f"   rodas {sim(p['rodas'])} · câmera {sim(p['camera'])} · mexe {sim(p['mexe'])} · Wi-Fi {p['wifi']}{extra}")
        print(f"   IA: {p['ia']}")
        print(f"   {p['link']}")


def perguntar(texto):
    r = input(f"{texto} [s/N] ").strip().lower()
    return r in ("s", "sim", "y", "yes")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Qual kit de robô que conversa comprar")
    ap.add_argument("--rodas", action="store_true", help="precisa andar")
    ap.add_argument("--camera", action="store_true", help="precisa de câmera")
    ap.add_argument("--mexe", action="store_true", help="precisa se mexer (cabeça ou rodas)")
    ap.add_argument("--pronto", action="store_true", help="quer pronto, sem comprar peça à parte")
    ap.add_argument("--ate", type=float, help="orçamento máximo em US$")
    ap.add_argument("--tabela", action="store_true", help="mostra todos os kits")
    ap.add_argument("--dados", default=str(DADOS))
    a = ap.parse_args(argv)
    produtos = carregar(a.dados)
    if a.tabela:
        mostrar(sorted(produtos, key=lambda p: p["usd"]))
        return 0
    if not any([a.rodas, a.camera, a.mexe, a.pronto, a.ate]) and sys.stdin.isatty():
        a.rodas = perguntar("Precisa andar (rodas)?")
        a.camera = perguntar("Precisa de câmera?")
        a.mexe = a.rodas or perguntar("Precisa se mexer (virar a cabeça)?")
        a.pronto = perguntar("Quer pronto, sem comprar peça à parte?")
        v = input("Orçamento máximo em US$ (Enter = sem limite): ").strip()
        a.ate = float(v) if v else None
    mostrar(filtrar(produtos, a.rodas, a.camera, a.mexe, a.pronto, a.ate))
    return 0


if __name__ == "__main__":
    sys.exit(main())
