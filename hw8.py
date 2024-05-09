shopping_bag={}
print('>>구입<<')
def buy(shopping_bag):
  while True:
    item=input('상품명?')
    if item=='':
      break
    num=input('수량?')
    
    shopping_bag[item]=num
    print(f'장바구니에 {item}이 {num}개 담겼습니다.\n')


def show(shopping_bag):
  print('장바구니 보기:',end='')
  print(shopping_bag)

def find(shoppiong_bag):
  res=input('장바구니에서 확인하고자 하는 상품은?')
  if res in shopping_bag:
    print(f'{res}는 장바구니에 {shopping_bag[res]}개 있습니다')
  else:
    print(f'{res}는 장바구니에 없습니다')


buy(shopping_bag)
show(shopping_bag)
find(shopping_bag)

