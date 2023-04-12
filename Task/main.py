# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import csv

def show_menu():
    print("Сделайте выбор:\n1 - Показать все контакты\n2 - Найти по фамилии\n"
          "3 - Найти по телефону\n4 - Добавить контакт\n5 - Удалить контакт\n"
          "6 - Изменить контакт")

def print_all_records():
    for row in reader:
        print(f"Фамилия: {row[0]}\nимя: {row[1]}\nтелефон: {row[2]}\nкомментарий: {row[3]}\n")

def find_by_last_name(reader):
    last_name = input("Введите фамилию контакта: ")
    for row in filter(lambda x: x[0] == last_name, reader):
        print(f"Фамилия: {row[0]}\nимя: {row[1]}\nтелефон: {row[2]}\nкомментарий{row[3]}\n")

def find_by_phone_number(reader):
    phone_number = input("Введите номер телефона: ")
    for row in filter(lambda x: x[2] == phone_number, reader):
        print(f"Фамилия: {row[0]}\nимя: {row[1]}\nтелефон: {row[2]}\nкомментарий{row[3]}\n")

def add_contact():
    with open('phones.csv', 'a', encoding='utf-8', newline='') as mod_file:
        contact = input("Введите данные контакта (фамилию,имя,телефон,комментарий) через пробел: ").split()
        csv.writer(mod_file).writerow(contact)

def remove_contact(reader):
    remove_parametr = input("Введите фамилию, либо имя, либо телефон контакта для удаления: ") #Использовал способ удаления контакта через копирование данных файла
    all_rows = []                                                                              #в список, поиска в нем значения и удаления нужной строчки, затем
    for row in reader:                                                                         #перезапись этого списка снова в файл, перезаписывая файл. Наверное не 
        all_rows.append(row)                                                                   #самый оптимальный способ, но его я хотя бы смог сейчас понять и реализовать)
        for elem_in_row in row:
            if elem_in_row == remove_parametr:
                all_rows.remove(row)
    with open('phones.csv', 'w', encoding='utf-8', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerows(all_rows)

def change_contact(reader):
    change_parametr = input("Введите фамилию, либо имя, либо телефон контакта для изменения: ")
    change = input("На что вы хотите поменять? ")                                             #Метод работает аналогично удалению, только с перезаписыванием нужного
    all_rows = []                                                                             #параметра в строке. Также в методах, не хватает уточнения какие контакты
    for row in reader:                                                                        #надо редактировать,если параметр будет у нескольких записей.  
        all_rows.append(row)                                                                  #Понимаю как надо это реализовывать, но если сейчас этим займусь,
        for i in range(len(row)):                                                             #то просто взорвется голова)
            if row[i] == change_parametr:
                row[i] = change
    with open('phones.csv', 'w', encoding='utf-8', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerows(all_rows)



user_choice = ""
while True:
    show_menu()
    user_choice = input()
    with open('phones.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        

        if user_choice == '1':
            print_all_records()
        elif user_choice == '2':
            find_by_last_name(reader)
        elif user_choice == '3':
            find_by_phone_number(reader)
        elif user_choice == '4':
            add_contact()
        elif user_choice == '5':
            remove_contact(reader)
        elif user_choice == '6':
            change_contact(reader)
        elif user_choice == '0':
            break
