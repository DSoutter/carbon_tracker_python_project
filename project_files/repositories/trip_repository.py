from pdb import run

from psycopg2.extensions import SQL_IN
from db.run_sql import run_sql

from models.transport import Transport
from models.purpose import Purpose
from models.trip import Trip
import repositories.purpose_repository as purpose_repo
import repositories.transport_repository as transport_repo

# save

def save(trip):
    sql = "INSERT INTO trips (distance, carbon, date, purpose_id, transport_type_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [trip.distance, trip.emissions(), trip.date, trip.purpose.id, trip.transport_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    trip.id = id

# select all

def select_all():
    trips = []
    sql = "SELECT * FROM trips"
    results = run_sql(sql)
    for row in results:
        purpose = purpose_repo.select(row['purpose_id'])
        transport_type = transport_repo.select(row['transport_type_id'])
        trip = Trip(row['distance'], row['date'], purpose, transport_type, row['id'])
        trips.append(trip)
    return trips
# select



# delete



# delete all

def delete_all():
    sql = "DELETE FROM trips"
    run_sql(sql)
# update

