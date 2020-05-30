def show_typeitem(list_typeofitem):
    print("This is the list of type of items")
    for i in range(0,len(list_typeofitem)):
        if list_typeofitem[i] == '':
            continue
        else:
            print('{0}.{1}'.format(i+1,list_typeofitem[i]))

def add_typeitem(list_typeofitem):
    input_new = input("Please enter the type of item you want to add: ")
    list_typeofitem.append(input_new)

def edit_typeitem(list_typeofitem):
    choose = int(input("Please enter id of the type of item you want to edit: "))
    print('This is the item you want to edit: ')
    print(list_typeofitem[choose-1])
    input_new = input("Please enter the content you want to edit: ")
    list_typeofitem[choose-1]=input_new

def delete_typeitem(list_typeofitem):
    choose = int(input("Please enter the type of item you want to delete: "))
    print('This is the item you want to delete: ')
    print(list_typeofitem[choose - 1])
    confirm = input("Do you really want to delete it? y/n: ")
    if confirm == 'y':
        list_typeofitem[choose-1]=''

def search_typeitem(list_typeofitem): ##Please use RegEx here. #bug bugg
    choose = input("Please enter the type of item you want to search: ")
    for ele in list_typeofitem:
        if ele == choose:
            print('{0}'.format(ele))

def show_typeitem(list_typeofitem):
    print("This is the list of type of items")
    for i in range(0,len(list_typeofitem)):
        print('{0}.{1}'.format(str(i+1),list_typeofitem[i]))