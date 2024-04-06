from flask import Flask, render_template, request, redirect, url_for
from model import DataModel
from logic import calculate_result

# ทำให้เว็บสามารถเรนเดอร์ไฟล์รูปภาพ และcssได้
app = Flask(__name__, template_folder='pages', static_url_path='/static')

# แสดงหน้าแรก
@app.route('/')
def home():
    data_list = DataModel.get_all()
    # ดึงผลลัพธ์Result
    result = request.args.get('result', '') 
    # ดึงผลลัพธ์Percentage
    percentage = request.args.get('percentage', '')
    # ถ้าพบค่า Percentage
    if percentage:
        # แปลงPercentageให้เป็นทศนิยม
        percentage = float(percentage)

    # ตรวจสอบว่าผลลัพธ์และเปอร์เซ็นต์ว่างเปล่าหรือไม่ ให้แสดง home.html ก่อน
    if not result and not percentage:
        return render_template('home.html')

    # ถ้าpercentage และ result ไม่ Null ให้แสดงผลไปที่หน้า page1.html
    return render_template('result.html', data_list=data_list, result=result, percentage=percentage)

# สร้างแถว
@app.route('/create', methods=['POST'])
def create():
    # รับค่าจากหน้าเว็บมาเก็บในตัวแปร
    if request.method == 'POST':
        pregnancies = request.form['pregnancies']
        glucose = request.form['glucose']
        bloodpressure = request.form['bloodpressure']
        BMI = request.form['BMI']
        age = request.form['age']
        # ค่าอื่นๆที่ไม่ได้รับมาจากเว็บ ได้รับมาจากส่วนของไฟล์ logic.py โดยทำงานเมธอท calculate_result(...)
        result, last_insert_id, percentage = calculate_result(pregnancies, glucose, bloodpressure, BMI, age)
        return redirect(url_for('home', result=result, percentage=percentage))
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
