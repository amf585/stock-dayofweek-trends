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
pip install yfinance pandas matplotlib numpy 
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

<img width="476" alt="Screen Shot 2025-05-29 at 8 59 02 AM" src="https://github.com/user-attachments/assets/deecc3f3-eed0-4b1c-bbe4-b24c93e833c0" />

### Chart: stock-dayofweek-trends/output/MSFT_1y_May-01-2025_09-46-29_AM_metrics.png

![MSFT_1y_May-01-2025_09-46-29_AM_metrics](https://github.com/user-attachments/assets/2cf6dd99-1b0b-4505-8280-e31997179a75)

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
