#телефонный справочник
def show_menu():
    print('1. Распечатать справочник\n'
          '2. Найти телефон по фамилии\n'
          '3. Изменить номер телефона\n'
          '4. Удалить запись\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить абонента в справочник\n'
          '7. Закончить работу')
    choice=int(input())
    return choice

def print_result(phone_book):
    keys = set()
    for record in phone_book:
        keys.update(record.keys())
    print(' '.join(keys))
    for record in phone_book:
        fields = ' '.join(f'{record.get(key, "")}' for key in keys)
        print(fields)

def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    with open('phonebook.txt','r',encoding='utf-8') as phb:
        for line in phb:
            record=dict(zip(fields,line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename,phone_book):
    with open('phonebook.txt','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

def find_by_lastname(phone_book,last_name):
    for i in phone_book:
        if i['Фамилия']==last_name:
            return i['Телефон']
        
    return "Номер телефона не найден"
def change_number(phone_book, last_name, new_number):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == last_name:
            phone_book[i]["Телефон"] = new_number
            return
    print("Фамилия не найдена")

def delete_by_lastname(phone_book, lastname):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == lastname:
            phone_book.remove(phone_book[i])
            return "done"
    print("не найдено")

def find_by_number(phone_book,number):
    for i in phone_book:
        if i["Телефон"]==number:
            return i["Фамилия"]
    return "Номер телефона не найден"

def add_user(phone_book,user_data):
    fields=['Фамилия', 'Имя', 'Отчество', 'Телефон','Описание']
    record=dict(zip(fields, user_data.split(',')))
    phone_book.append(record)

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)
        choice=show_menu()
work_with_phonebook()

