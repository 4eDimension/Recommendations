# 4D Server

4D Server est un système intégré de développement client / serveur,
optimisé pour créer des applications d'entreprise robustes avec un
système de base de données intégrée. Bien que 4D peut envoyer des
données (avec des normes telles que HTTP, SOAP, ODBC ou OCI) ou peut
être accessible à partir de l'extérieur (avec HTTP, SOAP, ODBC / SQL),
l'utilisation principale est basée sur le langage de développement
interne « 4D », en utilisant un protocole réseau interne et propriétaire
pour communiquer entre le client et le serveur.

La communication réseau prend en charge le cryptage TLS 1.3, soit à
l'aide d'une clé prédéfinie (pas de certificat SSL requis), soit avec un
fichier contenant une clé.

La liaison étroite entre le langage de développement et la communication
réseau permet une construction de haut niveau dans le concept de
protection, en évitant les scénarios d'attaque typiques tels que
l'injection SQL ou des attaques « buffer overflow ».

Le langage 4D est un langage puissant et mature, parfaitement conçu pour
construire des systèmes d'applications d'entreprise. Il propose plus
de 1 500 commandes, couvrant les opérations de base de données (tris,
requêtes, créations, transactions et ainsi de suite), l'impression, la
communication avec d'autres appareils ou ordinateurs, la gestion des
documents, une fenêtre ou une interface utilisateur, et bien plus
encore. Jeter un coup d'œil au manuel du langage 4D pour plus de
détails.

Le langage lui-même est segmenté, même en mode interprété (développement
ou prototypage), il n'est jamais exécuté comme une évaluation de texte.
En mode production, le langage est compilé et intègre un contrôle
automatique de plage de version contre les attaques de type « buffer
overflow ».
