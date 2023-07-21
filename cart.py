import pathlib
import toml
from string import ascii_lowercase

terms_path = pathlib.Path(__file__).parent / "terms.toml"
cart_data = toml.loads(terms_path.read_text())

def prepare_catalog():
    print("Available Stock: ")
    for item, data in cart_data.items():
        if item == "meta":
            continue

        stock = data.get("stock", 0)
        price = data.get("price", 0)
        catalogue = f" {item}: \n Stock - {stock}, Price - {price} \n" 
        print(catalogue)


def add_to_cart(cart_data, num_cart=1):
    cart = {}
    item_choices = dict(zip(ascii_lowercase, cart_data))
    for code, choice in item_choices.items():
        print(f"{code}){choice}")

    while True:
        chosen_code = " " if num_cart == 1 else f"s (choose max {num_cart})"
        choice = input(f"\nchoice{chosen_code}? ")
        cart_items = set(cart.replace(",", " ").split())

        if len(cart_items) != num_cart:
            chosen_code = " " if num_cart == 1 else f"s , separated by comma"
            print(f"Please pick {num_cart}choices{chosen_code}")
            continue
        if any((invalid := choice) not in item_choices for choice in cart_items):
            print(
                f"{invalid!r} does not exist"
                f"Available items are {','.join(item_choices)}"
            )
            continue
        
        return [item_choices[choice] for choice in cart_items]


def discounted_prices(item, quantity, price):
    if item in cart_data and "terms" in cart_data[item]:
        item_terms = cart_data[item]["terms"]
        for term in item_terms:
            if eval(f"{quantity}{term['size']}"):
                return price * (1 - term['discount'] / 100)
    return price


def print_receipt():
    metadata = f"\n Hustler Wholesalers \n Customer Name: Your Name \n"
    print(metadata)

    remarks = f" \n You were served by: Limoo"

    billed = 0
    for item, item_data in cart_data.items():
        if item == "meta":
            continue
            
        stock_quantity = item_data.get("stock", 0)
        cart_quantity = item_data["cart"].get("quantity", 0)
        cart_quantity = min(cart_quantity, stock_quantity)
        item_price = item_data.get("price", 0)
        orignal_amount = cart_quantity * item_price

        # Apply sales terms
        discounted_price = discounted_prices(item, cart_quantity, item_price)
        total_amount = discounted_price * cart_quantity
        discount = orignal_amount - total_amount

        billed += total_amount
        receipt = f"  {item}: \n  Quantity - {cart_quantity}, UnitPrice - {item_price}, Discount - {discount}, TotalPrice - {total_amount}"
        print(receipt)

    print(f"\n Total Bill: {billed}")
    print(remarks)
