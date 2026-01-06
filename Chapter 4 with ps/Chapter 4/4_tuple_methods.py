a=(1,45,342,4343,45,False,"rohan","shivam")
print(a)
no=a.count(45)
print(no)

tup = (1, 2, 3, 2, 4, 2, 5)
print(tup.count(2))   # Output: 3
print(tup.count(5))   # Output: 1
print(tup.count(10))  # Output: 0


tup = (10, 20, 30, 20, 40)

print(tup.index(20))   # Output: 1 (first occurrence)
print(tup.index(40))   # Output: 4
# print(tup.index(100))  # ❌ Raises ValueError


print(len(a))
