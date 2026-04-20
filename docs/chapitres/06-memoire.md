# Mémoire

[Recommandé :]{.underline}

- pour les postes de travail : 8 Go minimum

- pour les serveurs : 16 Go minimum (selon le nombre d\'enregistrements
  et d\'utilisateurs connectés, plus de mémoire peut être nécessaire)

- ECC (technologie de correction d\'erreurs)

La mémoire allouée à l\'application 4D Server dépend de 4 facteurs :

- la quantité de mémoire totale sur votre machine,

- la quantité de mémoire disponible,

- du système d\'exploitation,

- de la version de 4D Server utilisée.

Pour information, il n\'est pas possible d\'avoir un cache inférieur ou
égal à 100 Mo. De toute façon le cache est très important, il faut donc
réserver une quantité de mémoire suffisante (après calcul de la mémoire
nécessaire pour les process, etc.) au cache de 4D.

- L\'espace mémoire réservé au cache est séparé de l'espace mémoire
  utilisé par le serveur pour les process. Effectivement le fait
  d\'augmenter la taille du cache diminue l\'espace réservé aux process.

- La taille maximale varie en fonction du nombre d\'utilisateurs
  connectés et du nombre de process par utilisateur. Cependant 1 Go
  environ est par défaut utilisé par 4D (en dehors des process),
  notamment pour charger toutes les librairies systèmes.

- La gestion du cache a été améliorée. En particulier, un nouveau
  mécanisme effectue les opérations les plus consommatrices dans la
  mémoire temporaire, ce qui permet d'alléger le cache principal. La
  mémoire temporaire a pour avantage de n'être utilisée qu'en cas de
  besoin et ne mobilise pas les ressources de la machine. Nous vous
  invitons à calculer la mémoire nécessaire au bon fonctionnement de 4D
  Server, et ensuite de la déduire de la mémoire totale allouée par le
  système à 4D. Vous pourrez ainsi en déduire la taille de cache
  maximale que vous pouvez allouer. Une taille de cache excessive risque
  d'ailleurs de diminuer les performances générales du système, voire de
  le rendre instable.

- Pour connaître le taux de réussite il faut observer les variations de
  la mémoire cache observée. Lorsque vous observez une diminution du
  cache utilisé, cela signifie que 4D a eu besoin de supprimer des
  objets afin de libérer de la mémoire pour certains objets du moteur de
  données. Si le cache est purgé encore et encore, c\'est une bonne
  analyse qui indique que le cache est trop petit. Dans ce cas, 4D a
  besoin de purger de manière répétée un quart de son cache dans le but
  de libérer assez de place pour les objets du moteur de données.

- La gestion du cache doit être laissé aux soins de 4D, seules la taille
  du cache et la fréquence d\'écriture du cache sont importantes
  désormais. Nous vous conseillons de ne pas utiliser la commande
  « ECRIRE CACHE » par exemple, il est préférable d\'utiliser l\'option
  « Ecriture cache toutes les 20 secondes », qui spécifie les
  intervalles de sauvegarde des données, afin de contrôler l\'écriture
  du cache de données sur le disque. 4D utilise en interne un système
  intégré de cache de données permettant d\'accélérer les opérations
  d\'Entrée/Sortie. Le fait que des modifications de données soient, par
  moment, présentes dans le cache de données et pas sur le disque, est
  entièrement transparent pour votre code. Par exemple, si vous appelez
  la commande « CHERCHER », le moteur de 4D va intégrer les données
  présentes dans le cache pour effectuer l\'opération.

Nous vous conseillons :

- de ne pas cocher l'option « Calcul du cache adaptatif » afin de fixer
  une taille de cache fixe ;

- de décocher, sous Mac, l\'option « Maintenir le cache en mémoire
  physique » ;

- prévoir suffisamment de mémoire dans la machine pour le cache, la
  mémoire moteur de 4D Server et le système d\'exploitation lui-même ;

- de fixer la fréquence d\'écriture du cache à 20 secondes ;

- supprimer les appels à la commande « ECRIRE CACHE » dans votre code ;

- déployer la version 64 bits de 4D Server (une application 32 bits ne
  peut pas utiliser plus de 4 Go de mémoire, une application 64 bits
  dispose quant à elle de 8 To d\'espace adressable théorique !) ;

- déterminer la valeur idéale du cache pour votre base en production en
  utilisant le composant « 4D_Info_Report »
  (<https://taow.4d.com/Outil-4D-Info-Report/PS.1938271.fr.html>).

(Prévoir des slots de libre si le fichier de données est amené à grossir
rapidement pour rajouter de la mémoire par la suite)

Le gestionnaire du cache de la base de données a été entièrement réécrit
en 4D v16 et améliore ainsi l\'utilisation d\'un cache très important
pour les ordinateurs modernes (avec 64 ou même 128 Go de cache)
permettant de profiter des faibles prix des barrettes mémoire et
permettant ainsi de stocker une base de données de grande taille
entièrement en mémoire. Il améliore également les situations où le cache
est de petite taille alors que le fichier de données est très volumineux
grâce à une meilleure gestion des priorités pour les objets de données à
contenir ou à libérer du cache.

En conséquence, la base de données sera plus rapide, permettant de gérer
plus de données et plus d\'accès utilisateurs simultanés.

Enfin, 4D utilise en interne un système intégré de cache de données
permettant d\'accélérer les opérations d\'E/S. Le fait que des
modifications de données soient, par moments, présentes dans le cache de
données et pas sur le disque est entièrement transparent pour votre
code. Par exemple, si vous appelez la commande CHERCHER, le moteur de 4D
va intégrer les données présentes dans le cache pour effectuer
l\'opération.

Automatiquement disponible et optimisé, il peut cependant être configuré
ou analysé dynamiquement avec les commandes suivantes :

- La commande « ECRIRE CACHE » accepte désormais un paramètre \* pour
  vider le cache ou un nombre d\'octets minimum de libération du cache
  (uniquement pour effectuer des tests)

- La commande « FIXER TAILLE CACHE » fixe dynamiquement la taille du
  cache de la base de données dans les versions 64 bits de 4D

- La commande « Lire informations cache » récupère des informations
  relatives à l'utilisation du cache en 64 bits

- La commande « Lire taille cache » retourne la taille courante du cache

- Le sélecteur « Périodicité écriture cache » de la commande « FIXER
  PARAMETRE BASE » permet de lire ou de fixer la périodicité de
  l\'écriture du cache sur le disque

Le cache des données de la base inclut un mécanisme de gestion
automatique des priorités offrant un haut niveau d\'efficacité et de
performance. Ce mécanisme permet d\'optimiser la rotation des données
dans le cache lorsque le programme a besoin de place : les données de
plus faible priorité sont déchargées en premier, tandis que les données
de priorité plus haute restent chargées.

Ce mécanisme est entièrement automatique et la plupart du temps, vous
n\'aurez pas besoin de vous en préoccuper. Cependant, pour des cas
particuliers, il peut être personnalisé à l\'aide d\'un ensemble de
commandes dédiées, vous permettant de changer la priorité des objets
pour toute la session ou uniquement le process courant. A noter que ces
commandes doivent être utilisées avec précaution car elles peuvent
affecter les performances de la base.

Le gestionnaire du cache sélectionne les données à retirer du cache en
cas de besoin à l\'aide d\'un système de priorité.

Les trois types d\'objets qui peuvent être chargés dans le cache ont une
priorité différente :

- tables : toutes les données standard des champs (numériques,
  dates\...), à l\'exclusion des blobs (voir ci-dessous). Priorité par
  défaut : moyenne

- blobs : toutes les données binaires des champs (textes, images, objets
  et blob) stockées dans le fichier de données. Priorité par défaut :
  faible

- index : tous les index de champs simples, y compris les index de
  mots-clés et les index composites. Comme les index sont utilisés très
  fréquemment, ils ont un statut spécial dans le cache. Priorité par
  défaut : élevée

Les priorités par défaut assurent généralement des performances
optimales. Cependant, dans certains cas spécifiques, vous pouvez avoir
besoin de personnaliser ces priorités. Pour cela, vous disposez de deux
ensembles de commandes 4D :

- Les commandes qui modifient les priorités du cache pour l\'ensemble de
  la session et tous les process : « FIXER PRIORITE CACHE TABLE »,
  « FIXER PRIORITE CACHE INDEX » et « FIXER PRIORITE CACHE BLOBS ». Ces
  commandes doivent être appelées au démarrage de la base.

- Les commandes qui modifient les priorités du cache pour le process
  courant uniquement : « AJUSTER PRIORITE CACHE TABLE », « AJUSTER
  PRIORITE CACHE INDEX » et « AJUSTER PRIORITE CACHE BLOBS ». Utilisez
  ces commandes si vous souhaitez changer temporairement la priorité des
  objets dans le cache afin d\'améliorer les performances lors d\'une
  opération temporaire, puis revenir aux priorités initiales.
