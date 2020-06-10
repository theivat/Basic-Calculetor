""" ASCII VALU OF 
* = 42
+ = 43
- = 45
/ = 47
^ = 94
"""
print("You Can Do Addition , Subtraction , Multiplication , Division And Powers")
a=int(input("First Number = "))
b=input("Operation = ")
c=int(input("Second Number = "))
d=ord(b)
if d == 42:
    e=a*c
    print("Your Answer=",e)
elif d == 43:
    e = a+c
    print("Your Answer=",e)
elif d == 45:
    e = a-c
    print("Your Answer=",e)
elif d == 47:
    e = a/c
    print("Your Answer=",e)
elif d == 94:
    e = a**c
    print("Your Answer=",e)
else:
    print("You Enter Some Wrong Details")