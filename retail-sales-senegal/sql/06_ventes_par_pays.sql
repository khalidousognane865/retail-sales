-- ============================================================
-- 06_ventes_par_pays.sql
-- Répartition des ventes par pays avec part de marché (%)
-- ============================================================

SELECT
    "Country",
    COUNT(DISTINCT "CustomerID") AS nb_clients,
    COUNT(DISTINCT "InvoiceNo") AS nb_commandes,
    ROUND(SUM("TotalPrice")::numeric, 2) AS chiffre_affaires,
    ROUND(
        100.0 * SUM("TotalPrice") / SUM(SUM("TotalPrice")) OVER (), 2
    ) AS part_marche_pct
FROM sales
GROUP BY "Country"
ORDER BY chiffre_affaires DESC;
