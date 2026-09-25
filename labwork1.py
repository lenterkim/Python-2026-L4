import numpy
import re

def p1():
    a = float(input("Enter circle radius?"))
    b = numpy.pi*(a**2)
    print("Circle area =", round(b,0))

def p2():
    a = float(input("Enter the temperature in Celsius?"))
    b = a*9/5 +32
    print(a,"=",round(b,0) )


def p3():
    a = int(input("Enter a number?"))

    if a<=1:
         print(a, "is a NOT prime number")
         return 

    for i in range( 2, a):
            if a % i == 0:
                print(a, "is a NOT prime number")
                return
    print(a, "is a prime number")

def p4():
    a = int(input("Enter a number?"))
    b = 0

    if a<=0:
         print(a, "is a NOT prefect number")
         return

    for i in range(1, a-1):
         if a % i == 0:
            b += i
    if b == a:
        print (a , "is a perfect number")
    else:
         print(a,"is a NOT prefect number")

def p5():
     mycolor = ["Green", "Blue", "Red", "Orange", "White", "Black"]
     a = str(input("What is your favorite color?"))
     if a in mycolor:
          print("Your colod is at index", mycolor.index(a),"in my list")
     else:
          print("Sorry, I could not find your color")


def p6():
     x1 = range(7)
     for n in x1:
          print ( "x1=", n ,end=" ")
     x2 = range(1,13,3)
     for n in x2:
          print( "x2=", n ,end=" ")
     x3 = range(5,0,-1)
     for n in x3:
          print( "x3=", n, end=" ")
     x4 = range(6,-4,-2)
     for n in x4:
          print (  "x4=" ,n ,end=" ")

def p7():
     s = str(input())
     s_s = re.sub(r"\$", "", s)
     print(s_s)

def p8():
     s = input("Enter a list of integer:").split()
     extract_even = []
     for i in s:
          if int(i) % 2 == 0:
               extract_even.append(int(i))
     print(f"{extract_even}")

def p9():
     a = int(input("Enter a number"))
     b=1
     for i in range (1,a+1):
          b = b*i
     print(b)

def p10():
     a = int(input())
     b = []
     for i in range(1,a+1):
          if a % i ==0:
               b.append(int(i))
     print(f"{b}")

def p11():
     ax = float(input("ax="))
     ay = float(input("ay="))

     bx= float(input("bx="))
     by= float(input("by=")) 

     print(((ax-ay)**2 +(bx-by)**2)**0.5)

def p12():
     m = int(input("row"))
     n = int(input("column"))
     for i in range(m):
        # First or last row: print a full row of stars
        if i == 0 or i == m - 1:
            print("* " * n)
        # Middle rows: print star, spaces, star
        else:
            print("* " + "  " * (n - 2) + "*")

#p1()
#p2()
#p3()
#p4()
#p5()
#p6()
#p7()
#p8()
#p9()
#p10()
#p11()
#p12()