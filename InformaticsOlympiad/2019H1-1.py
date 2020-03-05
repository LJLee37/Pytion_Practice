
a = int(input())
b = int(input())
Answer = []
flag = False
for x in range (-100, 101):
    for y in range(-100, 101): # -100 <= x,y <= 100
        if (a * x + b * y) == 48:
            flag = True
            Answer.append(x)
            Answer.append(y)
print(flag)
if flag:
    print(Answer)
