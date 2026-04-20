# Surveillance du serveur

Vous pouvez utiliser le composant « 4D_Info_Report » pour collecter un
maximum d\'informations :

- sur l\'environnement système, matériel, 4D

- sur la base : structure, données, triggers, index, réglages
  personnalisés utilisés, etc.

- en temps réel : mémoire, cache, utilisateurs connectés, process, etc.

Ce composant peut être utilisé en Production sans problème : l'impact
sur les performances de l'application monitorée est négligeable.

Vous pouvez également utiliser l'onglet « Moniteur » de la fenêtre
d'administration de 4D Server pour afficher des informations dynamiques
relatives à l'exploitation de la base de données ainsi que des
informations sur le système et l'application 4D Server.

La zone graphique permet de visualiser l'évolution en temps réel de
plusieurs paramètres :

- le taux d'utilisation des processeurs,

- le trafic réseau,

- l\'état de la mémoire.

Ces informations peuvent être obtenues par programmation grâce à la
commande « LIRE APERCU ACTIVITE ». Cette commande permet d'obtenir un
instantané des n opérations les plus coûteuses en temps et/ou les plus
fréquentes en cours d'exécution telles que l'écriture du cache ou
l'exécution de formules.

Par défaut, la commande « LIRE APERCU ACTIVITE » traite des opérations
effectuées en local. Avec 4D en mode distant, vous pouvez également
obtenir l'aperçu des opérations effectuées sur le serveur : il suffit
pour cela de passer le paramètre « \* ». Dans ce cas, les données du
serveur seront récupérées localement.

Une nouvelle commande est également apparue en version 4D v16 R4
(modifiée en v16 R5) : « Lire activite process ». Elle retourne une vue
instantanée des sessions des utilisateurs connectés et/ou des process
exécutés à un instant précis, y compris les process internes qui
n'étaient pas accessibles avec la commande « INFORMATIONS PROCESS ».
