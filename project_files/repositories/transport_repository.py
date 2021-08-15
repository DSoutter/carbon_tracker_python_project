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



# select



# delete



# delete all

def delete_all():
    sql = "DELETE FROM transport_types"
    run_sql(sql)

# update


