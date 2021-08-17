from pdb import run, set_trace

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
    sql = "SELECT * FROM trips ORDER BY date DESC"
    results = run_sql(sql)
    for row in results:
        purpose = purpose_repo.select(row['purpose_id'])
        transport_type = transport_repo.select(row['transport_type_id'])
        trip = Trip(row['distance'], row['date'], purpose, transport_type, row['id'])
        trips.append(trip)
    return trips
# select

def select(id):
    sql = "SELECT * FROM trips WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        purpose = purpose_repo.select(result['purpose_id'])
        transport_type = transport_repo.select(result['transport_type_id'])
        trip = Trip(result['distance'], result['date'], purpose, transport_type, result['id'])
    return trip
# delete

def delete(id):
    sql = "DELETE FROM trips WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# delete all

def delete_all():
    sql = "DELETE FROM trips"
    run_sql(sql)

# update

def update(trip):
    sql = "UPDATE trips SET (distance, carbon, date, purpose_id, transport_type_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [trip.distance, trip.emissions(), trip.date, trip.purpose.id, trip.transport_type.id, trip.id]
    run_sql(sql, values)
    
# total emissions

def total():
    sql = "SELECT SUM(carbon) FROM trips" 
    total_carbon_emissions_base = run_sql(sql)[0][0]
    total_carbon_emissions =  str(total_carbon_emissions_base) + "g"
    if total_carbon_emissions_base > 2000000:
        total_carbon_emissions = str(round(total_carbon_emissions_base/1000000,2)) + "t"
    elif total_carbon_emissions_base > 5000:
        total_carbon_emissions = str(round(total_carbon_emissions_base/1000,2)) + "kg"
    return total_carbon_emissions

def count():
    sql = "SELECT COUNT(id) FROM TRIPS"
    return run_sql(sql)[0][0]

# update all carbon:
def update_carbon():
    sql = "SELECT * FROM trips"
    results = run_sql(sql)
    for row in results:
        purpose = purpose_repo.select(row['purpose_id'])
        transport_type = transport_repo.select(row['transport_type_id'])
        trip=Trip(row['distance'], row['date'], purpose, transport_type, row['id'])
        update(trip)

# select by year
def select_all_by_year(year):
    trips = []
    sql = "SELECT * FROM trips WHERE EXTRACT(year FROM date) = %s"
    values = [year]
    results = run_sql(sql,values)

    for row in results:
        purpose = purpose_repo.select(row['purpose_id'])
        transport_type = transport_repo.select(row['transport_type_id'])
        trip = Trip(row['distance'], row['date'], purpose, transport_type, row['id'])
        trips.append(trip)
    return trips