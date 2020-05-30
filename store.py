from file import readreturn, write
from item import Item, show_item, add_item, delete_item,edit_item,search_item
from typeofitem import show_typeitem,add_typeitem,delete_typeitem,edit_typeitem,search_typeitem
import pdb

def receive_input(list_item,list_typeofitem):
    choose = ['','']
    while choose[0] !='q':
        print('MAIN MENU')
        print('1. Function of Items')
        print('2. Function of Type of Items')
        print('q. Exit the app')
        choose[0] = input('Please chose the function you want to check: ')
        if choose[0] == '1':
            while choose[1] != 'q':
                show_item(list_item)
                print("FUNCTION")
                print("1. Add item.")
                print("2. Remove item.")
                print("3. Edit items.")
                print("4. Search items.")
                print('r. Return to the previous')
                print('q. Exit the app')
                choose[1] = input('Please chose the function you want to check: ')
                if choose[1] == '1':
                    add_item(list_item,list_typeofitem)
                elif choose[1] == '2':
                    delete_item(list_item)
                elif choose[1] == '3':
                    edit_item(list_item)
                elif choose[1] == '4':
                    search_item(list_item)
                elif choose[1] == "r":
                    choose[1] = ""
                    break
                elif choose[1] == "q":
                    choose[0] = 'q'
                    break
            else:
                print('Please input again, your input is wrong')

        elif choose[0] == "2":
            while choose[1] != 'q':
                show_typeitem(list_typeofitem)
                print("FUNCTION")
                print("1. Add the type of items.")
                print("2. Remove the type of items.")
                print("3. Edit the type of items.")
                print("4. Search the type of items.")
                print('r. Return to the previous')
                print('q. Exit the app')
                choose[1] = input('Please chose the function you want to check: ')
                if choose[1] == '1':
                    add_typeitem(list_typeofitem)
                elif choose[1] == '2':
                    delete_typeitem(list_typeofitem)
                elif choose[1] == '3':
                    edit_typeitem(list_typeofitem)
                elif choose[1] == '4':
                    search_typeitem(list_typeofitem)
                elif choose[1] == "r":
                    choose[1] = ""
                    break
                elif choose[1] == "q":
                    choose[0] = 'q'
                    break
                else:
                    print('Please input again, your input is wrong')
        elif choose[0] == "q":
            break
        else:
            print('Please input again, your input is wrong')
    print("Thanks for using our app")

list_item_tem,list_typeofitem = readreturn()
list_item =[]
for ele in list_item_tem:
    item = Item.from_string(ele)
    list_item.append(item)
print("WELCOME")
print("Please select the function")
receive_input(list_item,list_typeofitem)
write(list_item,list_typeofitem)

