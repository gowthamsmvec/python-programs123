def Findel(tup,K):
    result = []
    test_tup = list(tup)
    temp = sorted(tup)
    for i, val in enumerate(temp):
        if i < K or i >= len(temp) - K:
            result.append(val)
    result = tuple(result)
    # printing result 
    print("Max and Min K elements : ",result)

tup = (13, 10, 23, 2, 5, 6, 12)
K = 2
print("The original tuple: ", tup)
Findel(tup,K)
