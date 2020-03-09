import random

def lotto_generator():
    lotto_number = []
    while len(lotto_number) != 7:
        new_number = random.randrange(1, 46)
        if new_number not in lotto_number:
            lotto_number.append(new_number)
    return lotto_number

print("----------로또 번호 생성기 입니다----------")
temp = input("로또 번호를 생성하시겠습니까? Y/N :")
while True:
    if temp == "Y":
        Lotto = lotto_generator()
        print(Lotto)
        temp = input("다시 생성하시겠습니까? Y/N :")
    elif temp == "N":
        print("로또 번호 생성기를 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 시도해 주십시오.")
        temp = input("로또 번호를 생성하시겠습니까? Y/N :")b

