import pdb
from models.purpose import Purpose
from models.transport import Transport
from models.trip import Trip

import repositories.purpose_repository as purpose_repo
import repositories.transport_repository as transport_repo
import repositories.trip_repository as trip_repo
import datetime

trip_repo.delete_all()
transport_repo.delete_all()
purpose_repo.delete_all()

# Add in a few trips, transports and purposes to get started.
purpose1 = Purpose("To/From Work")
purpose2 = Purpose("For Work Travel")
purpose3 = Purpose("Kids Taxi Service")
purpose4 = Purpose("Leisure")

transport1 = Transport("Car 1, petrol", 45)
transport2 = Transport("Car 2, diesel", 50)
transport3 = Transport("Bus", None)
transport4 = Transport("Plane", None)
transport5 = Transport("Train", None)

trip1 = Trip(40, datetime.date(2020, 8, 10), purpose1, transport1)
trip2 = Trip(60, datetime.date(2021, 6, 11), purpose1, transport1)
trip3 = Trip(500, datetime.date(2021, 6, 12), purpose2, transport4)
trip4 = Trip(40, datetime.date(2021, 7, 13), purpose1, transport1)
trip5 = Trip(60, datetime.date(2021, 7, 11), purpose1, transport2)
trip6 = Trip(5000, datetime.date(2021, 8, 12), purpose2, transport4)
trip7 = Trip(40, datetime.date(2021, 8, 10), purpose1, transport2)
trip8 = Trip(60, datetime.date(2021, 8, 11), purpose1, transport3)
trip9 = Trip(1000, datetime.date(2021, 8, 12), purpose2, transport4)
trip10 = Trip(40, datetime.date(2021, 8, 10), purpose1, transport1)
trip11 = Trip(55, datetime.date(2021, 8, 16), purpose1, transport5)
trip12 = Trip(55, datetime.date(2021, 8, 17), purpose1, transport5)

purpose_repo.save(purpose1)
purpose_repo.save(purpose2)
purpose_repo.save(purpose3)
purpose_repo.save(purpose4)


transport_repo.save(transport1)
transport_repo.save(transport2)
transport_repo.save(transport3)
transport_repo.save(transport4)
transport_repo.save(transport5)

trip_repo.save(trip1)
trip_repo.save(trip2)
trip_repo.save(trip3)
trip_repo.save(trip4)
trip_repo.save(trip5)
trip_repo.save(trip6)
trip_repo.save(trip7)
trip_repo.save(trip8)
trip_repo.save(trip9)
trip_repo.save(trip10)
trip_repo.save(trip11)
trip_repo.save(trip12)



pdb.set_trace()
