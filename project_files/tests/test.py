import unittest
import pdb
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

    def test_trip1_has_purpose(self):
        self.assertEqual("To/From Work", self.trip1.purpose.travel_purpose)       

    def test_trip1_has_transport_mpg(self):
        self.assertEqual(45, self.trip1.transport_type.mpg)

    def test_transport_has_correct_emissions_petrol(self):
        self.assertEqual(232, self.transport1.emissions_pm())

    def test_transport_has_correct_emissions_diesel(self):
        self.assertEqual(245, self.transport2.emissions_pm())

    def test_transport_has_correct_emissions_bus(self):
        self.assertEqual(100, self.transport3.emissions_pm())

    def test_transport_has_correct_emissions_plane(self):
        # pdb.set_trace()
        self.assertEqual(145, self.transport4.emissions_pm())

    def test_transport_has_correct_emissions_train(self):
        self.assertEqual(56, self.transport5.emissions_pm())

    def test_trip1_emissions_figure(self):
        # pdb.set_trace()
        self.assertEqual(9280, self.trip1.emissions())

    def test_trip2_emissions_figure(self):
        self.assertEqual(13920, self.trip2.emissions())

    def test_trip3_emissions_figure(self):
        self.assertEqual(72500, self.trip3.emissions())