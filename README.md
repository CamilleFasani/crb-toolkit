# crb-toolkit

> A toolkit for capturing the beauty of reality – at least trying to.

Suite de trois outils en ligne de commande :

| Commande | Outil |
|---|---|
| `crb p2p` | **P2P - From Photo to Palette** : extrait une palette de couleurs d'une photo (YAML) |
| `crb p2c` | **P2C - From Palette to Canvas** : crée un tableau impressionniste (SVG) |
| `crb p2t` | **P2T - From Photo to Texture** : extrait une texture d'une photo (SVG) |

## Installation (développement)

```bash
uv sync
uv run crb --help
```

## Vérifications

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
uv run pytest
```
