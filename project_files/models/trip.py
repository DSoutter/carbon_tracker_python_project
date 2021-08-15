class Trip:
    def __init__(self, distance, date, purpose, mode_of_travel, id = None):
        self.distance = distance
        self.date = date
        self.purpose = purpose
        self.mode_of_travel = mode_of_travel
        self.id = id

    def emissions(self):
        emissions = self.distance * self.mode_of_travel.emissions_pm()
        return emissions