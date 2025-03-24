def get_integer(prompt):
    return int(input(prompt))

def exchange(amount):
    coin_500 = amount//500
    amount %= 500 
    coin_100 = amount //100
    amount %= 100 
    coin_50 = amount //50
    amount %= 50 
    coin_10 = amount //10
    print("500원 동전의 개수: " , coin_500)
    print("100원 동전의 개수: " , coin_100)
    print("50원 동전의 개수: " , coin_50)
    print("10원 동전의 개수: ",coin_10)


money = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(money)
