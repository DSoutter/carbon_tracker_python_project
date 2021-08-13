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
