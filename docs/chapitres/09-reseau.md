# Réseau

[Recommandé :]{.underline}

- Utiliser l\'ancienne couche réseau jusqu\'à la version v15 R5

- Utiliser la nouvelle couche réseau à partir de la version 16.2
  publique

*Attention : l\'ancienne couche réseau n\'est pas disponible dans les
versions 64 bits de 4D Developer (Windows et Mac) et dans la version 64
bits de 4D Server (Mac uniquement).*

Il est très important pour 4D Server d\'avoir en permanence suffisamment
de bande passante pour communiquer avec ses postes distants. Si vous
mutualisez la bande passante, il faudra en réserver une partie pour 4D
Server.

En effet, lorsque la bande passante vient à manquer, certains paquets
sont perdus et cela provoque inévitablement des erreurs côté Serveur. Si
trop d\'erreurs réseau surviennent au même moment ou de façon trop
fréquence, vous déstabilisez 4D Server.

Sachez également que, si vous utilisez le serveur Web de 4D et que vous
désirez séparer le trafic pour des raisons de sécurité et/ou de
performances, il est possible de dédier une carte réseau aux
utilisateurs de 4D Distant et une autre aux requêtes Web, SOAP ou REST.
