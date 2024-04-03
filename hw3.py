import module
rate=int(input('할인율은?'))
module.set_rate(rate)

beforeprice1=int(input('A 상품의 할인된 가격은?'))
beforeprice2=int(input('B 상품의 할인된 가격은?'))
print('A 상품의 정가는',module.to_beforeprice(beforeprice1),'원')
print('B 상품의 정가는',module.to_beforeprice(beforeprice2),'원')

