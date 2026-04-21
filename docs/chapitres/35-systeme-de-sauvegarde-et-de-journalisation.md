# Système de sauvegarde et de journalisation

4D fournit par défaut un système de journalisation transactionnelle.
Chaque opération de modification de données est enregistrée et peut être
annulée. En cas d'urgence, le travail de la journée peut être
restaurée - rien n'est perdu. Dans le cas d'une interruption, la base
de données est automatiquement vérifiée lors du redémarrage et les
opérations manquantes (conservées en mémoire mais non stockées sur le
disque encore) sont restaurées, afin d'avoir une base de données
contenant toutes les informations. Même dans le cas d'une corruption
totale des données (endommagement du disque, etc.), le fichier de
données est automatiquement restauré à partir de la dernière sauvegarde
complète et le fichier d'historique (contenant le travail quotidien) est
intégré.

Le journal des transactions peut également être utile en cas de
suppression accidentelle (ou volontaire d'enregistrements) et, à la
fois pour la récupération légale des données.

La sauvegarde standard fait partie du produit 4D, aucune licence
supplémentaire n'est nécessaire, seul un disque dur additionnel est
vivement conseillé (pour se protéger des pannes de disque).

Dans les environnements 24/7, 4D prend en charge l'utilisation de
systèmes miroirs montés en cascade et/ou en étoile. Une production, un
miroir et un miroir secondaire permettent d'assurer un service 24 heures
sur 24. Un système de miroir supplémentaire pourrait être exécuté dans
une autre ville ou le Cloud pour protéger les données, même en cas de
catastrophes extrêmes.

Parallèlement à cela, le système de journalisation transactionnelle de
4D prend en charge les snapshots des machines virtuelles (comme Volume
Shadow Copy Service de VMWare vSphere (Hyperviseur ESXi, pris en charge
à partir de la version 16 R2).
