class Trip:
    def __init__(self, distance, date, purpose, transport_type, id = None):
        self.distance = distance
        self.date = date
        self.purpose = purpose
        self.transport_type = transport_type
        self.id = id

    def emissions(self):
        emissions = self.distance * self.transport_type.emissions_pm()
        return emissions