# Lancer PostgreSQL + pgAdmin avec Docker

## Pré-requis
- Docker Desktop installé (Windows/Mac) ou Docker Engine + Docker Compose (Linux)
- Vérifier : `docker --version` et `docker compose version`

## Démarrage

```bash
cd retail-sales-senegal
docker compose up -d
```

Cela lance 2 conteneurs :
| Service | URL/Port | Identifiants |
|---|---|---|
| PostgreSQL | localhost:5432 | user: `postgres` / pwd: `changeme` / db: `retail_kaza` |
| pgAdmin | http://localhost:5050 | email: `admin@retail.sn` / pwd: `changeme` |

Le script `sql/01_create_tables.sql` est exécuté automatiquement au premier démarrage (création de la table `sales`).

## Vérifier que ça tourne

```bash
docker compose ps
docker compose logs postgres
```

## Se connecter à pgAdmin
1. Ouvrir http://localhost:5050
2. Se connecter avec `admin@retail.sn` / `changeme`
3. Ajouter un serveur : clic droit "Servers" → Register → Server
   - Name : `retail_kaza`
   - Host : `postgres` (nom du service Docker, pas `localhost`)
   - Port : `5432`
   - Username : `postgres` / Password : `changeme`

## Mettre à jour le .env
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=retail_senegal
DB_USER=postgres
DB_PASSWORD=changeme
```

## Charger les données nettoyées
```bash
python src/clean_data.py
python src/load_to_postgres.py
```

## Arrêter / Réinitialiser
```bash
docker compose stop          # arrête sans supprimer les données
docker compose down          # arrête et supprime les conteneurs
docker compose down -v       # supprime aussi les volumes (reset complet de la DB)
```
