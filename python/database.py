import mysql.connector
import hashlib

class Database():
    def get_user(self, uUsername, uPassword):
        cnx = mysql.connector.connect(
            host="bootcamp-tht.sre.wize.mx",
            port="3306",
            user="secret",
            password="noPow3r",
            database="bootcamp_tht",
        )

        cursor = cnx.cursor()
        cursor.execute('SELECT username, password, salt, role FROM users where username = "'+ uUsername +'"')
        result = cursor.fetchone()

        if result is None:
            return None

        username = result[0]
        password = result[1]
        salt = result[2]
        role = result[3]

        saltPassowrd = (uPassword + salt).encode()
        hashPassword512 = hashlib.sha512(saltPassowrd).hexdigest()

        cursor.close()
        cnx.close()

        if password == hashPassword512:
            return {"role": role}

        return None