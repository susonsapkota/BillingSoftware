import data_read_write

discount_amount = 0
discount_percent = 0


def ask_name():
    global costumers_name
    costumers_name = input("Billed to :")


def ask_discount():
    global discount_amount
    global discount_percent
    try:
        discount_percent = float(input("Discount percentage(up to decimal):"))
        counter = True
        while counter:
            if discount_percent < 0:
                print("Input positive number")
                discount_percent = float(input("Discount percentage(up to decimal):"))
            else:
                counter = False
                discount_amount = (total_price * (discount_percent / 100))

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        ask_discount()


products = []


def ask_product():
    global product_id
    try:
        product_input = int(input("What Product do you want to Buy? Input product id:"))
        counter = True
        while counter:
            if product_input > (len(data_read_write.cleaned_data)-1) or product_input < 0:
                print("Input valid product id")
                product_input = int(input("What Product do you want to Buy? Input product id:"))
            else:
                counter = False
                products.append(product_input)
                product_id = product_input
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        ask_product()


quantity = []


def ask_quantity():
    try:
        ask_times = int(input("How many quantity do you want to buy?"))
        counter = True
        while counter:
            if (int(data_read_write.cleaned_data[product_id][2]) - ask_times) < 0:
                print("Inventory out of stock. Available :" + data_read_write.cleaned_data[product_id][2])
                ask_times = int(input("How many quantity do you want to buy?"))

            else:
                counter = False
                quantity.append(ask_times)

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        ask_quantity()


def ask_try():
    ask_times = input("Do you want to add more product?\n"
                      "[y to continue or press key to exit.]")
    while ask_times == "y" or ask_times == "Y":
        data_read_write.display_product()
        ask_product()
        ask_quantity()
        ask_times = input("Do you want to add more product?\n"
                          "[y to continue or press key to exit.]")


price = []
total_price = 0


def calculate_price():
    global total_price
    for i in range(len(products)):
        unit_price = int(data_read_write.cleaned_data[products[i]][1])
        total = int(unit_price * int(quantity[i]))
        total_price = total_price + total
        price.append(str(total))
