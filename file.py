import pdb
def write(list_item,list_typeofitem):
    try:
        f = open('store.txt', 'w')
        f.writelines('items\n')
        f.writelines('Id\tName\t\tExpire\tCompany\tYear\tType of items\n')
        for ele in list_item:
            f.writelines(str(ele))
            f.writelines('\n')
        f.writelines('Type of items\n')
        for ele in list_typeofitem:
            f.writelines(ele)
            f.writelines('\n')
        f.close
    except IOError:
        print('Error')
    else:
        print("Content write sucessfully")
        f.close

content =[]
def read():
    try:
        f = open('store.txt', 'r')
        content = f.readlines()
    except IOError:
        print('Error')
    else:
        print("Content read sucessfully")
        f.close()
        return content

def readreturn():
    try:
        content = read()
        index = content.index("Type of items\n")
        list_item = []
        list_typeofitem = []
        for i in range(2,index):
            x = content[i].split('\n')
            list_item.append(x[0])
        for i in range(index+1,len(content)):
            x = content[i].split('\n')
            list_typeofitem.append(x[0])
        return list_item,list_typeofitem
    except ValueError:
        print('Nothing to read')
        return [],[]

readreturn()