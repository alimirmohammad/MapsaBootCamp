from Mapsa_libery_auto import Book, login_lib, lib_db
from Mapsa_libery_auto import Member

import json


class main:
    username = input("please enter your username:")
    password = input("please enter your password:")
    obj_login = login_lib.Login()
    mem = obj_login.check(username, password)
    # print(mem.name,mem.age,mem.id_mem,mem.trustee,mem.level)
    if mem.level == 1:
        action = input("choose your action, if you want add new memeber press 1\n add new book press 2\n "
                       "extend the time of trust book press 3\n add to or remve from balck list press 4\n "
                       "exit from system press 5\n")
        if action == '1':
            new_username = input("please enter the username:")
            new_password = input("please enter the password:")
            new_name = input("please enter the name:")
            new_age = input("please enter the age:")
            new_level = input("please enter 1 if this user is admin and enter 0 if is usal member:")
            mem.add_user(new_username, new_password, new_name, new_age, new_level)
    else:
        action = input("choose your action, wacht the list of book 1\n watch the lended book 2\n ")
    # continue_flag = False
    # print("if you want do any action,press Y")
    # doning = input()
    # if doning == "Y":
    #     continue_flag = True
    # while continue_flag:
    #     print("if you want add member,please write M. if you want add new book,please write B. if you want determin a renty book"
    #             "please Enter the R")
    #     fun = input()
    #     if fun == "M":
    #         print("please write the name of member")
    #         num_mem = input()
    #         print("please write the age of member")
    #         adge_mem = input()
    #         Member.MEMBER(num_mem, adge_mem)
    #         print("This member added successfully")
    #     elif fun == "B":
    #         print("please write the name of the book")
    #         book_name = input()
    #         print("please write the name of the writer:")
    #         wirter_name = input()
    #         print("please detect the category of the book:")
    #         category_book = input()
    #         print("please write the ISBN of the book:")
    #         isbn_book = input()
    #         Book.Book(book_name, wirter_name, category_book, isbn_book)
    #     elif fun == "R":
    #         print("plese write the id of membership")
    #         mem_id = input()
    #         print("please write the name of the book:")
    #         num_book = input()
    #         with open("book.json") as b:
    #             book_list = json.load(b)
    #         with open("member.json") as m:
    #             mem_list = json.load(m)
    #         for j in mem_list["mem"]:
    #             #print(type(j['id']))
    #             if j['id'] == int(mem_id):
    #                 mem_temp = Member.MEMBER(j["name"], j["age"])
    #         for i in book_list["book"]:
    #             if i["name"] == num_book:
    #                 book_temp = Book.Book(i["name"],i["author"],i["category"],i["ISBN"])
    #                 book_temp.rentbook(mem_temp)
    #                 print("The borrow book is register")
    #     print("if you want do anyting else,press Y otherwise press N")
    #     doagain = input()
    #     if doning == "N":
    #         continue_flag = False