"""
Pipeline de nettoyage des données Online Retail II.
Usage : python src/clean_data.py
"""
import pandas as pd
import logging
from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)


def load_raw_data(path) -> pd.DataFrame:
    """Charge le dataset brut (CSV ou Excel selon l'extension)."""
    logger.info(f"Chargement des données brutes depuis {path}")
    if str(path).endswith(".xlsx"):
        df = pd.read_excel(path)
    else:
        df = pd.read_csv(path, encoding="ISO-8859-1")
    logger.info(f"{len(df):,} lignes chargées, {df.shape[1]} colonnes")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie le dataset : valeurs nulles, doublons, types, valeurs aberrantes."""
    df = df.copy()

    # Harmoniser les noms de colonnes
    df.columns = [c.strip().replace(" ", "") for c in df.columns]
    
    #Renommer certaines colonnes pour plus de clarté
    rename_map = {
        "Invoice": "InvoiceNo",
        "Price": "UnitPrice",
    }
    df = df.rename(columns=rename_map)

    # Supprimer les lignes sans CustomerID (impossible de les rattacher à un client)
    before = len(df)
    df = df.dropna(subset=["CustomerID"])
    logger.info(f"Lignes sans CustomerID supprimées : {before - len(df):,}")

    # Supprimer les doublons exacts
    before = len(df)
    df = df.drop_duplicates()
    logger.info(f"Doublons supprimés : {before - len(df):,}")

    # Convertir les types
    df["CustomerID"] = df["CustomerID"].astype(int).astype(str)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)

    # Identifier les annulations (InvoiceNo commençant par 'C')
    df["IsCancelled"] = df["InvoiceNo"].str.startswith("C")

    # Retirer les quantités et prix négatifs ou nuls pour l'analyse principale
    # (on garde une trace des annulations séparément si besoin)
    df_sales = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0) & (~df["IsCancelled"])].copy()

    # Feature engineering
    df_sales["TotalPrice"] = df_sales["Quantity"] * df_sales["UnitPrice"]
    df_sales["Year"] = df_sales["InvoiceDate"].dt.year
    df_sales["Month"] = df_sales["InvoiceDate"].dt.month
    df_sales["Day"] = df_sales["InvoiceDate"].dt.day
    df_sales["Hour"] = df_sales["InvoiceDate"].dt.hour
    df_sales["DayOfWeek"] = df_sales["InvoiceDate"].dt.day_name()
    df_sales["YearMonth"] = df_sales["InvoiceDate"].dt.to_period("M").astype(str)

    logger.info(f"Dataset final : {len(df_sales):,} lignes de ventes valides")
    return df_sales


def save_processed_data(df: pd.DataFrame, path) -> None:
    df.to_csv(path, index=False)
    logger.info(f"Données nettoyées sauvegardées dans {path}")


def main():
    df_raw = load_raw_data(RAW_DATA_PATH)
    df_clean = clean_data(df_raw)
    save_processed_data(df_clean, PROCESSED_DATA_PATH)


if __name__ == "__main__":
    main()
