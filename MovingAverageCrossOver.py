import yfinance as yf
import matplotlib.pyplot as plt

class MovingAverageCrossOver:
    """
    This class calculates the number of times the fast moving average crossed over the slow moving average
    """
    def __init__(self, ticker, var, fast_sma, slow_sma, start_date, end_date, interval):
        """
        Initialize the class with the given parameters
        """
        self.ticker = ticker
        self.var = var
        self.fast_sma = fast_sma
        self.slow_sma = slow_sma
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval

    def get_data(self):
        """
        Retrieve the data from the given parameters
        """
        data = yf.download(self.ticker, self.start_date, self.end_date, interval = self.interval)

        return data

    def calculate_moving_averages(self):
        """
        Calculate the fast and slow moving averages
        """
        data = self.get_data()
        fast_sma = data[self.var].rolling(window=self.fast_sma).mean()
        slow_sma = data[self.var].rolling(window=self.slow_sma).mean()
        return fast_sma, slow_sma

    def calculate_crossovers(self):
        """
        Calculate the number of times the fast moving average crossed over the slow moving average
        """
        fast_sma, slow_sma = self.calculate_moving_averages()
        fast_cross_over_slow = 0
        slow_cross_over_fast = 0

        for i in range(len(slow_sma)):
            if i == 0:
                continue
            elif (fast_sma[i] > slow_sma[i] and fast_sma[i-1] < slow_sma[i-1]):
                fast_cross_over_slow += 1
            elif (fast_sma[i] < slow_sma[i] and fast_sma[i-1] > slow_sma[i-1]):
                slow_cross_over_fast += 1
        return fast_cross_over_slow, slow_cross_over_fast

    def get_cross_over_data(self):
        """
        Get the data for the crossover points
        """
        fast_sma, slow_sma = self.calculate_moving_averages()
        x1, y1, x2, y2 = [], [], [], []

        for i in range(len(slow_sma)):
            if i == 0:
                continue
            elif (fast_sma[i] > slow_sma[i] and fast_sma[i-1] < slow_sma[i-1]):
                x1.append(i)
                y1.append(fast_sma[i])
            elif (fast_sma[i] < slow_sma[i] and fast_sma[i-1] > slow_sma[i-1]):
                x2.append(i)
                y2.append(fast_sma[i])

        return x1, y1, x2, y2

    def plot_moving_average_crossover(self):
        """
        Plot the moving average crossover
        """
        fast_sma, slow_sma = self.calculate_moving_averages()
        data = self.get_data()
        x1, y1, x2, y2 = self.get_cross_over_data()
        plt.plot(data[self.var], label=self.var)
        plt.plot(fast_sma, label='Fast SMA')
        plt.plot(slow_sma, label='Slow SMA')
        plt.title('Moving Average Crossover')

        plt.scatter(x1, y1, c='red', label="Fast SMA crossed over Slow SMA")
        plt.scatter(x2, y2, c='blue', label="Slow SMA crossed over Fast SMA")

        plt.legend()
        plt.show()