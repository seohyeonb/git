def exchange(receivem):
  n500=receivem//500
  receivem%=500
  n100=receivem//100
  receivem%=100
  n50=receivem//50
  receivem%=50
  n10=receivem//10
  receivem%=10
  print('500원 동전의 개수:',n500)
  print('100원 동전의 개수:',n100)
  print('50원 동전의 개수:',n50)
  print('10원 동전의 개수:',n10)

def get_integer(prompt):
  res =int(input(prompt))
  return res;


money=get_integer('동전으로 교환하고자 하는 금액은?:')
exchange(money)
