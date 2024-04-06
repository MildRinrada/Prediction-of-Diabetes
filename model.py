# Import libraries
import mysql.connector
from decimal import Decimal

# ทำโมเดล+เขียนคำสั่ง SQL
class DataModel:
    def __init__(self, id, pregnancies, glucose, bloodpressure, BMI, age, result, percentage):
        self.id = id
        self.pregnancies = pregnancies
        self.glucose = glucose
        self.bloodpressure = bloodpressure
        self.BMI = BMI
        self.age = age
        self.result = result
        self.percentage = percentage

    @staticmethod
    def connector():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ppgdmild",
            database="diabetesdb"
        )
        return connection

    # insertแถวลงในDatabase
    def insert(self, result, percentage):
        # เชื่อมต่อฐานข้อมูล
        connection = DataModel.connector()
        cursor = connection.cursor()
        query = "INSERT INTO diabetestable (pregnancies, glucose, bloodpressure, BMI, age, result, percentage) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try: 
            values = (self.pregnancies, self.glucose, self.bloodpressure, Decimal(str(self.BMI)), self.age, result, Decimal(str(percentage)))
            cursor.execute(query, values)
            connection.commit()
            return cursor.lastrowid
        except Exception as e: #กรณีที่ insert แล้วเกิด error
            print(f"Error: {e}")
            return None


    # ดึงค่าจากฐานข้อมูลทั้งหมด
    @staticmethod
    def get_all():
        # เชื่อมต่อฐานข้อมูล
        connection = DataModel.connector()
        cursor = connection.cursor()
        query = "SELECT * FROM diabetestable" 
        cursor.execute(query)
        result = cursor.fetchall()
        data_list = []
        for row in result: 
            data_list.append(DataModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        return data_list #ลิสต์ข้อมูล
