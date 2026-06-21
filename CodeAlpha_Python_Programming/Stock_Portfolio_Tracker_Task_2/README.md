# Task 2 - Stock Portfolio Tracker

## Overview
A console-based Stock Portfolio Tracker that lets the user browse a list of stocks with mock prices, add new custom stocks, "buy" shares to build a portfolio, view a summary of holdings, and export the final portfolio to a CSV file.

## How It Works
The program runs an interactive menu loop with four options:
1. **View Stocks** - Displays all available stocks and their prices.
2. **Add New Stock** - Lets the user add a custom stock with a name and price.
3. **Buy Stock** - Lets the user choose a stock and quantity, calculates the investment amount, and asks for confirmation before adding it to the portfolio.
4. **Finish** - Ends the buying loop and proceeds to the summary.

After finishing:
- A **Portfolio Summary** table is displayed showing each stock's price, quantity held, and total value, along with the overall total investment value.
- The user is asked whether to save the portfolio to a CSV file (`portfolio.csv`).

## File
- `Task2.py` - Main script.

## How to Run
```bash
python Task2.py
```

## Sample Output
```
=== Stock Portfolio Tracker ===

1. View Stocks
2. Add New Stock
3. Buy Stock
4. Finish
Choose Option Using S.NO: 1

Available Stocks
------------------------------
AAPL       : $187.50
TSLA       : $248.00
...
```

## Output File
- `portfolio.csv` - Generated when the user chooses to save, containing stock name, price, quantity, value, and total investment.

## Notes
- Stock prices are stored in a predefined dictionary (`STOCK_PRICES`) and can be extended at runtime via the "Add New Stock" option.
- Input validation handles invalid prices, quantities, and menu choices.
- Uses Python's built-in `csv` and `datetime` modules; no external dependencies.
