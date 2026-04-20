# Recommandations générales

[Recommandé :]{.underline}

- Utiliser une gamme supportée
  (<https://fr.4d.com/cycle-de-vie-produits>), au choix :

  - La gamme Feature Release : 20 Rx

  - La gamme Long Term Support Release : 20.x

- Déployer la version la plus récente de la gamme que vous aurez choisie
  (<https://fr.4d.com/product-download/>) :

  - Gamme Feature Release :

    - Une nouvelle version R est disponible tous les 3 mois contenant de
      nouvelles fonctionnalités

    - 2 HotFix sont disponibles mensuellement pour la version R courante
      contenant des corrections de bugs empêchant son utilisation en
      déploiement (il faudra attendre la version R suivante pour les
      autres bugs)

  - Gamme LTS Release :

    - Une nouvelle version majeure est disponible tous les 18 mois
      contenant les fonctionnalités des 6 versions R antérieures à sa
      sortie

    - Des versions mineures et des HotFix sont disponibles régulièrement
      pour la version LTS majeure courante contenant des corrections de
      bugs

<!-- -->

- Vous pouvez utiliser la gamme Feature Release en développement afin de
  bénéficier des implémentations importantes offertes par 4D au plus tôt

- Développer en mode projet

- Utiliser des outils de dépôt et de contrôle de source pour le
  développement collaboratif mais aussi pour gérer vos différentes
  branches de développement et de déploiement

- Utiliser des champs UUID pour les clés primaires

- Dessiner les liens entre les tables et nommer vos liens

- Ne pas utiliser la commande « MODIFER SELECTION »

- Utiliser les objets

- Utiliser des listbox pour les listes

- Utiliser exclusivement des noms d'objets
