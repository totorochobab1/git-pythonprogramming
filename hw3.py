def get_fixed_price(discount_rate, discount_price):
    original_price = discount_price / (1 - discount_rate / 100)
    return original_price

discount_rate = int(input("할인율은? "))
discount_price_A = int(input("A 상품의 할인된 가격은? "))
discount_price_B = int(input("B 상품의 할인된 가격은? "))

original_price_A = get_fixed_price(discount_rate, discount_price_A)
original_price_B = get_fixed_price(discount_rate, discount_price_B)

print("A 상품의 정가는", int(original_price_A),"원")
print("B 상품의 정가는 ",int(original_price_B), "원")