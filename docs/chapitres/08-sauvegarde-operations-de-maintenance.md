# Sauvegarde / Opérations de maintenance

<u>Recommandé :</u>

- Programmer une sauvegarde journalière de la base de données
  (structure, données et fichier d'index des données)

- Utiliser un logiciel de sauvegarde tiers pour sauvegarder sur un autre
  site physique le dossier contenant les fichiers de sauvegarde de 4D
  (.4BK et .4BL)

- Utiliser un logiciel de snapshot compatible avec Volume Shadow Copy
  Service sous Windows pour sauvegarder les fichiers en cours
  d'exécution (notamment pour sauvegarder la base de données 4D « à
  chaud »)

- Activer le fichier d'historique 4D (.journal)

- Activer la restitution et l'intégration automatique du journal
  lorsqu'une corruption de données est détectée par 4D à l'ouverture de
  la base

- Restituer automatiquement (par programmation) chaque nouvelle
  sauvegarde (.4BK) sur une autre machine et effectuer une vérification
  des données avec l'outil intégré dans 4D (Centre de Sécurité et de
  Maintenance / CSM)

- Programmer l'envoi automatique (par programmation) d'un mail pour
  donner à l'administrateur de la base de données des informations sur
  l'état de la nouvelle sauvegarde et le résultat de la vérification des
  données

- Programmer de temps en temps une opération de compactage du fichier de
  données avec le CSM (depuis la v13, il est possible de détecter la
  fragmentation d'une table 4D et donc d'agir en conséquence grâce à
  la commande « Lire fragmentation table »)

- Fermer la fenêtre d'administration après chaque utilisation

Depuis la version 4D v15 R4, nous avons optimisé de façon importante
l'algorithme de réindexation globale de la base de données. Tout le
processus a été revu, et l'opération peut s'effectuer désormais
jusqu'à deux fois plus rapidement.

*Note : Une réindexation globale est nécessaire, par exemple, après une
réparation de la base de données ou lorsque le fichier .4dindx a été
supprimé.*

Comme chaque enregistrement de chaque table indexée doit être chargé en
mémoire durant l'indexation, l'optimisation a visé à minimiser les
échanges entre le cache et le disque (swaps). L'opération est désormais
effectuée séquentiellement sur chaque table, ce qui réduit les besoins
en chargement et en déchargement d'enregistrements.

Idéalement, si le cache était assez grand pour contenir la totalité du
fichier de données et des index, le nouvel algorithme de réindexation
n'apporterait aucune amélioration. Cependant, la mémoire disponible sur
le serveur n'est généralement pas aussi grande. Si le cache est assez
grand pour contenir au moins les données et les index de la table la
plus volumineuse, alors le nouvel algorithme sera jusqu'à deux fois
plus rapide que le précédent.

Réaliser des sauvegardes régulières des données est important mais ne
permet pas, en cas d'incident, de récupérer les données saisies depuis
la dernière sauvegarde. Pour répondre à ce besoin, 4D dispose d'un outil
particulier : le fichier d'historique. Ce fichier permet d'assurer la
sécurité permanente des données de la base.

En outre, 4D travaille en permanence avec un cache de données situé en
mémoire. Toute modification effectuée sur les données de la base est
stockée provisoirement dans le cache avant d'être écrite sur le disque
dur. Ce principe permet d'accélérer le fonctionnement des applications ;
en effet, les accès mémoire sont bien plus rapides que les accès disque.
Si un incident survient sur la base avant que les données stockées dans
le cache aient pu être écrites sur le disque, vous devrez intégrer le
fichier d'historique courant afin de récupérer entièrement la base.

Si vous travaillez en environnement virtuel, utiliser Volume Shadow Copy
sous Windows Server afin de gérer correctement les requêtes de
snapshots.

En plus de la sauvegarde et du fichier d'historique de 4D, nous vous
invitons à planifier régulièrement des opérations de maintenance en
vérifiant et en compactant le fichier de données et d'index.

Une fois votre stratégie de sauvegarde mise en place, nous vous invitons
à envisager le pire (incendie, vol) et donc d'effectuer une copie
hebdomadaire de la base sur un support inerte dans un autre endroit
sécurisé.

Dans le cadre d'applications critiques, il est également possible de
mettre en place un système de sauvegarde par miroir logique, permettant
un redémarrage instantané en cas d'incident sur la base en
exploitation. Les deux machines communiquent par le réseau, la machine
en exploitation transmettant régulièrement à la machine miroir les
évolutions de la base par l'intermédiaire du fichier d'historique.

De cette façon, en cas d'incident sur la base en exploitation, vous
pouvez repartir de la base miroir pour reprendre très rapidement
l'exploitation sans aucune perte de données.

Les principes mis en œuvre sont les suivants :

- La base de données est installée sur le poste 4D Server principal
  (poste en exploitation) et une copie identique de la base est
  installée sur le poste 4D Server miroir.

- Un test au démarrage de l'application (par exemple la présence d'un
  fichier spécifique dans un sous-dossier de l'application 4D Server)
  permet de distinguer chaque version (en exploitation et en miroir) et
  donc d'exécuter les opérations appropriées.

- Sur le poste 4D Server en exploitation, le fichier d'historique est
  segmenté à intervalle régulier à l'aide de la commande « Nouveau
  fichier historique ». Aucune sauvegarde n'étant effectuée sur le
  serveur principal, la base de données est en permanence disponible en
  lecture/écriture.

- Chaque segment de fichier d'historique est envoyé sur le poste miroir,
  où il est intégré à la base miroir à l'aide de la commande « INTEGRER
  FICHIER HISTORIQUE ».

La mise en place de ce système nécessite la programmation de code
spécifique, notamment :

- un minuteur sur le serveur principal pour la gestion des cycles
  d'exécution de la commande « Nouveau fichier historique »,

- un système de transfert des segments de fichier d'historique entre le
  poste en exploitation et le poste miroir (utilisation de 4D Internet
  Commands pour un transfert via ftp ou messagerie, Web Services, etc.),

- un process sur le poste miroir destiné à superviser l'arrivée de
  nouveaux « segments » de fichier d'historique et à les intégrer via la
  commande « INTEGRER FICHIER HISTORIQUE »,

- un système de communication et de gestion d'erreurs entre le serveur
  principal et le serveur miroir.

*Attention : La sauvegarde par miroir logique est incompatible avec les
sauvegardes « standard » sur la base en exploitation car l'emploi
simultané de ces deux modes de sauvegarde entraîne la désynchronisation
de la base en exploitation et de la base miroir. Par conséquent, vous
devez veiller à ce qu'aucune sauvegarde, automatique ou manuelle, ne
soit effectuée sur la base en exploitation. En revanche, il est possible
de sauvegarder la base miroir.*

Depuis la version v14, il est possible d'activer le fichier
d'historique courant sur le poste miroir. Vous pouvez ainsi mettre en
place un « miroir de miroir », ou des serveurs miroirs en série. Cette
possibilité s'appuie sur la commande « INTEGRER FICHIER HISTORIQUE
MIROIR ».
