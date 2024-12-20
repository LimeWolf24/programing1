print("Enter package weight in kilograms: ")
print("Enter package length in centimeters: ")
print("Enter package width in centimeters: ")
print("Enter package height in centimeters: ")

if package > 27 and package <= 10 and package<= 25 and package <= 38:
    print("too heavy")
elif package <= 27 and package > 10 and package > 25 and package > 38:
    print("too large")
elif package > 27and package > 10 and package > 25 and package > 38:
    print("too large and too heavy")
input()