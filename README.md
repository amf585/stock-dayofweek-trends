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

Create a virtual environment (optional):

```bash
python3 -m venv venv
source venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

> **Requirements:**
> - `yfinance`
> - `pandas`
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

```bash
[*********************100%***********************]  1 of 1 completed

--- Stock Analysis for MSFT (5y) ---
Latest Price: $314.27
Mean: $260.41
Median: $273.91
Std Dev: $47.24
Max: $366.78
Min: $133.19

Day of Week Performance:
  Monday: Mean $251.11
  Tuesday: Mean $263.87
  ...

Recommendation Score: 4/5 - Strong Buy
```

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
- `pandas` and `numpy` for data manipulation