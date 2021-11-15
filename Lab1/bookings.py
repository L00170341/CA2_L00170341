title="Booking Screen"
print(title.rjust(30, ' '))

print("\n")  # newline twice

title2="Customer: J.Finegan"
print("{:>30}".format(title2))

title3="Customer Code: L00170341"
print("{:>30}".format(title3))

print("\n")  # newline twice

price1=90.99
price2=99.99

print("{0:<30s} {1:16.2f}".format("7pm Booking", price1))
print("{0:<30s} {1:16.2f}".format("8pm Booking", price2))
print("_"*47)


answer=input("Please choose an option: ")
print("Your answer was: {}".format(answer))

print("{:>30}".format(title2))

