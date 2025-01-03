#Given three points ( x 1,y1) ( x 2,y2) and ( x 3,y3) write a program to check if all the three points fall on one straight line

"""x1=int(input ("Enter the value"))
y1=int(input ("Enter the value"))
x2=int(input ("Enter the value"))
y2=int(input ("Enter the value"))
x3=int(input ("Enter the value"))
y3=int(input ("Enter the value"))"""


# Input the coordinates of three points
x1, y1 = map(int, input("Enter the coordinates of point 1 (x1, y1): ").split())
x2, y2 = map(int, input("Enter the coordinates of point 2 (x2, y2): ").split())
x3, y3 = map(int, input("Enter the coordinates of point 3 (x3, y3): ").split())

# Checking collinearity using the cross-product method with if-else statement
if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
    print("The points are collinear and lie on the same straight line.")
else:
    print("The points are not collinear and do not lie on the same straight line.")
