# Processeur

<u>Recommandé :</u>

- pour les postes de travail : 1 CPU avec 2 cœurs minimum

- pour les serveurs : 1 CPU avec 4 cœurs minimum (plutôt que 2 CPU avec
  2 cœurs car la mémoire cache sera partagée entre tous les cœurs)

- déployer votre application en compilé afin de bénéficier du mode
  préemptif (\*) pour tirer intégralement parti des machines multi-cœurs

- déclarer explicitement toutes les méthodes que vous souhaitez démarrer
  en mode préemptif (cocher l'option dans les propriétés de vos
  méthodes et vérifier leur éligibilité grâce au compilateur)

4D tire parti à travers le système des multiples cœurs disponibles
(\*\*). En effet, le système d'exploitation répartit le « temps
processeur » (total du temps de tous les cœurs) entre chaque application
et entre les threads de chaque application. C'est ensuite l'application
qui définit les priorités de chacun de ses threads, chaque thread
travaillant individuellement.

*\* : si vous déployez votre application en interprétée, tous les
process s'exécuteront sur un seul cœur, quelque soit le nombre de cœurs
disponibles sur votre machine !*

*\*\* : Les systèmes supportant le multithreading permettent de simuler
2 cœurs logiques pour chaque cœur, multipliant ainsi par deux la
capacité de traitement de 4D Server.*

Dans 4D, il existe des threads coopératifs et des threads préemptifs. 4D
les utilise automatiquement (pas de logiciel ou de préférence
spécifique) en fonction du code 4D exécuté.

Tous les threads coopératifs fonctionnent dans le thread principal à la
différence des threads préemptifs qui sont dispatchés par le serveur 4D
sur les autres threads. En effet, lorsqu'il est exécuté en mode
préemptif, un process est dédié à un CPU (processeur). La gestion du
process est alors déléguée au système, qui peut allouer chaque CPU
séparément sur une machine multi-cœurs.

Lorsqu'ils sont exécutés en mode coopératif (seul mode disponible dans
4D jusqu'à 4D v15 R5), tous les process sont gérés par le thread
(process système) de l'application parente et partagent le même CPU,
même sur une machine multi-cœurs.

Par conséquent, en mode préemptif, les performances globales de
l'application sont améliorées, particulièrement avec des machines
multi-cœurs, car de multiples threads peuvent véritablement être
exécutés simultanément. Les gains effectifs dépendent cependant de la
nature des opérations exécutées. Fondamentalement, le code destiné à
être exécuté dans des threads préemptifs ne peut pas appeler d'éléments
ayant des interactions extérieures telles que du code de plug-in ou des
variables interprocess. L'accès aux données, cependant, est possible
car le serveur de données de 4D prend en charge l'exécution en mode
préemptif.

En contrepartie, puisqu'en mode préemptif chaque thread est indépendant
des autres et non géré directement par l'application, des conditions
spécifiques sont à respecter dans les méthodes qui doivent être
exécutées en préemptif. De plus, le mode préemptif est disponible
uniquement dans certains contextes.

*Notes :*

- *Le type de process « Worker » vous permet d'échanger des données
  entre n'importe quel process, y compris des process préemptifs.*

- *La commande « APPELER FORMULAIRE » fournit une solution élégante
  permettant d'appeler des objets d'interface depuis un process
  préemptif.*

- *Bien qu'elles aient été conçues principalement pour les besoins liés
  à la communication interprocess dans le contexte des process
  préemptifs (accessibles en version 64 bits uniquement), les commandes
  « APPELER WORKER » et « APPELER FORMULAIRE » sont disponibles dans les
  versions 32 bits et peuvent être utilisées avec des process en mode
  coopératif.*

Il faut savoir aussi qu'un process non local de 4D Distant communique
toujours avec deux threads jumeaux sur le serveur : un thread préemptif
pour les requêtes DB4D (créer, stocker, charger, supprimer, trier,
chercher, etc.) et un thread coopératif pour les requêtes applicatives
(date du jour(\*), lire variable process (-1;..), etc.). Un troisième
thread préemptif peut aussi être créé si vous exécutez des commandes SQL
(à l'appel à la commande « Debut SQL »).

En fonction de la commande exécutée, 4D utilise tel ou tel thread en
établissant la communication sur le port correspondant :

- port de publication pour les requêtes vers la base de données (thread
  coopératif)

- port applicatif (port de publication +1) pour les requêtes
  applicatives (thread préemptif)

- port SQL pour les requêtes SQL (thread préemptif)

En conclusion, vous devez utiliser un processeur multi-cœurs même si
l'utilisation de tous les cœurs dépendra des commandes 4D utilisées
dans votre application en sachant que plus vous êtes préemptif, plus
vous serez rapide sur une machine multi-cœurs.
