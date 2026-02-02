"""" Statement of Requirements

acceptable_currency = (50, 20, 10, 5)
amount = (75)

while amount > 0:
    insert = input("Insert coin (50p, 20p, 10p, 5p): ")
    convert_paid = int(insert.replace("p", ""))
    
    if convert_paid in acceptable_currency:
        amount = amount - convert_paid      #Deduct the totle amount to the amount the unser have entered
        if amount > 0:
            print(f"{amount} left")
            continue
        elif amount < 0:
            amount = amount*-1              #change the sign if the user enter over the amount
            print(f"Change of {amount}p")   #Print change
            continue
        else:
            print("Coffee paid")
            break
          
    
    else:
        print("Unknown currency denomination")
        continue
    
else:
    print("Enter value with number.") 
"""

"""
def is_interger(v):
    try:
        v = int(v)
        return True
    except ValueError:
        return False

acceptable_currency = (50, 20, 10, 5)
amount = (75)

while amount > 0:
    insert = input("Insert coin (50p, 20p, 10p, 5p): ")
    convert_paid = (insert.replace("p", ""))
    

    if is_interger(convert_paid) == True:
        convert_paid = int(convert_paid)
        if convert_paid in acceptable_currency:
            amount = amount - convert_paid
            if amount > 0:
                print(f"{amount} left")
                continue
            elif amount < 0:
                amount = amount*-1
                print(f"Change of {amount}p")
                continue
            else:
                print("Coffee paid")
                break
          
    
        else:
            print("Unknown currency denomination")
            continue
    
    else:
        print("Invalid Input, Enter value with number.")

"""
def main():
    drinks = input("Enter your drink (Coffee,Hot Chocolate, Tea): ").lower()
    if drinks == "coffee":
        amount_due = 75
    elif drinks == "hot chocolate":
        amount_due = 50
    elif drinks == "tea":
        amount_due = 20
    while amount_due > 0:
        coin = get_coin()
        amount_due = update_total(amount_due, coin)
    print(dispense_product(amount_due))

def is_interger(v):
    try:
        v = int(v)
        return True
    except ValueError:
        return False

def get_coin():
    acceptable_currency = (50, 20, 10, 5)
    check = False

    while check == False:
        insert = input("Insert coin (50p, 20p, 10p, 5p): ")
        convert_paid = (insert.replace("p", ""))

        if is_interger(convert_paid) == True:
            convert_paid = int(convert_paid)
            if convert_paid in acceptable_currency:
                check = True
            else:
                print("Unknown currency denomination")
                continue
        else:
            print("Invalid Input, Enter value with number.")
            continue
    
    return convert_paid
    
def update_total(current, coin):
    current = current - coin
    if current > 0:
        print(f"{current}p left")
        return current       
    else:
         return current


def dispense_product(total_inserted):
    if total_inserted < 0:
        total_inserted = total_inserted*-1
        return (f"Change of {total_inserted}p")
    
    else:
        total_inserted("Coffee paid")

main ()

