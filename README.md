# Prediction-of-Diabetes

pip install mysql-connector-python
pip install pandas
pip install scikit-learn
pip install Flask

1. สร้าง Database ก่อน โดยใช้คำสั่ง CREATE DATABASE diabetesdb;

2. สร้างตาราง
CREATE TABLE diabetestable (
  id int auto_increment primary key,
  pregnancies int,
  glucose decimal(10,2),
  skin_thickness decimal(10,2),
  BMI decimal(10,2),
  age int,
  result varchar(30)
);

3. เปิดโปรแกรม แล้วพิมพ์ใน terminal
pip install pandas
pip install scikit-learn
pip install mysql-connector-python
pip install Flask

4. แก้รหัสผ่านฐานข้อมูลตัวเองใน model.py และรันที่ views.py 
