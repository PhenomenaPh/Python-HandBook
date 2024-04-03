import pandas as pd
import numpy as np


def discount(data: pd.DataFrame) -> pd.DataFrame:
    new_data = data.copy(deep=True)

    new_data["cost"] = np.where(
        new_data["number"] > 2,
        new_data["cost"] * 0.5,
        new_data["cost"],
    )

    return new_data


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


products = ["bread", "milk", "soda", "cream"]
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
with_discount = discount(result)
print(result)
print(with_discount)
