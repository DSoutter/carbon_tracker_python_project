from unittest import result
from db.run_sql import run_sql

from models.purpose import Purpose

# save

def save(purpose):
    sql = "INSERT INTO purposes (travel_purpose) VALUES (%s)"
    values = [purpose.travel_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    purpose.id = id

# select all

def select_all():
    purposes = []
    sql = "SELECT * FROM purposes"
    results = run_sql(sql)
    for row in results:

        purpose = Purpose(row['travel_purpose'], row['id'])
        purposes.append(purpose)
    return purposes

# select



# delete



# delete all



# update