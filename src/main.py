import data_read_write
import user_input
import invoice

data_read_write.clean_data()
# cleans the data(converts into usable form)

user_input.ask_name()
# asks user's name

data_read_write.display_product()
# Displays the product

user_input.ask_product()
# asks for which product to add to cart

user_input.ask_quantity()
# asks for how many quantity of product to add to cart

data_read_write.update_inventory()
# updates the inventory after being added to cart

user_input.ask_try()
# asks if user want to add any more products

data_read_write.display_product()
# Displays the product



data_read_write.clean_data()
# done after each inventory updates so updated information is displayed.


user_input.calculate_price()
# process the total price

user_input.ask_discount()
# process the discount

invoice.invoice_process()
# process the invoice by using information form cart
