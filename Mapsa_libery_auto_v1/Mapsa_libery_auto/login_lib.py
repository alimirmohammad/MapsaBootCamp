from Mapsa_libery_auto import lib_db,Member

class Login:
    def __init__(self):
        self.db = lib_db.DataBase('db_lib')
        self.__member = None
    def check(self, username, password):
        result = self.db.cursor.execute("select * from user where username = '{}' and password = '{}'".format(
            username, password)).fetchall()
        if result != []:
            self.__member = Member.admin_member(result[0][3], result[0][4], result[0][0], result[0][5], result[0][6])
            print("{} loing sucssfuly".format(result[0][3]))
        else:
            print("your username or password incorrect!")
        return self.__member

# test = Login()
# test.check('admin', '123')
