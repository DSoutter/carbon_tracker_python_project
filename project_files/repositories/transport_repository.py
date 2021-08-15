from pdb import run

from psycopg2.extensions import SQL_IN
from db.run_sql import run_sql

from models.transport import Transport

# save
# why do I need int of the method????
def save(transport):
    sql = "INSERT INTO transport_types (mode_of_travel, carbon_per_mile, mpg) VALUES (%s, %s, %s) RETURNING *"
    values = [transport.mode_of_travel, int(transport.emissions_pm()), transport.mpg]
    results = run_sql(sql, values)
    id = results[0]['id']
    transport.id = id

# select all

def select_all():
    transport_types = []
    sql = "SELECT * FROM transport_types"
    results = run_sql(sql)
    for row in results:
        transport = Transport(row['mode_of_travel'], row['mpg'], row['id'])
        # carbon_per_mile = transport.emissions_pm()
        transport_types.append(transport)
    return transport_types


# select



# delete



# delete all

def delete_all():
    sql = "DELETE FROM transport_types"
    run_sql(sql)

# update


