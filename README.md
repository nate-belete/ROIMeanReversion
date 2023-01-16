## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project requires Python 3.6+ and the following libraries:

- yfinance
- pandas
- numpy
- matplotlib

### Installing

Clone the repository to your local machine.

`git clone https://github.com/nate-belete/ROI-Mean-Reversion.git`

Install the required libraries.

`pip install yfinance pandas numpy matplotlib`

## Usage

Create an instance of the `ROIMeanReversion` class.

```python
roi_mean_reversion = ROIMeanReversion(ticker, var, rolling_window_size, fast_sma, medium_sma, slow_sma, start_date, end_date, interval)
```

Parameters:

- ticker (str): Stock ticker symbol
- var (str): Stock variable to use (e.g. "Close" or "Adj Close")
- rolling_window_size (int): Rolling window size used to calculate mean reversion
- fast_sma (int): Window size to calculate the fast simple moving average
- medium_sma (int): Window size to calculate the medium simple moving average
- slow_sma (int): Window size to calculate the slow simple moving average
- start_date (str): Start date for data retrieval in the format "YYYY-MM-DD"
- end_date (str): End date for data retrieval in the format "YYYY-MM-DD"
- interval (str): Interval size for data retrieval (e.g. "1d", "1wk", "1mo")

Call the `calculate_SMA_MA()` method to calculate the simple moving averages.

```python
roi_mean_reversion.calculate_SMA_MA()
```

Call the `calculate_trend()` method to calculate the trend of the stock market.

```python
roi_mean_reversion.calculate_trend()
```

Call the `calculate_ROI()` method to calculate the return on investment for the given stock.

```python
roi_mean_reversion.calculate_ROI()
```

Call the `calculate_N_period_ROI_MA()` method to calculate a rolling window mean of the ROI.

```python
roi_mean_reversion.calculate_N_period_ROI_MA()
```

Call the `calculate_z_score()` method to calculate the z-score of the ROI at each period.

```python
roi_mean_reversion.calculate_z_score()
```

Call the `create_buy_sell_conditions()` method to create buy and sell conditions based on the ROI mean.

```python
roi_mean_reversion.create_buy_sell_conditions()
```

Call the `plot_results()` method to plot the stock data and buy/sell signals.

```python
roi_mean_reversion.plot_results()
```

Finally, call the `buy_sell_stock()` function to buy and sell a stock based on the action.

```python
buy_sell_stock(roi_mean_reversion)
```
