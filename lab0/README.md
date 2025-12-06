# TP : Installation d’un Cluster Hadoop avec Docker


**Cours :** Big Data — Année 2025-2026  
**Répertoire :** hadoop-cluster-lab

## Objectif
Installer et expérimenter un cluster Hadoop (NameNode + 2 DataNodes) en utilisant Docker et se familiariser avec les commandes HDFS.

## Contenu du dépôt
- `docker-compose.yml` — configuration des 3 conteneurs (master, slave1, slave2)
- `run-containers.sh` — commandes `docker run` (alternative au compose)
- `start-hadoop.sh` — script de démarrage Hadoop/YARN
- `data/purchases.txt` — fichier d'exemple
- `README.md` — ce document
- `screenshots/` — captures (NameNode UI, ResourceManager UI, JobHistory)
- `hdfs_commands.txt` — commandes HDFS utilisées
- `notes.md` — rapport et remarques

## Image utilisée
`yassern1/hadoop-spark-jupyter:1.0.3`

## Ports exposés
- NameNode UI : 9870
- ResourceManager UI : 8088
- Spark : 7077
- JobHistory : 19888
- Jupyter (si utilisé) : 8080
(voir `docker-compose.yml` pour détails)

## Instructions pour reproduire (Linux)
1. Cloner :
```bash
git clone https://github.com/<ton-user>/hadoop-cluster-lab.git
cd hadoop-cluster-lab
