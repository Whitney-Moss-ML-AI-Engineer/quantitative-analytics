"""Geometric-Brownian-motion Monte Carlo paths."""
import numpy as np

def gbm_paths(s0, mu, sigma, years=1, steps=252, paths=10000, seed=42):
    rng=np.random.default_rng(seed)
    dt=years/steps
    z=rng.normal(size=(paths,steps))
    increments=(mu-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*z
    return s0*np.exp(np.cumsum(increments,axis=1))
