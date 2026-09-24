import math

def calculate_factorial():
    number = int(input("Enter the number whose factorial you want to find:"))

    print(f"The factorial is {math.factorial(number)}")
    print("------------------------------------------------")


def compound_interest():
    P_amount = int(input("Enter principal amount:"))
    rate = int(input("Enter rate of interest(in %):"))
    time = int(input("Enter time(in years):"))

    Amount = P_amount * pow(
        (1 + rate / 100),
        time
    )

    print(f"The Compound Interest is :{Amount}")
    print("-------------------------------------------------")


def trigonometric_calculations():

    angle = float(input("Enter angle in degrees: "))

    # want the angle in radian
    print("The angle in radian for sin is :",math.sin(math.radians(angle)))
    print("The angle in radian for cos is :",math.cos(math.radians(angle)))
    print("The angle in radian for tan is :",math.tan(math.radians(angle)))

    print("Finding the inverse of sin,cos,tan")

    value = float(input("Enter a value: "))

    print("The inverse of cos in degree is :",math.degrees(math.acos(value)))
    print("The inverse of sin in degree is :",math.degrees(math.asin(value)))
    print("The inverse of tan in degree is :",math.degrees(math.atan(value)))

    print("-------------------------------------------------")


def geometric_areas():
    print("For Circle")
    radius = float(input("Enter the value of the raduis:"))

    circle_Area = 3.14 * radius * radius

    print(f"The Area of the circle is :{circle_Area}")

    print("\nFor Square")
    side = float(input("Enter the value of the side:"))

    Square_Area = pow(side, 2)

    print(f"The Area of the square is :{Square_Area}")
    print("------------------------------------------------")





