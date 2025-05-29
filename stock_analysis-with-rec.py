import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
from datetime import datetime

# Argument parsing
parser = argparse.ArgumentParser(description="Analyze historical stock trends by day of the week.")
parser.add_argument('--ticker', type=str, required=True, help='Stock ticker (e.g. AAPL)')
parser.add_argument('--period', type=str, default='5y', help='Data period (e.g. 1y, 2y, 5y, max)')
args = parser.parse_args()
ticker = args.ticker.upper()
period = args.period

# Download stock data (auto_adjust=True is now the default in yfinance)
stock_data = yf.download(ticker, period=period)

if stock_data.empty:
    print(f"No data found for {ticker} with period '{period}'. Please check the ticker or try a different period.")
    exit(1)

# Use 'Adj Close' if available, else fallback to 'Close'
close_col = 'Adj Close' if 'Adj Close' in stock_data.columns else 'Close'
stock_data['DailyReturn'] = stock_data[close_col].pct_change()

# Add day of week column
stock_data['DayOfWeek'] = stock_data.index.day_name()

# Group by day of week
grouped = stock_data.groupby('DayOfWeek')['DailyReturn']

# Order of weekdays
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Calculate metrics
metrics = {
    'Average Return': grouped.mean(),
    'Median Return': grouped.median(),
    'Standard Deviation': grouped.std(),
    'Volatility': grouped.std() / (grouped.mean().abs() + 1e-9)  # add epsilon to avoid divide by zero
}

# Normalize and calculate buy/sell score
normalized = pd.DataFrame(metrics)
normalized = normalized.reindex(days_order)

# Buy score = (Median Return + Avg Return) / Volatility
normalized['Buy/Sell Score'] = (normalized['Median Return'] + normalized['Average Return']) / (normalized['Volatility'] + 1e-9)

# Identify Best Day to Buy (highest Buy/Sell Score) and Best Day to Sell (lowest Buy/Sell Score)
best_day_to_buy = normalized['Buy/Sell Score'].idxmax()
best_day_to_sell = normalized['Buy/Sell Score'].idxmin()

# Get recent median prices for best buy/sell days
def get_recent_medians(df, day_name, close_column, weeks=4):
    recent_days = df[df['DayOfWeek'] == day_name].tail(weeks)
    recent_days = recent_days[[close_column]]
    recent_days.columns = ['Share Price']
    recent_days.index = pd.to_datetime(recent_days.index)
    return recent_days

buy_day_prices = get_recent_medians(stock_data, best_day_to_buy, close_col)
sell_day_prices = get_recent_medians(stock_data, best_day_to_sell, close_col)

# Calculate the recommendation score based on Buy/Sell Score and other factors
def calculate_recommendation_score():
    score = 5.0
    buy_score = normalized.loc[best_day_to_buy, 'Buy/Sell Score']
    volatility = normalized.loc[best_day_to_buy, 'Volatility']
    current_price = stock_data[close_col].iloc[-1]  # Get the last value, ensure it's a scalar

    # Ensure median price is extracted as a scalar value (if it is still a Series)
    median_price = buy_day_prices['Share Price'].iloc[0]  # Use .iloc[0] to get the first entry as scalar

    # If it's a Series or something else, use .values[0] or .item()
    current_price = current_price.item() if isinstance(current_price, pd.Series) else current_price
    median_price = median_price.item() if isinstance(median_price, pd.Series) else median_price

    # Conditional checks
    if buy_score > 0.01:
        score += 2
    elif buy_score < 0:
        score -= 2

    if volatility < 0.02:
        score += 1
    elif volatility > 0.05:
        score -= 1

    if current_price < median_price:
        score += 1
    else:
        score -= 1

    return round(max(1, min(score, 10)), 1)

recommendation_score = calculate_recommendation_score()

# Output paths
timestamp = datetime.now().strftime('%b-%d-%Y_%I-%M-%S_%p')
base_filename = f"{ticker}_{period}_{timestamp}"
export_dir = os.path.join(os.getcwd(), "output")
os.makedirs(export_dir, exist_ok=True)

chart_path = os.path.join(export_dir, f"{base_filename}_metrics.png")
log_path = os.path.join(export_dir, f"{base_filename}_log.txt")

# Save chart
# Normalize values for visualization only
plot_data = normalized[["Average Return", "Median Return", "Standard Deviation", "Volatility", "Buy/Sell Score"]]
plot_data_normalized = (plot_data - plot_data.min()) / (plot_data.max() - plot_data.min())

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
plot_data_normalized.plot(kind='bar', ax=ax)
plt.title(f"{ticker} ({period}) - Normalized Metrics")
plt.ylabel("Normalized Metric Value (0–1)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(chart_path)
plt.close()

# Save log file with explanations and best days
with open(log_path, 'w') as f:
    f.write(f"Stock Ticker: {ticker}\n")
    f.write(f"Data Period: {period}\n")
    f.write(f"Data Source: Yahoo Finance\n\n")

    f.write("Metric Explanations:\n")
    f.write("- Average Return: Mean daily return by day of week\n")
    f.write("- Median Return: Median daily return by day of week\n")
    f.write("- Standard Deviation: Volatility of return on each weekday\n")
    f.write("- Volatility: Std Dev divided by abs(mean), to standardize\n")
    f.write("- Buy/Sell Score: (Median + Average Return) / Volatility\n")
    f.write("  Higher score = potentially better day to buy (stronger returns, more consistent)\n\n")

    f.write("=== Metrics by Day ===\n")
    f.write(normalized.to_string())
    f.write("\n\n")

    f.write(f"Best Day to Buy: {best_day_to_buy} (Highest Buy/Sell Score)\n")
    f.write("Recent 4 Prices on Buy Day:\n")
    f.write(buy_day_prices.to_string())
    f.write("\n\n")

    f.write(f"Best Day to Sell: {best_day_to_sell} (Lowest Buy/Sell Score)\n")
    f.write("Recent 4 Prices on Sell Day:\n")
    f.write(sell_day_prices.to_string())
    f.write("\n")

    f.write(f"\n📈 Recommendation Score for this week: {recommendation_score}/10")

print(f"\n✅ Analysis complete! Results saved to:\n- Chart: {chart_path}\n- Log: {log_path}")