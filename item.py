from typeofitem import show_typeitem
import pdb

class Item: #There is one bug there. If you delete some object, the id of the item will be different from the file.
    Id = 1
    def __init__(self,name,expire,company,year,typeofitems):
        self.name = name
        self.expire = expire
        self.company = company
        self.year = year
        self.typeofitmes = typeofitems
        self.id = 'hh'+str(Item.Id)
        Item.Id +=1

    def __str__(self):
        return str(self.id) + '\t' + self.name + '\t\t' + self.expire + '\t' + self.company + '\t' + self.year + '\t' + self.typeofitmes

    def edit_item(self,att,value):
        if att == 1:
            self.name=value
        elif att == 2:
            self.expire=value
        elif att == 3:
            self.company=value
        elif att == 4:
            self.year=value
        elif att == 5:
            self.typeofitmes=value

    @classmethod
    def from_string(cls,s):
        lst = s.split('\t')
        lst.pop(0)
        lst.pop(1)
        (name,expire,company,year,typeofitems) = lst
        return cls(name,expire,company,year,typeofitems)

def show_item(list_item):
    print("This is the list of items")
    print('STT\tId\tName\t\tExpire\tCompany\tYear\tType of items')
    for i in range(0,len(list_item)):
        item = list_item[i]
        string = str(i+1)+ '\t' + str(item)
        print(string)

def add_item(list_item,list_typeofitem):
    print('Nhap thong tin hang hoa can them. ')
    name = input("Nhap ten cua hang hoa: ")
    expire = input("Nhap handung cua hang hoa: ")
    company = input("Nhap cong ty san xuat hang hoa: ")
    year = input("Nhap nam san xuat hang hoa: ")
    print("Chon Loai hang.")
    show_typeitem(list_typeofitem)
    typeofitems = list_typeofitem[int(input("Nhap loai hang: "))-1]
    new_item = Item(name,expire,company,year,typeofitems)
    list_item.append(new_item)
    print('You just add this items: {0}'.format(new_item))

def delete_item(list_item):
    show_item(list_item)
    choose = int(input("Please enter the item you want to delete: "))
    print('This is the item you want to delete: ')
    print(list_item[choose - 1])
    confirm = input("Do you really want to delete it? y/n: ")
    if confirm == 'y':
        list_item.pop(choose-1)

def edit_item(list_item):
    choose_edit =1000
    while choose_edit>len(list_item):
        choose_edit = int(input("Please choose the item you want to edit: "))
    item_choose = list_item[choose_edit - 1]
    listofattribute = [*list_item[0].__dict__]
    while True:
        for i in range(0, len(listofattribute)):
            print('{0}.{1}'.format(i+1,listofattribute[i]))
        choose_content = int(input("Please choose the content you want to edit. Press 9 for finish: "))
        if choose_content ==9:
            break
        edit_content = input('Please enter the content you want to edit for {0}: '.format(listofattribute[choose_content-1]))
        item_choose.edit_item(choose_content,edit_content)
        print('This is the item you just edit')
        print(item_choose)

def search_item(list_item): ##Please use RegEx here.
    print("We will search on the name")
    choose = input("Please enter the item you want to search: ")
    print('Id-Name-Expire-Company-Year-Type of items')
    for ele in list_item:
        if ele.name == choose:
            print(ele)