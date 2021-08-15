from pdb import run
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

def select(id):
    sql = "SELECT * FROM purposes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        purpose = Purpose(result['travel_purpose'], result['id'])

# delete

def delete(id):
    sql = "DELETE FROM purposes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# delete all

def delete_all():
    sql = "DELETE FROM purposes"
    run_sql(sql)

# update