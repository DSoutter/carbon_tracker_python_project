from pdb import run

from psycopg2.extensions import SQL_IN
from db.run_sql import run_sql

from models.transport import Transport
from models.purpose import Purpose
from models.trip import Trip

# save



# select all




# select



# delete



# delete all

def delete_all():
    sql = "DELETE FROM trips"
    run_sql(sql)
# update

