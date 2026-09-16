productArray = []
priceArray = []

while True:
    food = input("Enter your option: ")
    if food.lower() == "q":
        break
    else:
        product = input('Enter your product: ')
        price = input('Enter the price: $')

        productArray.append(product)
        priceArray.append(price)




