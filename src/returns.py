"""Financial return calculations."""
import numpy as np

def simple_returns(prices):
    return prices.pct_change().dropna()

def log_returns(prices):
    return np.log(prices / prices.shift(1)).dropna()

def annualized_volatility(returns, periods=252):
    return returns.std() * np.sqrt(periods)
