import pymysql
conn=pymysql.connect(user='root',host='localhost',password='Y1012Jqkhkp')
qur='CREATE DATABASE emp_project'
mycur=conn.cursor()
mycur.execute(qur)
mycur.close()
conn.close()
import pymysql
conn=pymysql.connect(user='root',host='localhost',password='1012Jqkhkp',database='emp_project')
qur='''CREATE TABLE emp (
    emp_id VARCHAR(10) PRIMARY KEY,
    emp_name VARCHAR(100),
    mob_no VARCHAR(15),
    dept VARCHAR(50),
    emp_salary VARCHAR(20)
)'''
mycur=conn.cursor()
mycur.execute(qur)
mycur.close()
conn.close()