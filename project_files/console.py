import pdb
from models.purpose import Purpose
from models.transport import Transport
from models.trip import Trip

import repositories.purpose_repository as purpose_repo
import repositories.transport_repository as transport_repo
import repositories.trip_repository as trip_repo

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

trip1 = Trip(40, 01/04/2023, purpose1, transport1)
trip2 = Trip(60, 02/04/2023, purpose1, transport1)
trip3 = Trip(500, XXXX, purpose2, transport4)