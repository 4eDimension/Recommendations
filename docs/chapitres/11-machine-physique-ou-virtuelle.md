# Machine physique ou virtuelle

<u>Recommandé :</u> machine physique dédiée par application 4D

Nous recommandons de déployer une application 4D par machine virtuelle
ou physique.

Même si 4D fonctionne en environnement virtuel (on-premise ou dans le
Cloud) et est donc éligible en terme d'exploitabilité, côté
performances notre expérience nous montre qu'une machine physique offre
de meilleures performances dans le temps à ressources équivalentes.

S'il ne vous est pas imposé de virtualiser le serveur 4D en production,
nous vous conseillons dans un premier temps de le déployer sur une
machine physique. Puis dans un second temps, de programmer des tests
poussés en environnement virtuel. Vous aurez ainsi l'avantage de pouvoir
comparer les 2 solutions.

Toutefois, si l'on peut trouver un avantage à la virtualisation c'est la
souplesse d'allocation des ressources (CPU, mémoire notamment). Il est
possible d'allouer des ressources supplémentaires par la suite, voir
même d'allouer des ressources en temps réel, en fonction de l'activité
de la machine. Nous avons d'ailleurs un certain nombre de clients qui
travaillent avec des environnements virtualisés, de plus en plus
d'ailleurs. Nous avons même des clients qui déploient des serveurs RDS
virtualisés sur des serveurs lames.

Nous n'avons cependant pas de documents officiels certifiant le
fonctionnement de 4D en environnement virtuel ou privilégiant une
solution plutôt qu'une autre.

Nous préconisons uniquement de s'assurer que les performances de la
machine soient suffisantes en termes de ressources (mémoire, processeur,
etc.) ou que le système d'exploitation virtualisé soit certifié avec la
version de 4D installée.

De manière générale les ressources CPU et RAM doivent être un peu plus
importantes en environnement virtualisé par rapport à une solution non
virtualisée.

De plus les performances observées dépendent grandement du paramétrage
de la machine virtuelle (CPU, mémoire, etc. mais aussi du disque dur et
de la carte réseau (caractéristiques, est-elle partagée, dédiée,
correctement configurée, etc.)), de la solution utilisée, de la version
de la solution et du système sur lequel est installé la solution. Pour
cette partie je vous invite à consulter les sites et forums des éditeurs
de solutions virtualisées ainsi que les études comparatives.
