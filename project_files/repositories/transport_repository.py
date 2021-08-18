from pdb import run

from psycopg2.extensions import SQL_IN
from db.run_sql import run_sql

from models.transport import Transport

# save
def save(transport):
    sql = "INSERT INTO transport_types (mode_of_travel, carbon_per_mile, mpg) VALUES (%s, %s, %s) RETURNING *"
    values = [transport.mode_of_travel, int(transport.emissions_pm()), transport.mpg]
    results = run_sql(sql, values)
    id = results[0]['id']
    transport.id = id

# select all

def select_all():
    transport_types = []
    sql = "SELECT * FROM transport_types ORDER BY id"
    results = run_sql(sql)
    for row in results:
        transport = Transport(row['mode_of_travel'], row['mpg'], row['id'])
        transport_types.append(transport)
    return transport_types


# select

def select(id):
    sql = "SELECT * FROM transport_types WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        transport = Transport(result['mode_of_travel'], result['mpg'], result ['id']) 
    return transport
# delete

def delete(id):
    sql = "DELETE FROM transport_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# delete all

def delete_all():
    sql = "DELETE FROM transport_types"
    run_sql(sql)

# update

def update(transport):
    sql = "UPDATE transport_types SET (mode_of_travel, carbon_per_mile, mpg) = (%s, %s, %s) WHERE id = %s"
    values = [transport.mode_of_travel, transport.emissions_pm(), transport.mpg, transport.id]
    run_sql(sql, values)