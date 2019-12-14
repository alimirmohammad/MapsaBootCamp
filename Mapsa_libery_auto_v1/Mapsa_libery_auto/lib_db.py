import sqlite3
import datetime


class DataBase:
    __instance = 0

    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # self.name = 'sara'

    def __new__(cls, db_name):
        if DataBase.__instance == 0:
            DataBase.__instance = super().__new__(cls)
        return DataBase.__instance

db = DataBase('db_lib')
# db.cursor.execute("create table user (id integer primary key autoincrement,username varchar(256), "
#                   "password varchar(256),name varchar(256),age int, trustee boolean,level boolean)")
# db.cursor.execute("insert into user(username, password, name, age, trustee, level) values"
#                   "('admin','1234','saeede',26, 0, 1)")

# db.cursor.execute("create table book (id integer primary key autoincrement, name varchar(256), author  varchar(256),"
#                   "ISBN int, category varchar(256), status boolean, type boolean, language varchar(256), "
#                   "translator varchar(256))")
# db.cursor.execute("insert into book (name, author, ISBN, category, status, type, language) values "
#                    "('paiz fasl akhar ast', 'Nasim marashi', 342087, 'novel', 1, 0, 'fa' ) ")
# db.cursor.execute("create table rent (id integer  autoincrement ,book_id int, member_id int,start_date_lend Date,"
#                   "return_status boolean ,"
#                   "FOREIGN KEY (book_id)REFERENCES book (id)"
#                   ",FOREIGN KEY (member_id)REFERENCES user (id))")
#
# db.cursor.execute("insert into rent (book_id, member_id) values (3,1)")
print(db.cursor.execute("select * from user").fetchall())
# db.cursor.execute("drop table rent")
db.connection.commit()