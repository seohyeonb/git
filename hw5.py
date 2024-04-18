def read_single_digit(num1):
    if num1 == 1:
        return '일'
    elif num1 ==2:
        return '이'
    elif num1 == 3:
        return '삼'
    elif num1 ==4:
        return '사'
    elif num1 ==5:
        return '오'
    elif num1 ==6:
        return '육'
    elif num1 ==7:
        return '칠'
    elif num1 ==8:
        return '팔'
    elif num1 ==9:
        return '구'

def read_number(num2,num3,num4):
    read_single_digit(num2)
    return num2
    read_single_digit(num3)
    return num3
    read_single_digit(num4)
    return num4

answer1=int(input('세자리 정수 입력'))
read_single_digit(answer1)
read_single_digit(answer2)
read_single_digit(answer3)
