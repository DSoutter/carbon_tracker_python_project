class Transport:
    def __init__(self, mode_of_travel, mpg, emissions_per_mile, id = None):
        self.mode_of_travel = mode_of_travel
        self.mpg = mpg
        self.emissions_per_mile = emissions_per_mile
        self.id = id

    def emissions_pm(self):
        # return self.mpg * some factor
        # could consider it an if else statement as follows:
        # if mode is car:
        #   if car is diesel:
        #       return factor x mpg
        #  else:
        #       return factor x mpg
        # else if mode is plane:
        #   return a predetermined number
        # else if mode is bus:
        #   return a predetermined number
        # else if mode is train:
        #   return a predetermined number
        