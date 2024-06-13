import os
import pickle
from datetime import datetime

class Time:
    def __init__(self,hour=0,minute=0):
        self.hour=hour
        self.minute=minute
def display(self):
        print(f"{self.hour:02d}:{self.minute:02d}")
        
def get_current_time():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    return Time(hour, minute)


def save_time(time):
    with open(lastdat.txt, 'wb') as file:
        pickle.dump(time, file)


def load_time(filename):
    with open(filename, 'rb') as file:
        t = pickle.load(file)
    return t


if os.path.exists(filename):
    t = load_time(filename)
    print(f'안녕하세요, 마지막으로 {t.toString()}에 실행되었습니다')
else:
    print('안녕하세요, 처음 실행되었습니다')

t=get_current_time()
print(f'지금은 {t}입니다')
save_time(t,filename)
