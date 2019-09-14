from moduleTester import square
print("variables")
myvar = 1
print(f"Variable myvar : {myvar} is an {type(myvar)}")
print("Done Practicing Variables")

print("Hello Word") # Display a message
myname = input("state your name: ")
print("Hello " + str(myname))
print("Hello %s" % myname)


i = 120
print(f"i equals {i}")
f = 1.6180339
print(f"f equals {f} and is a {type(f)}")
b = True
print(f"b equals {b}")
n = None
print(f"n equals  {n}")
# tuple
c = (10,20,10)
print(f" c[0] equals {c[0]} and is an : {type(c)}")

l = ["George", "timmy", "Doom"]
l = [10,20,30]
print(f" l[0] has equals {l[0]} and is a: {type(l)}")
# Sets variables.
s = set()
s.add(1)
s.add(4)
s.add(6)
print("the numbers are %s" % s)
# Dictionary
grades = {"jimmy" : "B+", "george": "A+"}
grades["jimmy"] = "b";
grades["Anna"] = "F"

mydictionary = dict()

x=10
if (x > 0):
    print("%s is a positive number" % x)
elif (x<0):
    print("%s is a negative number" % x)
else:
    print("%s equals zero" % x)


for i in range(5):
    print(i)
for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}" )


def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False


print(square(100))
