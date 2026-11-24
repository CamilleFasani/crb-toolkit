# P2P - From Photo to Palette

## 1. Rôle
Extraire d'une photo une palette de couleurs, au format YAML.

## 2. Entrée
- Une photo (formats : _à définir_).

## 3. Sortie
- Fichier de palette `.yaml` (format : voir section 5).

## 4. Sélection des couleurs
- **[Décidé]** v1 : sélection 100 % manuelle. L'autrice choisit elle-même chaque couleur sur la photo (cf. `why.md`, intention 2 : « l'outil exécute, je règle »).
- **[Décidé]** Interface : `crb p2p` ouvre la photo dans une fenêtre matplotlib ; l'autrice y trace des rectangles à la souris, un par couleur.
- **[Décidé]** Entre 2 et 8 couleurs par palette.
- **[Décidé]** Couleur d'un rectangle = médiane de ses pixels, canal par canal (robuste aux pixels qui débordent sur une autre couleur, contrairement à la moyenne).
- **[Décidé]** Coordonnées des rectangles en pixels, sur la photo redressée (orientation EXIF appliquée avant suppression des métadonnées, ex. `ImageOps.exif_transpose` de Pillow). Origine en haut à gauche, x vers la droite, y vers le bas.
- **[Écarté]** Poids de chaque couleur (part de la photo) calculé par P2P. Les proportions des couleurs seront un réglage de P2C.
- **[Piste]** Plus tard : suggestion automatique d'une palette par k-means (dans l'espace OKLab), à ajuster ensuite à la main. Repoussé : inutile tant que la sélection est manuelle.
- **[Piste]** Plus tard, avec k-means : pondération par la saturation (éviter que les couleurs vives mais rares disparaissent).
- **[Décidé]** Champ « histoire » : P2P écrit `story: ""`, l'autrice le remplit ensuite à la main en éditant le YAML.
- **[Piste]** Plus tard, si besoin : saisie de l'histoire dans le terminal, après la fenêtre de sélection.
- **[Décidé]** Ne pas écraser un fichier de palette existant (pour ne pas perdre les histoires), sauf avec l'option `--force`. Vérification faite avant d'ouvrir la fenêtre (échouer tôt) ; en cas de refus, message clair et code de sortie 1.

## 5. Format de `palette.yaml`
- **[Décidé]** Format v1 :
  ```yaml
  version: 1                      # version du format (le contrat P2P → P2C), entier
  story: ""                       # histoire de la palette entière, remplie à la main
  colors:                         # 2 à 8 couleurs, dans l'ordre de sélection
    - hex: "#C8321E"              # couleur sRGB : « # » + 6 caractères hexadécimaux, en majuscules
      region: [1240, 820, 20, 20] # rectangle source : x, y (≥ 0), largeur, hauteur (> 0), en pixels
      story: "Le coquelicot du bord du chemin."  # histoire de la couleur, remplie à la main
  ```
- **[Décidé]** Pas de nom de photo source dans le fichier (un nom de fichier peut révéler un lieu ou une personne ; palettes publiées sur le site). Principe de minimisation des données.
- **[Piste]** Nom du fichier de sortie choisi par l'autrice (ex. `--output coquelicots.yaml`).
- **[Décidé]** Extension `.yaml` (et non `.yml`), partout.
- **[Décidé]** Ordre des couleurs : ordre de sélection (choix artistique, repère pour remplir les histoires). Réordonnables à la main dans le YAML. Un éventuel tri d'affichage relève du site, pas du fichier.
