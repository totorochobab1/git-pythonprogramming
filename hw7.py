shopping_bag=[] 
d={}
print('[구입]')
while True:
    item=input('상품명?')
    if len(item)==0:
        print()
        print(f'>>> 장바구니 보기: {d}')
        break
    else:
        shopping_bag.append(item)
        q=int(input('수량은?'))
        d[item]=q
        print(f'장바구니에 {item} {d[item]}개가 담겼습니다.')
        print()
print('\n[검색]')
s=input('장바구니에서 확인하고자 하는 상품은?')
print(f'{s}은(는) {d[s]}개 담겨 있습니다.')
