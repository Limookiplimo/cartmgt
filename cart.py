import pathlib
import toml

terms_path = pathlib.Path(__file__).parent / "terms.toml"
cart_data = toml.loads(terms_path.read_text())

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

        receipt = f"  {item}: \n  Quantity - {cart_quantity}, UnitPrice - {item_price}, UnitPrice - {discount}, TotalPrice - {total_amount}"
        print(receipt)

    print(remarks)

print_receipt()
