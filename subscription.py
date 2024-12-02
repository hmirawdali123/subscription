import cherrypy
import pymysql
from pymysql import Error

# MySQL Database connection setup
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        database='subscription_db',
        user='root',
        password='StrongPassword123!'
    )

class SubscriptionAPI:
    
    @cherrypy.expose
    def index(self):
        return "Welcome to the Subscription Database API"

    # CRUD operation for Users
    @cherrypy.expose
    def add_user(self, name, email, birthday, monthly_income):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """INSERT INTO Users (name, email, birthday, monthly_income) 
                       VALUES (%s, %s, %s, %s)"""
            values = (name, email, birthday, monthly_income)
            cursor.execute(query, values)
            conn.commit()
            return {"status": "success", "message": "User added successfully"}
        except Error as e:
            return {"error": str(e)}
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @cherrypy.expose
    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Users")
            result = cursor.fetchall()
            return {"Users": result}
        except Error as e:
            return {"error": str(e)}
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # CRUD operation for Subs (Subscriptions)
    @cherrypy.expose
    def add_subscription(self, company_name, cost, sub_type, sub_time):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """INSERT INTO Subs (company_name, cost, sub_type, sub_time) 
                       VALUES (%s, %s, %s, %s)"""
            values = (company_name, cost, sub_type, sub_time)
            cursor.execute(query, values)
            conn.commit()
            return {"status": "success", "message": "Subscription added successfully"}
        except Error as e:
            return {"error": str(e)}
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @cherrypy.expose
    def get_subscriptions(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Subs")
            result = cursor.fetchall()
            return {"Subscriptions": result}
        except Error as e:
            return {"error": str(e)}
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # CRUD operation for UserSub (Linking users and subscriptions)
    @cherrypy.expose
    def add_user_subscription(self, user_id, sub_id, renewal_date, pay_type):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """INSERT INTO UserSub (user_id, sub_id, renewal_date, pay_type) 
                       VALUES (%s, %s, %s, %s)"""
            values = (user_id, sub_id, renewal_date, pay_type)
            cursor.execute(query, values)
            conn.commit()
            return {"status": "success", "message": "User subscription added successfully"}
        except Error as e:
            return {"error": str(e)}
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @cherrypy.expose
    def get_user_subscriptions(self, user_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM UserSub WHERE user_id = %s", (user_id,))
            result = cursor.fetchall()
            return {"UserSubscriptions": result}
        except Error as e:
            return {"error": str(e)}
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # CRUD operation for Renewal Notifications
    @cherrypy.expose
    def get_renewal_notifications(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM renewal_notifications")
            result = cursor.fetchall()
            return {"RenewalNotifications": result}
        except Error as e:
            return {"error": str(e)}
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# CherryPy configuration
if __name__ == '__main__':
    cherrypy.quickstart(SubscriptionAPI())
