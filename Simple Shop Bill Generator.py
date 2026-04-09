import datetime


def sub_total(item_list):

    total = 0
    for item in item_list:
        total = total + item[1] * item[2]
    return total


def discount_calc(item_list):

    current_total = sub_total(item_list)
    if current_total > 10000:
        discount = current_total * (15 / 100)
    elif current_total > 5000:
        discount = current_total * (10 / 100)
    else:
        discount = 0
    return discount


def final_amount(item_list):

    net_amount = sub_total(item_list) - discount_calc(item_list)
    return net_amount


print("--Welcome To Simple Shop Bill Generator--")
print("-----------------------------------------")

item_list = []

while True:

    item_name = input("Enter Your Item Name\t: ")
    quantity = float(input("Enter Your Quantity\t: "))
    price_per_item = float(input("Enter Price Per Item\t: "))

    user_record = [item_name, quantity, price_per_item]
    item_list.append(user_record)
    print("-----------------------------------------")
    user_choice = input("Are you add another item ? (Y/N) : ")
    print("-----------------------------------------")
    if user_choice.upper() == "N":
        break

current_time = datetime.datetime.now().strftime("%Y-%m-%d  %I:%M %p")

print("\n--------This is Your Bill Summary--------")
print(f"Date & Time : {current_time}")
print("\nItem Name\tQuantity\tPrice(Rs.)")
print("-----------------------------------------")

for item in item_list:

    print(f"\n{item[0]}\t\t{item[1]}\t\t{item[1]*item[2]:.2f}")

print(f"\nTotal\t\t: Rs. {sub_total(item_list):.2f}")
print(f"Discount\t: Rs. {discount_calc(item_list):.2f}")
print(f"Final Amount\t: Rs. {final_amount(item_list):.2f}")

print("\n----------------Thank You----------------")
