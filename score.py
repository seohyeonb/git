import pickle
filepath='example.bin'

def input_scores():
    s=[]
    i=1
    while True:
        n=int(input(f'#{i}? '))
        if n<0:
            break
        s.append(n)
        i+=1
    return s
def get_average(s):
    total=0
    for n in s:
        total+=n
    return total/len(s)

def show_scores(s):
    for n in s:
        print(n,end='')

print('점수입력')
scores=input_scores()

print('\n점수출력\n개인점수:',end=' ')
show_scores(scores)
avg=get_average(scores)
print(f'\n평균: {avg}')
