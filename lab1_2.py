class AreaPerimeter :
    def Rectangle(self, l, b):
        perimeter = 2*(l+b)
        area=l*b
        print("perimeter of reactangle is ", perimeter)
        print("area of rectangle is ", area)

    def Circle(self,r):
        perimeter=2*3.14*r
        area=3.14*r*r
        print("perimeter of circle is ", perimeter)
        print("area of circle is  ", area)

    def Triangle(self,a, b, c):
        perimeter=a+b+c
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("perimeter of triangle is ", perimeter)
        print("area of triangle is ", area)


ap = AreaPerimeter()
ch = int(input("enter number of inputs :"))
if ch == 1:
    a = int(input())
    ap.Circle(a)
elif ch == 2:
    a = int(input())
    b = int(input())
    ap.Rectangle(a, b)
elif ch == 3:
    a = int(input())
    b = int(input())
    c = int(input())
    ap.Triangle(a, b, c)
else:
    print("invalid entry")

