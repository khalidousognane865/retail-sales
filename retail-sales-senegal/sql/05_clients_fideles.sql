-- ============================================================
-- 05_clients_fideles.sql
-- Identification des clients les plus fidèles (sous-requête + CTE)
-- ============================================================

WITH stats_clients AS (
    SELECT
        "CustomerID",
        "Country",
        COUNT(DISTINCT "InvoiceNo") AS nb_commandes,
        ROUND(SUM("TotalPrice")::numeric, 2) AS depense_totale,
        MIN("InvoiceDate") AS premiere_commande,
        MAX("InvoiceDate") AS derniere_commande
    FROM sales
    GROUP BY "CustomerID", "Country"
)
SELECT
    "CustomerID",
    "Country",
    nb_commandes,
    depense_totale,
    premiere_commande,
    derniere_commande,
    (derniere_commande - premiere_commande) AS duree_relation
FROM stats_clients
WHERE nb_commandes >= (
    -- Sous-requête : seuil = nombre moyen de commandes + 1 écart-type
    SELECT AVG(nb_commandes) + STDDEV(nb_commandes) FROM stats_clients
)
ORDER BY depense_totale DESC
LIMIT 20;
