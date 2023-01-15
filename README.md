# ROIMeanReversion

ROIMeanReversion is a Python class that implements a mean reversion strategy for a given stock ticker. 

## Installation


Clone the repository to your local machine.

```bash
git clone https://github.com/nate-belete/ROIMeanReversion.git
```

You will need to install pandas, numpy, and yfinance.

```bash
pip install pandas
pip install numpy
pip install yfinance
```

## Usage

Once you have cloned the repository and installed the necessary packages, you can create an instance of the ROIMeanReversion class.

```python
from ROIMeanReversion import ROIMeanReversion

# Create instance of the ROIMeanReversion class
roi_mean_reversion = ROIMeanReversion(ticker='AAPL', var='Close', N=20, start_date='2018-01-01',
                                      end_date='2023-12-31', interval='1wk')

# Calculate ROI
roi_mean_reversion.calculate_ROI()

# Calculate rolling window mean of ROI
roi_mean_reversion.calculate_N_period_ROI_MA()

# Create buy and sell conditions
roi_mean_reversion.create_buy_sell_conditions()

# Plot results
roi_mean_reversion.plot_results()

# Buy and sell stock
buy_sell_stock(roi_mean_reversion)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.