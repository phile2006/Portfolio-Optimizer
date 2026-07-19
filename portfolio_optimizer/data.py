"""Price data acquisition from Yahoo Finance."""
from __future__ import annotations

import pandas as pd
import yfinance as yf


def fetch_prices(tickers: list[str], period: str = "2y",
                 interval: str = "1d") -> pd.DataFrame:
    """Download adjusted close prices as a wide matrix (columns = tickers).

    Rows with any missing value are dropped so all series share one calendar.
    Raises if a requested ticker returns no data.
    """
    if len(tickers) < 2:
        raise ValueError("Need at least 2 tickers.")
    raw = yf.download(tickers, period=period, interval=interval,
                      auto_adjust=True, progress=False)
    closes = raw["Close"]
    if isinstance(closes, pd.Series):
        closes = closes.to_frame()
    missing = [t for t in tickers
               if t not in closes.columns or closes[t].isna().all()]
    if missing:
        raise ValueError(f"No price data for: {missing}")
    return closes[tickers].dropna()
