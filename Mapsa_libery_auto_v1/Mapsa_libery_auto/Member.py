from datetime import*
from dateutil.relativedelta import*
from Mapsa_libery_auto import lib_db
import json

class admin_member:
    def __init__(self, name, age, id, trustee, level):
        self.name = name
        self.id_mem = id
        self.age = age
        self.time_join = datetime.now()
        self.books_rent = []
        self.trustee = trustee
        self.current_book_rent = []
        self.penalty = 0
        # self.add = self.adduser()
        self.level = level
        self.db = lib_db.DataBase('db_lib')
    # def rent(self, book):
    #     pass

    # def extend(self):
    #     self.time_join += relativedelta(years=1)

    # def expirecheck(self):
    #     expire_status = False
    #     expire_time = self.time_join
    #     expire_time = expire_time + relativedelta(years=1)
    #     if expire_time <= datetime.now():
    #         expire_status = True
    #     return expire_status

    def add_user(self,username, password, name, age,level):

        re = self.db.cursor.execute("select id from user where username = '{}'".format(username)).fetchall()
        if re == []:
            self.db.cursor.execute("insert into user(username, password, name, age, trustee, level) values"
                              "('{}', '{}', '{}', {}, 0, {})".format(username, password, name, age, level))
            self.db.connection.commit()
            print("This user is register")
        else:
            print("This username is exist")
        # try:
        #     with open("member.json") as outfile:
        #         pass
        # except IOError:
        #     list_member = {"mem": []}
        #     with open("member.json", 'w') as outfile:
        #         json.dump(list_member, outfile)
        # with open('member.json') as outfile:
        #     list_member = json.load(outfile)
        # list_member["mem"].append({"id": self.id_mem,"name": self.name, "age": self.age,"time_join": str(self.time_join),
        #                            "book_rent": self.books_rent, "trustee": self.trustee,
        #                            "current_rent": self.current_book_rent, "penalty": self.penalty})
        # with open('member.json', 'w') as outfile:
        #     json.dump(list_member, outfile)
        # return

    def add_ex_book(self, b_name, b_author, b_isbn, b_category, b_type, b_lang, b_translator ):
        self.db.cursor.execute("insert into book (name, author, ISBN, category, status, type, language, translator) "
                               "values ('{}', '{}', {}, '{}', {}, {}, '{}')".format(b_name, b_author, b_isbn,
                                                                                    b_category, 1, b_type, b_lang,
                                                                                    b_translator))
        self.db.connection.commit()

    def add_in_book(self, b_name, b_author, b_isbn, b_category, b_type, b_lang):
        self.db.cursor.execute("insert into book (name, author, ISBN, category, status, type, language) "
                               "values ('{}', '{}', {}, '{}', {}, {}, '{}')".format(b_name, b_author, b_isbn,
                                                                                    b_category, 1, b_type, b_lang))
        self.db.connection.commit()

    # def chang_deadlin(self, username, book_name):


#u1 = MEMBER("ali", 12)
#u2 = MEMBER("bahram", 22)
#u2 = MEMBER("saeed", 26)
#u2 = MEMBER("sara", 24)
#print(u1.id_mem)

#print(u2.time_join)
#u2.extend()
#u2.expirecheck()
#print(u2.time_join)

