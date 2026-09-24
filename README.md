# Quantitative Analytics

A quantitative analytics portfolio focused on financial mathematics, statistical modeling, risk measurement, portfolio construction, time-series analysis, Monte Carlo simulation, and machine learning for financial data.

## Quantitative Workflow

**Market Data → Data Quality → Returns → Statistical Analysis → Risk → Forecasting → Portfolio Construction → Optimization → Backtesting → Model Evaluation → Risk Controls → Visualization**

The objective is to connect mathematical models to measurable financial decisions while clearly documenting assumptions, uncertainty, limitations, and computational methods.

## Core Quantitative Domains

### 1. Market Statistics
- Simple returns
- Log returns
- Mean and median return
- Variance
- Standard deviation
- Covariance
- Correlation
- Beta
- Alpha
- Sharpe ratio
- Sortino ratio
- Information ratio
- Tracking error
- Skewness
- Kurtosis

### 2. Risk Measurement
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Expected Shortfall
- Maximum drawdown
- Downside deviation
- Volatility
- Semi-variance
- Stress testing
- Scenario analysis
- Risk contribution
- Marginal VaR
- Component VaR

### 3. Probability and Statistical Modeling
- Probability distributions
- Conditional probability
- Bayes' theorem
- Expected value
- Confidence intervals
- Hypothesis testing
- Bootstrap
- Monte Carlo simulation
- Maximum likelihood estimation
- Bayesian inference

### 4. Time-Series Modeling
- Moving averages
- Exponential smoothing
- Autoregression
- Moving-average models
- ARMA
- ARIMA
- SARIMA
- VAR
- GARCH
- EGARCH
- GJR-GARCH
- State-space models

### 5. Portfolio Analytics
- Portfolio return
- Portfolio variance
- Covariance matrices
- Efficient frontier
- Minimum-variance portfolio
- Maximum-Sharpe portfolio
- Risk parity
- Factor exposure
- Portfolio beta
- Diversification
- Rebalancing

### 6. Derivatives and Financial Mathematics
- Time value of money
- Present value
- Future value
- Discount factors
- Bond pricing
- Duration
- Convexity
- Forward pricing
- Futures
- Options
- Black-Scholes
- Greeks
- Implied volatility
- Heston-style stochastic volatility

### 7. Machine Learning for Finance
- Linear and regularized regression
- Random Forest
- Gradient boosting
- XGBoost
- LightGBM
- LSTM
- GRU
- Transformers
- Anomaly detection
- Classification
- Clustering
- Feature selection

## Forecasting Horizons

Research can evaluate models across:

| Horizon | Example Use |
|---|---|
| 1 day | Short-term forecasting and risk |
| 1 week | Tactical analysis |
| 1 month | Monthly allocation |
| Quarterly | Portfolio planning |
| 1 year | Strategic forecasting |
| 3 years | Long-range scenarios |
| 5 years | Strategic investment analysis |
| 10 years | Long-term scenario analysis |

Long-horizon forecasts should be interpreted as scenario/model outputs rather than guaranteed predictions.

## Financial Measures

| Measure | Core Idea |
|---|---|
| Return | Change in investment value |
| Volatility | Dispersion of returns |
| Covariance | Joint movement of two variables |
| Correlation | Standardized co-movement |
| Beta | Sensitivity to a benchmark |
| Alpha | Return relative to a specified benchmark/model |
| VaR | Loss threshold at a chosen confidence level |
| CVaR | Average loss beyond a VaR threshold |
| Sharpe | Excess return per unit of total volatility |
| Sortino | Excess return per unit of downside risk |
| Drawdown | Decline from a previous peak |
| Maximum Drawdown | Largest observed peak-to-trough decline |

## Technology Stack

**Python:** NumPy, Pandas, SciPy, statsmodels  
**Finance:** yfinance, pandas-datareader where applicable, QuantLib where appropriate  
**Machine Learning:** scikit-learn, XGBoost, LightGBM, PyTorch  
**Time Series:** statsmodels, arch  
**Optimization:** SciPy optimize, CVXPY, OR-Tools where appropriate  
**Visualization:** Matplotlib, Plotly  
**Development:** Jupyter, Google Colab, Git, GitHub

## Repository Structure

| Directory | Purpose |
|---|---|
| data/ | Data documentation and schemas |
| returns/ | Return calculations and diagnostics |
| risk/ | VaR, CVaR, drawdown, stress testing |
| portfolio/ | Portfolio construction and optimization |
| time_series/ | Statistical forecasting |
| derivatives/ | Pricing and Greeks |
| monte_carlo/ | Simulation methods |
| factors/ | Factor and exposure analysis |
| machine_learning/ | ML-based financial modeling |
| deep_learning/ | LSTM and Transformer studies |
| backtesting/ | Strategy/model evaluation |
| notebooks/ | Reproducible analysis |
| src/ | Reusable Python modules |
| tests/ | Automated tests |
| reports/ | Technical research reports |
| visualizations/ | Research figures |

## Research Standards

Every quantitative study should document:

1. Financial question
2. Data source
3. Data frequency
4. Lookback period
5. Data-cleaning rules
6. Return definition
7. Model assumptions
8. Training/test methodology
9. Transaction-cost assumptions
10. Evaluation metrics
11. Risk measures
12. Sensitivity analysis
13. Limitations
14. Reproducibility information

## Important Modeling Controls

Financial models are especially vulnerable to:

- Look-ahead bias
- Survivorship bias
- Data leakage
- Overfitting
- Multiple-testing effects
- Non-stationarity
- Regime changes
- Transaction costs
- Slippage
- Liquidity constraints
- Parameter instability

A backtest should therefore separate **in-sample development** from **out-of-sample evaluation** and document assumptions that materially affect results.

## Example Research Projects

### Project 1 — Multi-Horizon Financial Forecasting
Compare statistical and deep-learning models from one-day through ten-year horizons.

### Project 2 — Volatility Forecasting
Compare historical volatility, GARCH-family models, and neural forecasting methods.

### Project 3 — Portfolio Optimization
Compare equal-weight, minimum-variance, maximum-Sharpe, and risk-parity approaches using common constraints.

### Project 4 — VaR and CVaR
Compare historical simulation, parametric, and Monte Carlo risk estimates.

### Project 5 — ML Asset Classification
Use supervised learning to classify market regimes, risk states, or other clearly defined targets without leakage.

## Reproducibility

Record:
- Dataset/version
- Date range
- Time zone
- Data frequency
- Features
- Random seed
- Model parameters
- Optimization constraints
- Transaction-cost assumptions
- Software environment
- Results
- Code version

## Disclaimer

This repository is an educational and research portfolio. Quantitative results are model outputs and should not be interpreted as personalized investment advice or guarantees of future performance.

## Author

**Whitney Moss** — Machine Learning Engineer | AI & Data Analyst | Data Scientist
