-- ============================================================
-- 04_panier_moyen.sql
-- Panier moyen global et par pays
-- ============================================================

-- Panier moyen global
SELECT
    ROUND(SUM("TotalPrice")::numeric / COUNT(DISTINCT "InvoiceNo"), 2) AS panier_moyen_global,
    COUNT(DISTINCT "InvoiceNo") AS nb_commandes_total
FROM sales;

-- Panier moyen par pays (top 15)
SELECT
    "Country",
    COUNT(DISTINCT "InvoiceNo") AS nb_commandes,
    ROUND(SUM("TotalPrice")::numeric / COUNT(DISTINCT "InvoiceNo"), 2) AS panier_moyen,
    ROUND(SUM("TotalPrice")::numeric, 2) AS ca_total
FROM sales
GROUP BY "Country"
HAVING COUNT(DISTINCT "InvoiceNo") > 20
ORDER BY panier_moyen DESC
LIMIT 15;
