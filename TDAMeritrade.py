import requests
from ROIMeanReversion import ROIMeanReversion


class TDAMeritrade:
    """
    This class implements a trading strategy for a given stock ticker
    using the TD Ameritrade API.
    
    Parameters:
    ticker (str): Stock ticker symbol
    var (str): Stock variable to use (e.g. "Close" or "Adj Close")
    rolling_window_size (int): Rolling window size used to calculate mean reversion
    fast_sma (int): Window size to calculate the fast simple moving average
    slow_sma (int): Window size to calculate the slow simple moving average
    start_date (str): Start date for data retrieval in the format "YYYY-MM-DD"
    end_date (str): End date for data retrieval in the format "YYYY-MM-DD"
    interval (str): Interval size for data retrieval (e.g. "1d", "1wk", "1mo")
    access_token (str): Your TD Ameritrade access token
    account_id (str): Your TD Ameritrade account ID
    
    Attributes:
    roi_mean_reversion (ROIMeanReversion): Instance of ROIMeanReversion class
    stock_price (float): Current stock price
    quantity (int): Number of shares of stock to buy/sell
    order_type (str): Type of order to place
    
    Methods:
    execute_buy_sell_orders(): Executes buy and sell trades based on the ROIMeanReversion class
    """
    
    def __init__(self, ticker, var, rolling_window_size, fast_sma, slow_sma, start_date, end_date, interval, 
                access_token, account_id):

        self.ticker = ticker
        self.var = var
        self.rolling_window_size = rolling_window_size
        self.fast_sma = fast_sma
        self.slow_sma = slow_sma
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.access_token = access_token
        self.account_id = account_id
        self.roi_mean_reversion = ROIMeanReversion(self.ticker, self.var, self.rolling_window_size, self.fast_sma, 
                                                   self.slow_sma, self.start_date, self.end_date, self.interval)
        self.stock_price = 0
        self.quantity = 0
        self.order_type = ''

    def execute_buy_sell_order(access_token, account_id, ticker, stock_price, quantity, order_type):
        """
        Function that calls the TD Ameritrade API to execute buy and sell orders for a given stock.

        Parameters:
        access_token (str): Your TD Ameritrade access token
        account_id (str): Your TD Ameritrade account ID
        ticker (str): Stock ticker symbol
        stock_price (float): Current stock price
        quantity (int): Number of shares of stock to buy/sell
        order_type (str): Type of order to place (buy or sell)

        Returns:
        response (JSON): Response from TD Ameritrade API
        """

        # Construct the request headers
        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json'
        }

        # Construct the request body
        body = {
            'orderType': order_type,
            'session': 'NORMAL',
            'duration': 'DAY',
            'orderStrategyType': 'SINGLE',
            'orderLegCollection': [
                {
                'instruction': order_type,
                'quantity': quantity,
                'instrument': {
                    'symbol': ticker,
                    'assetType': 'EQUITY'
                }
                }
            ],
            'price': stock_price
        }

        # Construct the request URL
        url = 'https://api.tdameritrade.com/v1/accounts/' + account_id + '/orders'

        # Execute the POST request
        response = requests.post(url, headers=headers, json=body)

    # Return the response
    return response.json()
    
    def execute_buy_sell_orders(self):
        """
        Executes buy and sell trades based on the ROIMeanReversion class.
        """
        # Iterate over rows of df
        for index, row in self.roi_mean_reversion.df.iterrows():
            # If 'Buy' action, execute buy order
            if row['action'] == 'Buy':
                self.stock_price = row[self.roi_mean_reversion.var]
                self.quantity = 1
                self.order_type = 'buy'
                # Call TD Ameritrade API
                api.execute_buy_sell_order(self.access_token, self.account_id, self.ticker, self.stock_price, self.quantity, self.order_type)
            # If 'Sell' action, execute sell order
            elif row['action'] == 'Sell':
                self.stock_price = row[self.roi_mean_reversion.var]
                self.quantity = 1
                self.order_type = 'sell'
                # Call TD Ameritrade API
                api.execute_buy_sell_order(self.access_token, self.account_id, self.ticker, self.stock_price, self.quantity, self.order_type)