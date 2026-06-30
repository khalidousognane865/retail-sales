"""
Charge les données nettoyées dans PostgreSQL.
Usage : python src/load_to_postgres.py
"""
import pandas as pd
import logging
from sqlalchemy import create_engine
from config import DATABASE_URL, PROCESSED_DATA_PATH

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)


def main():
    logger.info("Connexion à PostgreSQL...")
    engine = create_engine(DATABASE_URL)

    logger.info(f"Lecture des données nettoyées depuis {PROCESSED_DATA_PATH}")
    df = pd.read_csv(PROCESSED_DATA_PATH, parse_dates=["InvoiceDate"])

    logger.info(f"Chargement de {len(df):,} lignes dans la table 'sales'...")
    df.to_sql("sales", engine, if_exists="replace", index=False, chunksize=10000)

    logger.info("Chargement terminé avec succès ✅")


if __name__ == "__main__":
    main()
