## calculate and apply tax
def calculate_total(prices):
    return sum(prices)

def apply_tax(amount):
    final_amount = lambda x: x + (x * 0.05)
    return final_amount(amount)