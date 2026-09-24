"""Historical VaR, CVaR, and maximum drawdown."""
import numpy as np

def historical_var(returns, confidence=0.95):
    return float(-np.quantile(returns, 1-confidence))

def historical_cvar(returns, confidence=0.95):
    threshold=np.quantile(returns,1-confidence)
    return float(-returns[returns<=threshold].mean())

def max_drawdown(prices):
    wealth=prices/prices.iloc[0]
    return float((wealth/wealth.cummax()-1).min())
