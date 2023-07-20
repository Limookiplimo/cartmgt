import pathlib
import toml

terms_path = pathlib.Path(__file__).parent / "terms.toml"
terms = toml.loads(terms_path.read_text())

def get_items():
    stocks = {"fat": 1000, "flour": 1000}
    cart = {"fat": 15, "flour": 100}
    price = {"fat": 1950, "flour": 2100}

    for i, s in stocks.items():
        cart_quantity = cart.get(i, 0)
        if cart_quantity > s:
            cart_quantity = s
        total_price = cart_quantity * price[i]
        print(f"{i}: Quantity - {cart_quantity}, Price - {total_price}")

get_items()


