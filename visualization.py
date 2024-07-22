import matplotlib.pyplot as plt
import pandas as pd

def plot_expenses(expense_data):
    df = pd.read_csv(expense_data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum().plot(kind='bar')
    plt.title('Monthly Expenses')
    plt.xlabel('Month')
    plt.ylabel('Total Amount')
    plt.show()

if __name__ == "__main__":
    plot_expenses('data/expense_data.csv')
