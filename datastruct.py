#List
print("\n----- LIST -----\n")
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]

print("List 1 :", list1)
print("List 2 :", list2)

list1.pop(3)
list2.append(50)
list3 = list1+list2

print("\nList 1 :", list1)
print("List 2 :", list2)
print("List 3 :", list3)

print("\nSome elements in lists")
print("List 1 2nd element :", list1[1])
print("List 2 4th element :", list2[3])
print("List 3 6th element :", list3[5])
print("List 3 elements from index 2 to 7 :", list3[2:8])


#Tuple
print("\n----- TUPLE -----\n")
tuple1 = (2, 4, 6, 8, 10)
tuple2 = (3, 6, 9, 12, 15, 18)

print("Tuple 1 :", tuple1)
print("Tuple 2 :", tuple2)

print("\nTuple 1 last element :", tuple1[-1])
print("Tuple 2 last 3 elements :", tuple2[-3:])


#Dictinary
print("\n----- DICTIONARY -----\n")

dict1 = { "one":1, "two":2, "three":3 }
dict2 = { "plus":"+", "minus":"-", "divide":"/" }

print("Dict 1 :", dict1)
print("Dict 2 :", dict2)

del dict1["two"]
dict2.pop("plus")

print("\nDictionary elements after deletion")
print("Dict 1 :", dict1)
print("Dict 2 :", dict2)
