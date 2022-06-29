tupMat = [[(7, 2, 6), (4, 1, 5)], [(9, 2, 6), (4, 5, 3)]]
additionVals = [3, 2]
print("Elements of Tuple matrix initially :" + str(tupMat))
addTupMat = [[sub + (additionVals[i], ) for sub in ele] for i, ele in enumerate(tupMat)]
print("Elements of Tuple matrix after addition :" + str(addTupMat))
