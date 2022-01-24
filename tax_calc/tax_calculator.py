def calculate_tax(price):
    """takes price in cent returns the 0.19 vat amount also in cents, negative ints return None"""
    if price < 0:
        return None
    else:
        return round(price * 0.19)