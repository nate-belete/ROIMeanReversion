import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ROIMeanReversion:
    """
    This class implements a mean reversion strategy for a given stock ticker.
    
    Parameters:
    ticker (str): Stock ticker symbol
    var (str): Stock variable to use (e.g. "Close" or "Adj Close")
    N (int): Rolling window size used to calculate mean reversion
    start_date (str): Start date for data retrieval in the format "YYYY-MM-DD"
    end_date (str): End date for data retrieval in the format "YYYY-MM-DD"
    interval (str): Interval size for data retrieval (e.g. "1d", "1wk", "1mo")
    
    Attributes:
    df (pandas.DataFrame): DataFrame containing stock data
    
    Methods:
    calculate_ROI(): Calculates the return on investment for the given stock
    calculate_N_period_ROI_MA(): Calculates a rolling window mean of the ROI
    create_buy_sell_conditions(): Creates buy and sell conditions based on the ROI mean
    plot_results(): Plots the stock data and buy/sell signals
    """
    
    def __init__(self, ticker, var, N, start_date = '2018-01-01', end_date = '2023-12-31', interval = '1wk'):
        self.ticker = ticker
        self.var = var
        self.N = N
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.df = yf.download(self.ticker, self.start_date, self.end_date, interval = self.interval)
        self.df.dropna(inplace=True)
        self.df = self.df[:-1].copy()
    
    def calculate_ROI(self):
        """
        Calculates the return on investment for the given stock.
        """
        self.df['roi'] = self.df[self.var] / self.df[self.var].shift(1) - 1

    def calculate_N_period_ROI_MA(self):
        """
        Calculates a rolling window mean of the ROI.
        """
        self.df['roi_ma'] = self.df['roi'].rolling(window=self.N).mean()

    def create_buy_sell_conditions(self):
        """
        Creates buy and sell conditions based on the ROI mean.
        """
        self.df.dropna(inplace=True)
        action = ['Nothing'] * self.N
        roi_ma = list(self.df['roi_ma'])
        for i in range(self.N,len(roi_ma)):
            buy_rate = np.percentile(roi_ma[:i], 10)
            sell_rate = np.percentile(roi_ma[:i], 90)
            if roi_ma[i] <= buy_rate:
                action.append('Buy')
            elif roi_ma[i] >= sell_rate:
                action.append('Sell')
            else:
                action.append('Nothing')
        self.df['action'] = action

    def plot_results(self):
        """
        Plots the stock data and buy/sell signals.
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20,12))
        # Plot Close price
        ax1.plot(self.df[self.var], color='blue', label='Close Price')
        # Plot Buy and Sell signals
        for index, row in self.df.iterrows():
            if row['action'] == 'Buy':
                ax1.scatter(index, row[self.var], color='green', label='Buy', s=100)
            elif row['action'] == 'Sell':
                ax1.scatter(index, row[self.var], color='red', label='Sell', s=100)
        # Set labels and legend
        ax2.plot(self.df['roi_ma'], color='Black', label='Close Price  ROI')
        # Plot Buy and Sell signals
        for index, row in self.df.iterrows():
            if row['action'] == 'Buy':
                ax2.scatter(index, row['roi_ma'], color='green', label='Buy', s=100)
            elif row['action'] == 'Sell':
                ax2.scatter(index, row['roi_ma'], color='red', label='Sell', s=100)
        # Ensure x axis doesn't overlap
        plt.tight_layout()
        # Show the plot
        plt.show()
        
    def buy_sell_stock(roi_mean_reversion):
        """
        Function that buys and sells a stock based on action.

        Parameters:
        roi_mean_reversion (ROIMeanReversion): Instance of ROIMeanReversion class

        Returns:
        (float): Profit or loss from stock trading
        """
        # Initialize profit/loss at 0
        profit_loss = 0
        # Initialize cost at 0
        cost = 0

        # Iterate over rows of df
        for index, row in roi_mean_reversion.df.iterrows():
            # If 'Buy' action, buy the stock and track cost
            if row['action'] == 'Buy':
                cost = row[roi_mean_reversion.var]
            # If 'Sell' action, sell the stock and track profit/loss
            elif row['action'] == 'Sell':
                profit_loss += row[roi_mean_reversion.var] - cost

        # Return profit/loss
        return profit_loss