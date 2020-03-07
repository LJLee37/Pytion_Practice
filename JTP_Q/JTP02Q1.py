score = {
    "Korean" : 80,
    "English" : 75,
    "Math" : 55
}
num = 0
for i in score.values():
    num += i
print(num/len(score))