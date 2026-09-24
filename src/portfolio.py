"""Basic portfolio risk calculations."""
import numpy as np

def portfolio_return(weights, expected_returns):
    return float(np.dot(weights, expected_returns))

def portfolio_variance(weights, covariance):
    w=np.asarray(weights)
    return float(w.T @ covariance @ w)

def portfolio_volatility(weights, covariance):
    return np.sqrt(portfolio_variance(weights,covariance))
