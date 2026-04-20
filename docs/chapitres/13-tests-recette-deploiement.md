# Tests / Recette / Déploiement

Utiliser le mode projet de 4D pour enregistrer le code source de votre
application sous forme de fichier texte, autorisant l'usage d'un système
de gestion de versions.

Vous pourrez alors utiliser un système de contrôle des révisions (comme
Git) mais également un service d'hébergement pour le code source de
votre application 4D (comme GitHub).

Ne déployez pas votre base de données sans l'avoir testée au préalable
dans son futur environnement ou dans un environnement similaire
(matériel, version de 4D identique, etc.) et surtout dans ses futures
conditions d'utilisation (avec le même nombre d'utilisateurs
simultanés en utilisant des scénarios de tests Utilisateur).

Stresser sa base de données pour en connaître les limites, non
détectables par l'équipe de développement, vous épargnera bien des
soucis en Production et permettra d'optimiser les fonctionnalités les
plus utilisées.

Les tests et la recette sont les clés d'un déploiement réussi !
