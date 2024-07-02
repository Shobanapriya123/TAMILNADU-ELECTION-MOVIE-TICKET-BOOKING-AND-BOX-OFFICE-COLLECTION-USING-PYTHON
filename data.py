import pandas as pd
import mysql.connector

# Read the CSV file
view_data = pd.read_csv('data_new.csv')

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="shobi"
)

mycursor = mydb.cursor()


mycursor.execute("""
CREATE TABLE details (
    id_no INT,
    name VARCHAR(255),
    place VARCHAR(255),
    phn_no VARCHAR(255),
    email_id VARCHAR(255),
    car_model VARCHAR(255),
    date DATE,
    time TIME,
    amount_paid DECIMAL(10, 2)
)
""")


sql = "INSERT INTO box (id_no, name, place, phn_no, email_id, car_model, date, time, amount_paid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


for index, row in view_data.iterrows():
    val = (
        row["id_no"], row["name"], row["place"], row["phn_no"], row["email_id"],
        row["car_model"], row["date"], row["time"], row["amount_paid"]
    )
    mycursor.execute(sql, val)


mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

