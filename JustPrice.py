from random import randint

# choose a number between 1 and 1000
price = randint(1,1000)

running = True

while running:

    user_price = int(input("Enter the price"))

    # conditions
    if user_price == price:
        print("Nice !")
        # end
        running = False

    elif user_price > price:
        print("less")
    elif user_price < price:
        print("more")
