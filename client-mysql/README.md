# Client mysql en conteneur - exercices 6 et 9

Image outil basee sur `ubuntu:latest` contenant `default-mysql-client` plus
quelques utilitaires reseau (`ping`, `dig`, `nc`) pour diagnostiquer.

```bash
docker build -t tp-mysql-client:1.0 .
```

## Exo 6 - lancer un serveur mysql et publier son port

```bash
docker run -d --name tp-mysql \
  -e MYSQL_ROOT_PASSWORD=rootpwd \
  -e MYSQL_DATABASE=exodb \
  -p 3308:3306 \
  mysql:8.0

docker ps
```

Sans `-p`, le serveur n'est joignable que depuis le reseau Docker ; avec
`-p 3308:3306` on peut s'y connecter depuis la machine hote :

```bash
mysql --protocol tcp -h 127.0.0.1 -P 3308 -u root -prootpwd
```

`--protocol tcp` est necessaire car sinon le client mysql tente une socket
Unix locale au lieu d'une connexion reseau.

Pour arreter et supprimer :

```bash
docker kill tp-mysql && docker rm tp-mysql
```

## Exo 9 - deux conteneurs qui se parlent

### 1. Sans reseau commun : echec

```bash
docker run --rm tp-mysql-client:1.0 mysql -h exo-mysql -u root -prootpwd -e "SELECT 1"
```

```
ERROR 2005 (HY000): Unknown MySQL server host 'exo-mysql' (-2)
```

Sur le bridge par defaut, Docker ne fournit pas de resolution DNS par nom de
conteneur : le nom `exo-mysql` ne veut rien dire.

### 2. Avec un user-defined bridge : ca marche

```bash
docker network create exonet
docker network ls

docker run -d --name exo-mysql --network exonet \
  -e MYSQL_ROOT_PASSWORD=rootpwd -e MYSQL_DATABASE=exodb mysql:8.0

docker run --rm -it --network exonet tp-mysql-client:1.0 \
  mysql -h exo-mysql -u root -prootpwd
```

Resultat obtenu :

```
version
8.0.46
nb_etudiants
3
```

La difference entre les deux cas : sur un reseau cree par l'utilisateur, Docker
active un serveur DNS interne, et le **nom du conteneur** devient utilisable
comme nom d'hote. Aucun `-p` n'est necessaire, la publication de port ne sert
qu'a entrer depuis l'exterieur.
