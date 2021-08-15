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



# select



# delete



# delete all



# update