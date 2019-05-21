# Swap variables
# Re declare variables
# Delete variables
x = 10
y = 20

print("x, y before swapping :", x, y)

x,y = y,x

y=100
print("x, y after swapping :", x, y)

del y

print("x, y after swapping :", x, y)