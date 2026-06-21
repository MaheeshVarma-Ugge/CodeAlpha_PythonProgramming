import csv
from datetime import date

STOCK_PRICES = {
    "AAPL": 187.50,"TSLA": 248.00,"GOOGL": 172.30,"MSFT": 415.20,"AMZN": 189.90,"NVDA": 875.40,"META": 502.10,"NFLX": 635.80,"AMD": 158.60,"INTC": 31.20,
}

# Display available stocks
def display_available_stocks():
    print("\nAvailable Stocks")
    print("-" * 30)
    for name, price in STOCK_PRICES.items():
        print(f"{name:<10} : ${price:.2f}")
    print("-" * 30)

# Add new stock dynamically
def add_new_stock():
    name = input("Enter new stock name: ").upper()
    if name in STOCK_PRICES:
        print("Stock already exists!")
        return
    try:
        price = float(input("Enter stock price: "))
        STOCK_PRICES[name] = price
        print(f"{name} added successfully!")

    except ValueError:
        print("Invalid price!")
# Portfolio input
def get_portfolio():
    portfolio = {}
    while True:
        print("\n1. View Stocks")
        print("2. Add New Stock")
        print("3. Buy Stock")
        print("4. Finish")

        choice = input("Choose Option Using S.NO: ").strip()

        # View Stocks
        if choice == "1":
            display_available_stocks()

        # Add New Stock
        elif choice == "2":
            add_new_stock()

        # Buy Stock
        elif choice == "3":
            name = input("Enter stock name: ").upper()

            if name not in STOCK_PRICES:
                print("Stock not found!")
                continue
            try:
                qty = int(input("Enter quantity: "))
                if qty <= 0:
                    print("Quantity must be positive!")
                    continue
                investment_value = STOCK_PRICES[name] * qty
                print(f"\nInvestment Amount = ${investment_value:.2f}")
                confirm = input("Confirm investment? (yes/no): ").lower()

                # YES CONDITION
                if confirm == "yes" or confirm == "y":
                    portfolio[name] = portfolio.get(name, 0) + qty
                    total_value = STOCK_PRICES[name] * portfolio[name]

                    print("Investment Success.")
                    print(f"{name} added to portfolio.")
                    print(f"Current Value: ${total_value:.2f}")

                # NO CONDITION
                elif confirm == "no" or confirm == "n":
                    print("Investment cancelled.")

                # INVALID INPUT
                else:
                    print("Invalid input!")

            except ValueError:
                print("Invalid quantity!")

        # Finish
        elif choice == "4":
            break

        else:
            print("Invalid option!")

    return portfolio

# Portfolio summary
def display_summary(portfolio):
    if not portfolio:
        print("\nNo stocks purchased.")
        return 0

    total = 0

    print("\nPortfolio Summary")
    print("-" * 50)
    print(f"{'Name':<10}{'Price':<10}{'Qty':<10}{'Value':<10}")

    for name, qty in portfolio.items():
        price = STOCK_PRICES[name]
        value = price * qty
        total += value

        print(f"{name:<10}${price:<9.2f}{qty:<10}${value:<10.2f}")

    print("-" * 50)
    print(f"Total Investment Value = ${total:.2f}")

    return total

# Save to CSV
def save_to_csv(portfolio, total):
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Price", "Quantity", "Value"])

        for name, qty in portfolio.items():
            price = STOCK_PRICES[name]
            value = price * qty

            writer.writerow([name, price, qty, value])

        writer.writerow([])
        writer.writerow(["Total Investment", total])

    print("Portfolio saved to portfolio.csv")

# Main function
def main():
    print("=== Stock Portfolio Tracker ===")

    portfolio = get_portfolio()
    total = display_summary(portfolio)

    save = input("\nSave portfolio to CSV? (yes/no): ").lower()

    if save == "yes" or save == "y":
        save_to_csv(portfolio, total)

    print("\nThank You!")
if __name__ == "__main__":
    main()