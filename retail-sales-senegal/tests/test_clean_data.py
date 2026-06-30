"""
Tests unitaires pour le module clean_data.
Usage : pytest tests/
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pandas as pd
from src.clean_data import clean_data


def make_sample_df():
    return pd.DataFrame({
        "InvoiceNo": ["536365", "536365", "C536366", "536367", "536367"],
        "StockCode": ["85123A", "71053", "84406B", "22752", "21730"],
        "Description": ["WHITE LAMP", "WHITE METAL", "CREAM CUPID", "SET 7", "GLASS STAR"],
        "Quantity": [6, 6, -1, 32, 0],
        "InvoiceDate": ["2010-12-01 08:26:00"] * 5,
        "UnitPrice": [2.55, 3.39, 7.65, 1.85, 0.0],
        "CustomerID": [17850.0, 17850.0, None, 13047.0, 13047.0],
        "Country": ["United Kingdom"] * 5,
    })


def test_clean_data_removes_nulls_customerid():
    df = make_sample_df()
    result = clean_data(df)
    assert result["CustomerID"].isnull().sum() == 0


def test_clean_data_removes_negative_quantity():
    df = make_sample_df()
    result = clean_data(df)
    assert (result["Quantity"] <= 0).sum() == 0


def test_clean_data_removes_zero_price():
    df = make_sample_df()
    result = clean_data(df)
    assert (result["UnitPrice"] <= 0).sum() == 0


def test_clean_data_creates_total_price():
    df = make_sample_df()
    result = clean_data(df)
    assert "TotalPrice" in result.columns
    assert (result["TotalPrice"] == result["Quantity"] * result["UnitPrice"]).all()


def test_clean_data_creates_date_features():
    df = make_sample_df()
    result = clean_data(df)
    for col in ["Year", "Month", "Day", "Hour", "DayOfWeek", "YearMonth"]:
        assert col in result.columns
