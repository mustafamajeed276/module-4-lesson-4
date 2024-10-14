import array as arr
arraynum = arr.array("i", [1, 2, 3, 4, 5, 3, 2, 3, 7 ,3])
print("orignal array : "+str(arraynum))
print("number of times three has occured in the said array : "+str(arraynum.count(3)))
arraynum.reverse()
print("reverse order of array")
print(str(arraynum))