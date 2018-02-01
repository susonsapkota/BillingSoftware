import datetime
import data_read_write
import user_input
import number_to_words

date_time = datetime.datetime.now()
date_now = date_time.strftime("%Y-%m-%d")
time_now = date_time.strftime("%H:%M:%S")


def invoice_process():
    # file writing and form creating.
    f = open(date_time.strftime("%Y%m%d%H%M%S") + ".txt", "w")

    f.write("Costumers Name : " + user_input.costumers_name + "\n")
    f.write("Date : " + date_now + "\n")
    f.write("Time : " + time_now + "\n")

    f.write("=============================================\n")
    f.write("S.N\tProduct Name\tQuantity\tPrice \n")
    f.write("=============================================\n")

    for i in range(len(user_input.products)):
        f.write(str(i + 1) + ".\t" + str(
            data_read_write.cleaned_data[user_input.products[i]][0] + "\t\t" + str(
                user_input.quantity[i])) + "\t\t" + str(
            user_input.price[i]) + "\n")
    f.write("=============================================\n")
    f.write("\t\t\t      Total:  " + str(user_input.total_price) + "\n")
    f.write(
        "\t   - Discount Amount(" + str(user_input.discount_percent) + "%):  " + str(user_input.discount_amount) + "\n")
    f.write("\t\t\t\t  -----------\n")
    costumer_pay = round((user_input.total_price - user_input.discount_amount), 2)
    f.write("\t\t\tGrand Total: " + str(costumer_pay) + "\n")

    f.write("=============================================\n")

    split_num = str(abs(costumer_pay)).split('.')
    int_part = int(split_num[0])
    decimal_part = int(split_num[1])

    f.write("Rs." + str(
        number_to_words.num_to_word(int_part) + "\n and " + number_to_words.num_to_word(
            decimal_part) + " paisa only.\n"))

    f.close()
