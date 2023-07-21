import pathlib
import toml

terms_path = pathlib.Path(__file__).parent / "terms.toml"
terms = toml.loads(terms_path.read_text())

def discounted_prices(item, quantity):
    if item in terms:
        item_terms = terms[item]["terms"]
        for term in item_terms:
            if eval(f"{quantity} >= {term['size']}"):
                return (1 - term['discount'] / 100) * quantity
    return quantity

def get_items():
    stocks = {"fat": 1000, "flour": 1000}
    cart = {"fat": 15, "flour": 100}
    price = {"fat": 1950, "flour": 2100}
        
    metadata = f"\n Hustler Wholesalers \n Customer Name: Your Name \n"
    print(metadata)
    for item, stock_quantity in stocks.items():
        cart_quantity = cart.get(item, 0)
        cart_quantity = min(cart_quantity, stock_quantity)
        total_price = cart_quantity * price[item]


        # Apply sales terms
        discounted_quantity = discounted_prices(item, cart_quantity)
        discounted_price = round(discounted_quantity * price[item])
        discount = round(total_price - discounted_price)

        remarks = f" \n You were served by: Limoo"
        receipt = f"  {item}: \n  Quantity - {cart_quantity}, Discount - {discount}, Price - {discounted_price}"

        print(f"{receipt}")
    print(remarks)

def apply_terms(path):
    global terms
    terms_info = toml.loads(path.read_text())
    terms = { **terms, **terms_info}

apply_terms(terms_path)
get_items()



