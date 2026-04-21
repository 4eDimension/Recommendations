# Serveur Web

4D dispose de son propre serveur HTTP, un puissant serveur multithread
pour les contenus statiques et dynamiques. L'intégration étroite a un
impact considérable sur la sécurité accrue.

Sans compter une meilleure sécurité du code (voir ci-dessous), ce
concept supprime le problème de mise à jour typique oublié. Comme tout
est intégré, il n'y a qu'un seul logiciel à mettre à jour. Les
solutions habituelles nécessitent une énorme quantité de logiciels à
maintenir à jour : PHP, OpenSSL, Apache, NodeJS, etc. Tous ont besoin de
mises à jour régulières et il est commun que certaines parties restent
non patchées pendant longtemps, en particulier si elles sont utilisées
comme solution de service, sans une équipe informatique spécialisée.

Les requêtes web déclenchent du code 4D, qui répondent à la demande au
niveau applicatif, pas seulement au niveau de la base de données.
L'intégration étroite permet de contrôler toutes les requêtes,
utilisant la construction d'autorisations et d'implémentations sur
mesure, bien sûr cryptées TLS.

Le serveur intégré HTTP permet également des justifications de contrôle
fin, par exemple pour un serveur REST.

Depuis la version 4D v16 R6, 4D prend désormais en charge Perfect
Forward Secrecy (PFS). Cela vous donne le niveau de sécurité le plus
élevé pour vos communications, par défaut ! Au-delà de la protection
qu'il offre, le soutien de PFS augmente également les résultats des
tests de vérification SSL, ce qui est excellent pour nos clients. En
particulier, ceux qui travaillent avec des informations sensibles.

Le niveau de sécurité par défaut du serveur Web de 4D a été augmenté
pour être conforme à certaines fonctions de sécurité réseau (Sécurité
App Transport (ATS) sur iOS, par exemple), et permet d'obtenir de
meilleurs résultats lors des tests de vérification de sécurité Web (par
exemple : SSL Labs).

Pour ce faire, nous avons :

- activé « Perfect Forward Secrecy », et

- désactivé l'algorithme RC4 de la liste de chiffrement.

Par conséquent, le serveur Web 4D obtient un « A » dans le classement de
SSL Labs, sans qu'aucune action ne soit nécessaire !

Perfect Forward Secrecy (PFS) est un algorithme d'échange de clés. Il
utilise les algorithmes Diffie-Hellman (DH) pour générer des clés de
session de telle sorte que seules les deux parties impliquées dans la
communication peuvent les obtenir.

4D active automatiquement PFS lorsque TLS est activé sur le serveur.
Pour cela, 4D génère un fichier « dhparams.pem » - s'il n'existe pas
déjà - qui contient la clé privée de votre serveur DH. Si vous utilisez
la liste de chiffrement standard de 4D, PFS est prêt à l'emploi. Si
vous préférez utiliser une liste de chiffrement personnalisé, vérifiez
qu'il contient des entrées avec des algorithmes de ECDH ou DH.

Pour savoir si PFS est activé sur votre serveur Web, exécutez la
commande « WEB Lire infos serveur » avec le nouvel attribut
« perfectForwardSecrecy ». Cela permet de vérifier si toutes les
conditions nécessaires pour utiliser PFS sont remplies :

- TLS est activé

- La liste de chiffrement contient au moins un algorithme ECDH ou DH

- Le fichier « Dhparams.pem » est présent et valide

- Tous les certificats SSL / TLS sont présents

L'algorithme RC4 a connu des problèmes de sécurité et est maintenant
déprécié dans le serveur Web de 4D. Tous les chiffrements RC4 ont été
retirés de la liste de chiffrement par défaut et le modèle « RC4 » a été
ajouté à la liste de chiffrement pour l'interdire explicitement.
