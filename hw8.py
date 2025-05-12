def buy(shopping_bag):
    print('[구입]')
    item = input('상품명?')
    if item == '':
        return False
    q = int(input('수량은?'))
    shopping_bag.append(item)  
    d[item] = q               
    print(f'장바구니에 {item} {d[item]}개가 담겼습니다.\n')
    return True

def show(shopping_bag):
    print(f'\n>>> 장바구니 보기: {d}')

def find(shopping_bag):
    print('\n[검색]')
    s = input('장바구니에서 확인하고자 하는 상품은?')
    if s in d:
        print(f'{s}(는) {d[s]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {s}은(는) 없습니다.')


shopping_bag = []  
d = {}             

while True:
    if buy(shopping_bag) == False :  
        break

show(shopping_bag)
find(shopping_bag)