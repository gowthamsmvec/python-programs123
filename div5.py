
my_list = [12, 65, 54, 35, 102, 330, 221,]

result = list(filter(lambda x: (x % 5 == 0), my_list))

print("Numbers divisible by 5 are",result)
