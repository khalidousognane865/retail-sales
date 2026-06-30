-- ============================================================
-- 01_create_tables.sql
-- Création du schéma de base de données pour le projet retail
-- ============================================================

DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    "InvoiceNo" VARCHAR(20),
    "StockCode" VARCHAR(20),
    "Description" TEXT,
    "Quantity" INTEGER,
    "InvoiceDate" TIMESTAMP,
    "UnitPrice" NUMERIC(10, 2),
    "CustomerID" VARCHAR(20),
    "Country" VARCHAR(100),
    "IsCancelled" BOOLEAN,
    "TotalPrice" NUMERIC(12, 2),
    "Year" INTEGER,
    "Month" INTEGER,
    "Day" INTEGER,
    "Hour" INTEGER,
    "DayOfWeek" VARCHAR(20),
    "YearMonth" VARCHAR(10)
);

-- Index pour accélérer les requêtes analytiques
CREATE INDEX idx_sales_customer ON sales ("CustomerID");
CREATE INDEX idx_sales_date ON sales ("InvoiceDate");
CREATE INDEX idx_sales_country ON sales ("Country");
CREATE INDEX idx_sales_yearmonth ON sales ("YearMonth");
