# Spécifications techniques — crb-toolkit

Légende : **[Décidé]** · **[Piste]** · **[Ouvert]** · **[Écarté]**

## 1. Structure
- **[Décidé]** Un seul dépôt pour les trois outils.
- **[Décidé]** Nom du dépôt et du dossier : `crb-toolkit` (tiret). Nom du package Python : `crb_toolkit` (underscore).
- **[Décidé]** Une seule commande `crb` avec sous-commandes : `crb p2p`, `crb p2c`, `crb p2t`.
- **[Décidé]** Terme « photo » (et non « picture »). Noms complets dans les README : « P2P - From Photo to Palette », « P2C - From Palette to Canvas », « P2T - From Photo to Texture ».
- **[Piste]** Arborescence :
  ```
  crb-toolkit/
  ├── pyproject.toml
  ├── README.md
  ├── docs/            → spécification de chaque outil
  ├── src/crb_toolkit/
  │   ├── common/      → photo, EXIF, couleurs, SVG
  │   ├── p2p/
  │   ├── p2c/
  │   └── p2t/
  └── tests/
  ```

## 2. Outillage
- **[Décidé]** ruff (lint + formatage).
- **[Décidé]** pytest (tests).
- **[Décidé]** uv (gestion de Python, des dépendances, de l'environnement).
- **[Décidé]** mypy en mode strict (assouplissement ciblé possible sur numpy).
- **[Décidé]** Typer pour la ligne de commande (basé sur les annotations de type ; préféré à argparse, plus verbeux).
- **[Décidé]** Python 3.13.
- **[Décidé]** pydantic pour valider le format de `palette.yaml` (contrat entre P2P et P2C).
- **[Décidé]** matplotlib pour l'interface de sélection des couleurs de P2P (fenêtre avec rectangles tracés à la souris). Affichage sous WSL2 via WSLg (présent).
- **[Piste]** Plus tard : k-means (scikit-learn ou numpy « fait main ») pour suggérer une palette. Pas en v1.

## 3. Contrat partagé
- **[Décidé]** Le format de `palette.yaml` est le contrat entre P2P et P2C. Toute modification est faite dans un seul commit, avec tests.

## 4. Vie privée
- **[Décidé]** Suppression des métadonnées de toute image traitée ou produite.
