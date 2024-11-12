import csv

try:
    with open('D:\Programming\Python\storage_manager\storage.csv', mode='r') as db:
        db_reader = csv.DictReader(db)
        line_count = 0
        print("Database successfully imported")

except FileNotFoundError:
    open('D:\Programming\Python\storage_manager\storage.csv', mode='x')
    print("File not found")
    print("New database created")

with open('D:\Programming\Python\storage_manager\storage.csv', mode='r') as db:
        db_reader = csv.DictReader(db)
        line_count = 0
        for row in db_reader:
            print(row)


def add_new_product():
     print("Add new product")
     get_ean = input("Enter EAN: ")
     quantity = input("Enter quantity: ")
     with open('D:\Programming\Python\storage_manager\storage.csv', 'a', newline='') as db_output:
        writer = csv.writer(db_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([get_ean, quantity, 15])

def take_product():
     print("Taking product...")
     get_ean = input("Enter EAN: ")
     placeholder = []
     does_item_exist = False
     with open('D:\Programming\Python\storage_manager\storage.csv', mode='r') as db:
        db_reader = csv.DictReader(db)
        line_count = 0
        print("Database import successful")
        for row in db_reader:
            if get_ean == row['ean']:
                print("item found")
                x = int(row['quantity']) - 1
                row['quantity'] = x
                print(row)
                placeholder.append(row)
                does_item_exist = True
            
            elif get_ean not in row['ean']:
                placeholder.append(row)                
                
        if does_item_exist == False:
            print("Item not found")
            add_product()

     check_quantity()
     update_database(placeholder)

def add_product():
     print("Adding product...")
     get_ean = input("Enter EAN: ")
     get_quant = input("How many have you ordered? ")
     placeholder = []
     with open('D:\Programming\Python\storage_manager\storage.csv', mode='r') as db:
        db_reader = csv.DictReader(db)
        line_count = 0
        print("Database import successful")
        for row in db_reader:
            if get_ean in row['ean']:
                print("item found")
                x = int(row['quantity']) + int(get_quant)
                row['quantity'] = x
                print(row)
                placeholder.append(row)
                break
            
            else:
                prompt = input("Item not found, add new? Y/n ")
                if prompt == 'Y':
                    add_new_product()
                    break

                else:
                    break
                
     update_database(placeholder)

def update_database(placeholder):
    print("update database")
    with open('D:\Programming\Python\storage_manager\storage.csv', mode='w') as db:
        fieldnames = ['ean', 'quantity', 'minquantity']
        writer = csv.DictWriter(db, fieldnames=fieldnames)
        line_count = 0   
        print("Database import successful")
        writer.writeheader()
        x = 0
        for i in placeholder:
            writer.writerow(placeholder[x])
            x = x + 1
        print('Updated ', x, 'lines')

def check_quantity():
    print("check quantity")
    with open('D:\Programming\Python\storage_manager\storage.csv', mode='r') as db:
        db_reader = csv.DictReader(db)
        line_count = 0
        print("Database import successful")

        for row in db_reader:
            quant = int(row['quantity'])
            min = int(row['minquantity'])
            if quant < min:
                print("You need to order ", row['ean'], "only", row['quantity'], "remain")


def main():

    print("Storage Manager v1.0")
    print("Menu:")
    print("1. Take products(default)")
    print("2. Add products (samordnaren)")
    select_mode = int(input("Select mode: "))

    while select_mode == 1:
        take_product()
    
    while select_mode == 2:
        add_product()

take_product()