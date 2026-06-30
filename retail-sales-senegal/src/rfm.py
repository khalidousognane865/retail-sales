"""
Calcul du score RFM (Récence, Fréquence, Montant) pour segmenter les clients.
Usage : python src/rfm.py
"""
import pandas as pd
import logging
from datetime import timedelta
from src.config import PROCESSED_DATA_PATH, ROOT_DIR

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

RFM_OUTPUT_PATH = ROOT_DIR / "data" / "processed" / "rfm_segments.csv"


def compute_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """Calcule les scores R, F, M et le segment client associé."""
    snapshot_date = df["InvoiceDate"].max() + timedelta(days=1)

    rfm = df.groupby("CustomerID").agg(
        Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("TotalPrice", "sum")
    ).reset_index()

    # Scores en quartiles (1 = pire, 4 = meilleur)
    rfm["R_Score"] = pd.qcut(rfm["Recency"], 4, labels=[4, 3, 2, 1]).astype(int)
    rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)
    rfm["M_Score"] = pd.qcut(rfm["Monetary"], 4, labels=[1, 2, 3, 4]).astype(int)

    rfm["RFM_Score"] = rfm["R_Score"].astype(str) + rfm["F_Score"].astype(str) + rfm["M_Score"].astype(str)
    rfm["RFM_Sum"] = rfm["R_Score"] + rfm["F_Score"] + rfm["M_Score"]

    rfm["Segment"] = rfm.apply(assign_segment, axis=1)
    return rfm


def assign_segment(row) -> str:
    """Attribue un segment marketing basé sur les scores RFM."""
    r, f, m = row["R_Score"], row["F_Score"], row["M_Score"]
    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"
    elif r >= 3 and f >= 3:
        return "Clients fidèles"
    elif r >= 4 and f <= 2:
        return "Nouveaux clients"
    elif r <= 2 and f >= 3:
        return "À risque"
    elif r <= 2 and f <= 2 and m <= 2:
        return "Clients perdus"
    else:
        return "Clients occasionnels"


def main():
    logger.info("Chargement des données nettoyées...")
    df = pd.read_csv(PROCESSED_DATA_PATH, parse_dates=["InvoiceDate"])

    logger.info("Calcul des scores RFM...")
    rfm = compute_rfm(df)

    logger.info("Répartition des segments :")
    logger.info("\n" + rfm["Segment"].value_counts().to_string())

    rfm.to_csv(RFM_OUTPUT_PATH, index=False)
    logger.info(f"Résultats RFM sauvegardés dans {RFM_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
