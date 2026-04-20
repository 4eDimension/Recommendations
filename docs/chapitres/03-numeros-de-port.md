# Numéros de port

[Recommandé :]{.underline} s\'assurer que les ports ci-dessous soient
disponibles et dédiés à l\'application 4D Server

- ports obligatoires :

  - TCP 19813 : port de publication client/serveur & serveur
    d\'application (modifiable dans les propriétés de la base)

  - TCP 19814 : port applicatif & serveur de base de données (non
    modifiable : port de publication +1)

- ports facultatifs :

  - TCP 19812 : port pour le serveur SQL (modifiable dans les propriétés
    de la base)

  - UDP 19813 : port pour le broadcast (non modifiable, n\'est utilisé
    que si le port de publication est égal à sa valeur par défaut :
    19813)

  - TCP 19815 : port du débogage distant du serveur (non modifiable :
    port de publication +2)

  - TCP 80 et TCP 443 : ports pour le serveur Web, utilisés pour les
    requêtes HTTP, HTTPS, SOAP ou REST (modifiables dans les propriétés
    de la base)

  - TCP 8002 : port pour l\'interpréteur PHP (modifiable dans les
    propriétés de la base)

  - d\'autres ports peuvent également être utilisés par 4D, notamment
    par le plugin 4D Internet Commands

Vous pouvez modifier les ports utilisés par 4D, par défaut. Cependant
attention certains ports sont utilisés ou réservés pour d\'autres
applications :

- 0 à 1023 (Ports réservés) : Ces ports sont affectés par l\'I.A.N.A.
  (Internet Assigned Numbers Authority) et sur la plupart des systèmes
  ne peuvent être utilisés que par des process système (ou racine) ou
  par des programmes exécutés par des utilisateurs disposant de
  privilèges d\'accès avancés.

  - 20 et 21 FTP;

  - 23 TELNET;

  - 25 SMTP;

  - 37 NTP;

  - 80 et 8080 HTTP;

  - 443 HTTPS.

- 1024 à 49151 (Ports enregistrés) : Ces ports sont enregistrés par
  l\'I.A.N.A. et peuvent être utilisés sur la plupart des systèmes par
  des process utilisateurs ou par des programmes exécutés par des
  utilisateurs sans privilèges particuliers (routeurs, applications
  spécifiques\...)

- 49152 à 65535 (Ports dynamiques et/ou privés) : Ces ports sont
  d\'utilisation libre.

Les personnes souhaitant utiliser les commandes TCP/IP pour synchroniser
des bases de données doivent utiliser des numéros de port supérieurs à
49151.

Pour de plus amples informations, veuillez visiter le site Web de
l\'I.A.N.A. : <http://www.iana.org/>

Pour activer ou mettre à jour une licence depuis l'application 4D ou 4D
Server, vous devez également autoriser l\'ordinateur à communiquer avec
les URLs suivantes (port 443) :

- <https://autoregistration.4d.fr/>

- <https://autoregistration.4d.com/>

- <https://motor.4d.fr/>

- <https://motor.4d.com/>
