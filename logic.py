# Import libraries
from model import DataModel
import pandas as pd
from sklearn.linear_model import LogisticRegression

def calculate_result(pregnancies, glucose, bloodpressure, BMI, age):
    # อ่านข้อมูลจากไฟล์ csv
    df = pd.read_csv('diabetes_training_data.csv')

    # กำหนดตัวแปร target และ features
    target = 'Outcome'
    features = list(df.columns)
    features.remove(target)

    # สร้างโมเดล logistic regression
    model = LogisticRegression(max_iter=1000)

    # ฝึกโมเดลด้วยข้อมูลทั้งหมด
    X = df[features]
    y = df[target]
    model.fit(X, y)
    
    # ตอนรับค่า แปลงตัวเลขก่อน ป้องกัน error
    sample = [int(float(pregnancies)), float(glucose), float(bloodpressure), float(BMI), int(float(age))]
    sample = pd.DataFrame([sample], columns=['Pregnancies', 'Glucose', 'BloodPressure', 'BMI', 'Age'])
    sample = sample.astype({'Pregnancies': 'int', 'Glucose': 'float', 'BloodPressure': 'float', 'BMI': 'float', 'Age': 'int'})
    
    # ทำนายแล้วรับคำตอบเป็นความน่าจะเป็น
    probabilities = model.predict_proba(sample)[0]
    # ใช้ฟังก์ชัน predict_proba เพื่อคำนวณค่าเปอร์เซ็นต์
    percentage = probabilities[1] * 100
    # ได้ output เป็น เปอร์เซ็น เช่น 10%
    result = f"{percentage:.2f}%"  

    # สร้าง instance ของ DataModel และเรียกใช้เมทอด insert()
    data = DataModel(None, int(pregnancies), float(glucose), float(bloodpressure), float(BMI), int(age), result, float(percentage))
    # insertข้อมูลล่าสุด
    last_insert_id = data.insert(result,percentage)
    return result, last_insert_id, percentage
