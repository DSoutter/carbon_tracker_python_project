import unittest
from models.purpose import *
from models.transport import *
from models.trip import *
import datetime

from repositories.purpose_repository import *
from repositories.transport_repository import *
from repositories.trip_repository import *

class TestClasses(unittest.TestCase):
    def setUp(self):
        self.purpose1 = Purpose("To/From Work")
        self.purpose2 = Purpose("For Work Travel")
        self.purpose3 = Purpose("Kids Taxi Service")
        self.purpose4 = Purpose("Leisure")

        self.transport1 = Transport("Car 1, petrol", 45)
        self.transport2 = Transport("Car 2, diesel", 50)
        self.transport3 = Transport("Bus", None)
        self.transport4 = Transport("Plane", None)
        self.transport5 = Transport("Train", None)

        self.trip1 = Trip(40, datetime.date(2021, 8, 10), self.purpose1, self.transport1)
        self.trip2 = Trip(60, datetime.date(2021, 8, 11), self.purpose1, self.transport1)
        self.trip3 = Trip(500, datetime.date(2021, 8, 12), self.purpose2, self.transport4)

    def test_trip1_has_day(self):
        self.assertEqual(10, self.trip1.date.day)

    def test_trip1_has_month(self):
        self.assertEqual(8, self.trip1.date.month)