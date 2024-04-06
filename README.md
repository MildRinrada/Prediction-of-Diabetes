# Prediction-of-Diabetes

pip install mysql-connector-python <br>
pip install pandas <br>
pip install scikit-learn <br>
pip install Flask <br>

1. สร้าง Database ก่อน โดยใช้คำสั่ง CREATE DATABASE diabetesdb; <br>
2. สร้างตาราง<br>
CREATE TABLE diabetestable ( <br>
  id int auto_increment primary key, <br>
  pregnancies int, <br>
  glucose decimal(10,2),<br>
  skin_thickness decimal(10,2),<br>
  BMI decimal(10,2),<br>
  age int,<br>
  result varchar(30)<br>
);<br>
3. เปิดโปรแกรม แล้วพิมพ์ใน terminal<br>
pip install pandas<br>
pip install scikit-learn<br>
pip install mysql-connector-python<br>
pip install Flask<br>
4. แก้รหัสผ่านฐานข้อมูลตัวเองใน model.py และรันที่ views.py 
