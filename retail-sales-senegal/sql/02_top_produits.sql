-- ============================================================
-- 02_top_produits.sql
-- Top 10 produits par chiffre d'affaires et par quantité vendue
-- ============================================================

-- Top 10 produits par CA
SELECT
    "StockCode",
    "Description",
    SUM("Quantity") AS quantite_totale,
    ROUND(SUM("TotalPrice")::numeric, 2) AS chiffre_affaires,
    COUNT(DISTINCT "InvoiceNo") AS nb_commandes
FROM sales
GROUP BY "StockCode", "Description"
ORDER BY chiffre_affaires DESC
LIMIT 10;

-- Top 10 produits par quantité vendue
SELECT
    "StockCode",
    "Description",
    SUM("Quantity") AS quantite_totale,
    ROUND(SUM("TotalPrice")::numeric, 2) AS chiffre_affaires
FROM sales
GROUP BY "StockCode", "Description"
ORDER BY quantite_totale DESC
LIMIT 10;
