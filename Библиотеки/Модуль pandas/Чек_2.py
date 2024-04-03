import pandas as pd


products = ["bread", "milk", "soda", "cream"]
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)


def cheque(purchase_list, **purchases) -> pd.DataFrame:
    data = [
        {
            "product": product,
            "price": purchase_list[product],
            "number": quantity,
            "cost": purchase_list[product] * quantity,
        }
        for product, quantity in purchases.items()
    ]

    df = pd.DataFrame(data)

    df.sort_values(by=["product"], inplace=True)

    return df.reset_index(drop=True)


result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
