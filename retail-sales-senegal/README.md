#  Analyse des Ventes Retail 

> Projet Data Analyst : nettoyage, EDA, SQL analytique et dashboard Power BI sur des données de vente retail (Online Retail II Dataset, UCI/Kaggle)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811)
![Status](https://img.shields.io/badge/Status-En%20cours-yellow)

---

##  Objectif

Analyser 12 mois de transactions retail pour :
- Comprendre les habitudes d'achat des clients
- Identifier les produits les plus rentables
- Segmenter les clients (analyse RFM)
- Aider à optimiser les stocks en période de forte demande (Tabaski, Korité, Noël)

##  Aperçu du dashboard

![Dashboard preview](reports/figures/dashboard_preview.png)
*(à remplacer par une vraie capture d'écran une fois le dashboard Power BI terminé)*

##  Structure du projet

```
retail-sales-senegal/
├── data/
│   ├── raw/                  # Données brutes (non versionnées, voir .gitignore)
│   └── processed/            # Données nettoyées (CSV/Parquet)
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_rfm_analysis.ipynb
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_top_produits.sql
│   ├── 03_ca_mensuel.sql
│   ├── 04_panier_moyen.sql
│   ├── 05_clients_fideles.sql
│   └── 06_ventes_par_pays.sql
├── src/
│   ├── __init__.py
│   ├── clean_data.py         # Pipeline de nettoyage réutilisable
│   ├── load_to_postgres.py   # Chargement DB
│   ├── rfm.py                 # Calcul du score RFM
│   └── config.py              # Variables de configuration (.env)
├── powerbi/
│   └── dashboard_ventes.pbix  # Fichier Power BI (à ajouter après création)
├── reports/
│   ├── figures/                # Graphiques exportés
│   └── rapport_management.pdf  # Rapport final
├── tests/
│   └── test_clean_data.py
├── .env.example
├── .gitignore
├── docker-compose.yml         # PostgreSQL + pgAdmin en local
├── DOCKER.md                  # guide d'utilisation Docker
├── requirements.txt
└── README.md
```

##  Installation (VS Code)

### Option A — Avec Docker (recommandé, plus rapide)

```bash
git clone https://github.com/<ton-username>/retail-sales-senegal.git
cd retail-sales-senegal
docker compose up -d        # lance PostgreSQL + pgAdmin
cp .env.example .env        # garder les valeurs par défaut (déjà alignées avec docker-compose.yml)
```
Voir `DOCKER.md` pour le détail (pgAdmin, logs, reset...).

### Option B — Sans Docker (PostgreSQL installé en local)

```bash
# 1. Cloner le repo
git clone https://github.com/khalidousognane865/retail-sales
cd retail-sales

# 2. Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Copier le fichier d'environnement
cp .env.example .env
# → remplir les identifiants PostgreSQL dans .env

# 5. Télécharger le dataset
# Aller sur https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci
# Télécharger et placer le CSV dans data/raw/online_retail_II.csv
```

### Extensions VS Code recommandées
- Python (Microsoft)
- Jupyter (Microsoft)
- SQLTools + driver PostgreSQL
- Power BI (aperçu, optionnel)
- GitLens

## 🚀 Utilisation

```bash
# Nettoyage des données
python src/clean_data.py

# Chargement dans PostgreSQL
python src/load_to_postgres.py

# Calcul RFM
python src/rfm.py
```

Puis ouvrir les notebooks dans l'ordre : `01_data_cleaning.ipynb` → `02_eda.ipynb` → `03_rfm_analysis.ipynb`.

##  Résultats clés 

| Indicateur | Valeur |
|---|---|
| Chiffre d'affaires total | 17,374,804.27 |
| Panier moyen | 469.98 |
| Nombre de clients uniques | 5,878|
| Nombre de commande | 36,969|

##  Stack technique

Python · Pandas · NumPy · Matplotlib · Seaborn · SQLAlchemy · PostgreSQL · Power BI Desktop · Jupyter

##  Auteur

Khalidou Sognane — Portfolio:https://portfolio-2fsoeoq45-kaza3.vercel.app/

##  Licence

Projet pédagogique — données sous licence UCI/Kaggle (usage éducatif).
