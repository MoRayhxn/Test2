# x = float(input("What's X? "))
# y = float(input("What's y? "))

# if x < y:
#     print(f"{x} is less than {y}")
# if x > y:
#     print(f"{x} is greater than {y}")
# if x == y:
#     print(f"{x} is equal to {y}")

## more efficient way to run code

# x = float(input("What's X? "))
# y = float(input("What's y? "))

# if x < y:
#     print(f"{x} is less than {y}")
# elif x > y:
#     print(f"{x} is greater than {y}")
# else:
#     print(f"{x} is equal to {y}")

x = float(input("What's X? "))
y = float(input("What's y? "))

if x != y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")