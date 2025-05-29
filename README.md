# 📈 Stock Analysis Tool with Recommendation Score

This is a command-line Python tool that analyzes historical stock data using the [Yahoo Finance](https://finance.yahoo.com/) API via the [`yfinance`](https://github.com/ranaroussi/yfinance) library. It computes key statistics and generates a simple recommendation score based on historical price positioning.

---

## 🔧 Features

- Download historical stock data using a ticker and time period
- Calculate descriptive statistics: mean, median, standard deviation, min/max
- Identify day-of-week performance patterns
- Compute a basic "Recommendation Score" based on how the current price compares to historical medians
- Command-line interface with ticker and time period options

---

## 🚀 Usage

### 1. Clone the repository

```bash
git clone https://github.com/amf585/stock-dayofweek-trends
cd stock-dayofweek-trends
```

### 2. Install dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

> **Requirements:**
> - `yfinance`
> - `pandas`
> - `matplotlib`
> - `numpy`

Or install them manually:

```bash
pip install yfinance pandas numpy
```

### 3. Run the script

```bash
python3 stock_analysis-with-rec.py --ticker MSFT --period 5y
```

**Arguments:**

| Flag         | Description                              | Example        |
|--------------|------------------------------------------|----------------|
| `--ticker`   | Stock ticker symbol (e.g., AAPL, MSFT)   | `--ticker AAPL`|
| `--period`   | Time period for historical data          | `--period 5y`  |

> Valid period formats: `1d`, `5d`, `1mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max`.

---

## 📌 Output Example

### Text Recommendation: stock-dayofweek-trends/output/MSFT_1y_May-01-2025_09-46-29_AM_log.txt

Stock Ticker: MSFT
Data Period: 1y
Data Source: Yahoo Finance

Metric Explanations:
- Average Return: Mean daily return by day of week
- Median Return: Median daily return by day of week
- Standard Deviation: Volatility of return on each weekday
- Volatility: Std Dev divided by abs(mean), to standardize
- Buy/Sell Score: (Median + Average Return) / Volatility
  Higher score = potentially better day to buy (stronger returns, more consistent)

=== Metrics by Day ===
           Average Return  Median Return  Standard Deviation  Volatility  Buy/Sell Score
DayOfWeek                                                                               
Monday          -0.001356      -0.000644            0.012075    8.905831       -0.000225
Tuesday          0.002678       0.003920            0.011379    4.249132        0.001553
Wednesday        0.004435       0.003096            0.021121    4.762561        0.001581
Thursday        -0.002467      -0.001331            0.022177    8.990508       -0.000422
Friday          -0.000616       0.001109            0.013130   21.306591        0.000023

Best Day to Buy: Wednesday (Highest Buy/Sell Score)
Recent 4 Prices on Buy Day:
            Share Price
Date                   
2025-04-09   390.489990
2025-04-16   371.609985
2025-04-23   374.390015
2025-04-30   395.260010

Best Day to Sell: Thursday (Lowest Buy/Sell Score)
Recent 4 Prices on Sell Day:
            Share Price
Date                   
2025-04-10   381.350006
2025-04-17   367.779999
2025-04-24   387.299988
2025-05-01   434.230011

📈 Recommendation Score for this week: 3.0/10


### Chart: stock-dayofweek-trends/output/MSFT_1y_May-01-2025_09-46-29_AM_metrics.png
![MSFT May 1st, 2025 analysis results for 1 year period](https://file%2B.vscode-resource.vscode-cdn.net/Users/andrewfagan/Desktop/Projects/python/stock-dayofweek-trends/output/MSFT_1y_May-01-2025_09-46-29_AM_metrics.png?version%3D1748533065829)

---

## ⚠️ Troubleshooting

### 🛑 Yahoo Rate Limit Error

If you see:

```bash
YFRateLimitError: Too Many Requests. Rate limited.
```

Try:
- Switching to a different network or IP (e.g., mobile hotspot, VPN)
- Using the `.history()` method instead of `.download()` in the script
- Waiting a few hours or days before retrying
- Updating `yfinance`:  
  ```bash
  pip install --upgrade yfinance
  ```

---

## 🧠 How the Recommendation Score Works

The tool compares the current price to historical metrics:

- ✅ **Strong Buy** if price is significantly below the median
- ⚖️ **Hold** if price is around the average
- 🚫 **Sell** if price is far above historical norms

> This is a basic statistical approach and **not** financial advice.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- [Yahoo Finance](https://finance.yahoo.com/) via `yfinance`
- `pandas`, `matplotlib` and `numpy` for data manipulation/display