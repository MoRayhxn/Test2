# # Ask user their name
# name = input('Please enter your name: ')

# # # Remove space from str if made in error
# # name = name.strip()

# # #Capitalise user input  "you can combine line 5 and 8 by just putting them on eachother like in line 10"
# # name = name.title()

# name = name.strip().title()

# #Say hello to user
# print(f'Hello, {name}')
# # print("Hello,",name) - alternative way



# # Ask user their name
# name = input("Please enter your name").strip().title()

# # Say hello to user
# print(f'hello, {name}') 

def main():
    name = input("What is your name? ").title().strip()
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()




