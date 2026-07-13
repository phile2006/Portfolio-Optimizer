"""Markowitz mean-variance optimization.

Pure numerical core: takes a wide price matrix (one column per ticker) and
returns optimal portfolio weights with risk/return metrics. Knows nothing
about databases, HTTP, or where the prices came from.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.optimize import minimize

TRADING_DAYS = 252


@dataclass(frozen=True)
class Portfolio:
    weights: dict[str, float]
    expected_return: float
    volatility: float
    sharpe: float

