"""
Configuration centralisée du projet.
Charge les variables d'environnement depuis le fichier .env
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Racine du projet
ROOT_DIR = Path(__file__).resolve().parent.parent

# Charger le fichier .env
load_dotenv(ROOT_DIR / ".env")

# --- Base de données ---
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "retail_senegal")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "kaza123")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# --- Chemins fichiers ---
RAW_DATA_PATH = ROOT_DIR / os.getenv("RAW_DATA_PATH", "data/raw/online_retail_II.csv")
PROCESSED_DATA_PATH = ROOT_DIR / os.getenv("PROCESSED_DATA_PATH", "data/processed/online_retail_clean.csv")
FIGURES_DIR = ROOT_DIR / "reports" / "figures"

# Créer les dossiers si besoin
FIGURES_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
