def memory1(num):
  for n in range(2,6):
    print(f'{n}x{num}={num*n:2d}',end='  ')

def memory2(num):
  for n in range(6,10):
    print(f'{n}x{num}={num*n:2d}',end='  ')
    
def arrange1(num):
  while num<=9:
    memory1(num)
    print('\n',end='')
    num+=1


def arrange2(num):
  while num<=9:
    memory2(num)
    print('\n',end='')
    num+=1
  

arrange1(1)
print('\n')
arrange2(1)
