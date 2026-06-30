-- ============================================================
-- 03_ca_mensuel.sql
-- Évolution du chiffre d'affaires mensuel + croissance MoM
-- ============================================================

WITH ca_mensuel AS (
    SELECT
        "YearMonth",
        ROUND(SUM("TotalPrice")::numeric, 2) AS chiffre_affaires,
        COUNT(DISTINCT "InvoiceNo") AS nb_commandes,
        COUNT(DISTINCT "CustomerID") AS nb_clients
    FROM sales
    GROUP BY "YearMonth"
)
SELECT
    "YearMonth",
    chiffre_affaires,
    nb_commandes,
    nb_clients,
    -- Fonction fenêtre : comparaison au mois précédent
    LAG(chiffre_affaires) OVER (ORDER BY "YearMonth") AS ca_mois_precedent,
    ROUND(
        (chiffre_affaires - LAG(chiffre_affaires) OVER (ORDER BY "YearMonth"))
        / NULLIF(LAG(chiffre_affaires) OVER (ORDER BY "YearMonth"), 0) * 100, 2
    ) AS croissance_pct
FROM ca_mensuel
ORDER BY "YearMonth";
