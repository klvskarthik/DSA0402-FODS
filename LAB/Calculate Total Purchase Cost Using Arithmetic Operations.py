prices = [100, 200, 150]
quantities = [2, 1, 3]
discount = 10
tax = 5

subtotal = sum(p * q for p, q in zip(prices, quantities))
discount_amount = subtotal * discount / 100
after_discount = subtotal - discount_amount
tax_amount = after_discount * tax / 100
total = after_discount + tax_amount

print("Subtotal:", subtotal)
print("Discount:", discount_amount)
print("Tax:", tax_amount)
print("Total Cost:", total)
