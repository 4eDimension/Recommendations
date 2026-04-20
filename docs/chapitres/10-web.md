# Web

<u>Recommandé :</u>

- utiliser une version 64 bits de 4D

- utiliser le serveur web de 4D Server (le mode préemptif n'est pas
  pris en charge par 4D en mode distant)

- déployer une application 4D compilée

- s'assurer que les méthodes bases et les méthodes projets relatives au
  Web soient confirmées thread-safe par 4D Compiler

- utiliser un reverse proxy (exemple : Nginx) pour ne pas exposer le
  serveur 4D sur Internet

Depuis la version v16, le serveur Web intégré de 4D (en 64 bits
uniquement) pour Windows et pour Mac OS X permet de tirer pleinement
parti du multi-cœur en utilisant des process Web préemptifs dans les
applications compilées. La plupart des commandes de 4D liées au Web, les
méthodes et les URL de la base de données sont thread-safe et peuvent
être utilisées en mode préemptif. Vous pouvez configurer votre code lié
au Web, y compris les balises HTML 4D et les méthodes base Web, afin
qu'il s'exécute simultanément sur le plus grand nombre de cœurs
possibles.

Si vous souhaitez rendre une application 4D full web hautement
disponible, voici l'architecture que nous vous conseillons :

- Front-End :

  - Mettre en place un load balancer (exemple : Nginx) et utiliser une
    IP élastique pour rediriger les requêtes web vers la VM de son choix

  - Disposer d'une page de maintenance à afficher lorsque la production
    est interrompue

- Back-End :

  - Mettre en place une VM avec son disque système et 3 disques attachés
    supplémentaires, dont 2 SSD (qui peuvent ainsi être détachés et
    rattachés à une autre VM, à la demande)

    - disque 1 : contient le système et les applications

    - disque 2 : contient les sources de l'application 4D connectées à
      un serveur de sources (exemple : Gitlab) -- permet de faciliter
      l'intégration, le déploiement et le suivi des mises à jour du code
      sur les différentes serveurs (test, recette et production)

    - disque 3 : contient la base de données (disque SSD)

    - disque 4 : contient les sauvegardes 4D et son fichier
      d'historique courant (disque SSD) -- permet d'automatiser la
      restitution automatique des sauvegardes sur une autre VM pour
      vérifier les données régulièrement et s'assurer qu'elles sont
      saines

  - Sauvegarder les sessions pour ne pas perdre les contextes web
    (stockés en mémoire) des utilisateurs connectés, 2 solutions (au
    choix) sont envisageables pour cela :

    - Côté client : Utiliser JSON Web Token (JWT) pour sauvegarder les
      sessions dans le navigateur

    - Côté serveur : Sauvegarder les sessions dans la base de données 4D

Lorsque vous prévoyez de faire une mise à jour système ou applicative,
voici la procédure à suivre :

- Cloner la VM de Production avec son disque système (le disque 1) :
  cette VM devient la VM de recette

- Procéder aux opérations de maintenance (mise à jour système ou mise à
  jour applicative) sur cette VM de recette

- Exécuter vos tests pour vous assurer que ces opérations n'ont aucun
  impact sur le fonctionnement de l'application 4D

- Une fois la phase de validation achevée et qu'aucune régression n'a
  été constatée, cloner la VM de recette avec son disque système (disque
  1)

- Sauvegarder les sessions web et demander à NGINX d'afficher une page
  de maintenance

- Arrêter la VM de production et détacher les disques 2, 3 et 4

- Démarrer le clone de la VM de recette, qui devient la VM de
  production, et y attacher les disques 2, 3 et 4

- Restaurer les sessions web et désactiver la page de maintenance

- La base de production est de nouveau opérationnelle

Bien sûr toutes ces opérations d'interruption de la production (lignes 5
à 8) sont automatisables pour n'interrompre la production que quelques
secondes seulement et qu'à l'issue les utilisateurs conservent leur
contexte d'utilisation.
