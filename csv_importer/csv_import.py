import psycopg2
import os
import csv
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASS")

csv_file = 'companies.csv'
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST
)

cur = conn.cursor()

insert_query = """
    INSERT INTO company (company_name, registration_date, country, industry, employee_count)
    VALUES (%s, %s, %s, %s, %s);
"""

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        company_name = row[0]
        registration_date = row[1]
        country = row[2]
        industry = row[3]
        employee_count = int(row[4])


        cur.execute(insert_query, (company_name, registration_date, country, industry, employee_count))


conn.commit()


cur.close()
conn.close()

print("data is added!")
