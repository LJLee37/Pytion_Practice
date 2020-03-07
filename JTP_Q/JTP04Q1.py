def is_odd(x):
    if x % 2 == 0:
        return True
    else:
        return False

a = int(input())
if is_odd(a):
    print("짝수 입니다")
else:
    print("홀수 입니다")
    