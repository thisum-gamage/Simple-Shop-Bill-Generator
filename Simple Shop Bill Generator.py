def Sub_Total():

    Total = sum()
    return Total


def Discount():

    if Sub_Total() > 10000:
        Discount = 15 / 100
    elif Sub_Total() > 5000:
        Discount = 10 / 100
    else:
        Discount = 0
    return Discount


def Final_Amount():

    Net_Amount = Sub_Total() - Discount()
    return Net_Amount


print("--Welcome To Simple Shop Bill Generator--")
print("-----------------------------------------")

Item_Name = input("Enter Your Item Name : ")
Quantity = float(input("Enter Your Quantity : "))
Price_Per_Item = float(input("Enter Price Per Item : "))

print("-----------------------------------------")

print("--------This is Your Bill Summary--------")

print("\nItem Name\t: ")
print("Quantity\t: ")
print("Price\t\t: ")
print("Total\t\t: ")
print("Discount\t: ")
print("Final Amount\t: ")

print("\n----------------Thank You----------------")
