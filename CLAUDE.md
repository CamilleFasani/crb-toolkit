# CLAUDE.md — crb-toolkit

> A toolkit for capturing the beauty of reality – at least trying to.

## 1. Façon de travailler

1. **Langue** :
   - **en français** : les conversations, les docstrings, les commentaires, les documents de cadrage ;
   - **en anglais** : les noms de fonctions, de variables, de classes, de modules et de fichiers de code.
2. **Style** : méthodique, structuré, explicite. Sections numérotées, listes, tableaux. Aucune étape implicite.
3. **Challenger** : signaler les tensions, risques et alternatives plutôt que valider sans discussion.
4. **Décisions** : les choix appartiennent à l'autrice. Proposer une recommandation, puis attendre la validation avant de la noter comme décidée.
5. **Commits** : ne jamais commiter sans accord explicite.

## 2. Le projet

- Suite de trois outils en ligne de commande, en Python, dans un seul dépôt.
- Projet secondaire de **curriculhome** (site CV / manifeste personnel, dossier `/home/cpressense/curriculhome`) : les fichiers produits par ces outils seront utilisés par le site.

| Commande | Outil | Entrée | Sortie |
|---|---|---|---|
| `crb p2p` | P2P - From Photo to Palette | Photo | `palette.yaml` |
| `crb p2c` | P2C - From Palette to Canvas | Palette (+ photo selon le mode) | SVG impressionniste |
| `crb p2t` | P2T - From Photo to Texture | Photo | SVG de texture |

## 3. Documents de cadrage (à lire avant toute décision)

| Fichier | Contenu |
|---|---|
| `why.md` | Intention, essence du projet |
| `tech-spec.md` | Choix techniques, avec statuts **[Décidé]** / **[Piste]** / **[Ouvert]** / **[Écarté]** |
| `docs/p2p.md`, `docs/p2c.md`, `docs/p2t.md` | Spécification de chaque outil |
| `raw-ideas.md` | Idées en vrac, à trier puis intégrer ou supprimer |

Toute décision validée est reportée dans le bon fichier, avec le bon statut.

## 4. Stack et outillage

- Python 3.13, géré par **uv** (`uv sync`, `uv add`, `uv run`). Si `uv` est introuvable : `export PATH="$HOME/.local/bin:$PATH"`.
- **Typer** : ligne de commande (`src/crb_toolkit/cli.py`, commande `crb`).
- **pydantic** : validation du format `palette.yaml`, contrat entre P2P et P2C.
- **ruff** (lint + formatage), **mypy** (mode strict, plugin pydantic), **pytest**.

### Vérifications à lancer après chaque modification

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
uv run pytest
```

## 5. Structure

```
src/crb_toolkit/
├── cli.py      → commande crb et sous-commandes
├── common/     → code partagé : photo, EXIF, couleurs, SVG
├── p2p/
├── p2c/
└── p2t/
tests/
```

## 6. Règles non négociables

1. **Vie privée** : aucune métadonnée (EXIF, GPS) dans les fichiers produits. Ne jamais commiter de photo d'origine (le dossier `photos/` est ignoré par Git).
2. **Dépôt public** : aucune donnée personnelle (adresse, téléphone, e-mail) dans le code ni dans les docs.
3. **Reproductibilité** : même entrée + mêmes réglages (graine aléatoire fixe) = même sortie.
4. **Le format de `palette.yaml` est un contrat** : toute modification touche P2P et P2C dans le même commit, avec tests.

## 7. État d'avancement (au 2026-11-20)

### Fait
- Docs de cadrage (commit initial `2c572bf`, auteur corrigé : adresse dev).
- Projet initialisé avec uv, dépendances installées, config ruff / mypy / pytest.
- Commande `crb` avec trois sous-commandes vides (`p2p`, `p2c`, `p2t`).
- 2 tests (`tests/test_cli.py`). Lint, types et tests passent.
- Adresse e-mail : l'adresse dev de l'autrice est utilisée dans `pyproject.toml` et dans la config Git locale du dépôt (`git config --local user.email`). Jamais l'adresse perso.
- Typer passé en [Décidé].

### Pas encore fait
1. **Commit de l'initialisation** : en attente du feu vert de l'autrice.

### Prochaine étape
- Spécifier P2P en détail, en commençant par **le format de `palette.yaml`**.
