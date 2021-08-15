from logging import NullHandler


class Transport:
    def __init__(self, mode_of_travel, mpg, id = None):
        self.mode_of_travel = mode_of_travel
        self.mpg = mpg
        self.id = id

    
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

    def emissions_pm(self):
            if "car" in self.mode_of_travel:
                if "petrol" in self.mode_of_travel:
                    return 12270/self.mpg
                else:
                    return 10450/self.mpg
            elif "train" or "rail" in self.mode_of_travel:
                return 56.5
            elif "plane" in self.mode_of_travel:
                return 145
            elif "bus" in self.mode_of_travel:
                return 100
            else:
                return None

# plane CO2e = 145 g/mile
# rail CO2e = 56.5g/mile
# bus CO2e = 100g/mile
# petrol car = 2.7 kg CO2/litre = 12.27 kg CO2/gallon
# diesel car = 2.3 kg CO2/litre = 10.45 kg CO2/gallon
# plane CO2e emissions is 90g/RPK (revenue passenger kilometer) globally on average: https://theicct.org/sites/default/files/publications/CO2-commercial-aviation-oct2020.pdf
# rail CO2e emissions is 35.1g/km: https://dataportal.orr.gov.uk/media/1843/rail-emissions-2019-20.pdf
# bus CO2e emissions: https://www.carbonindependent.org/20.html
# car emissions per litre: https://people.exeter.ac.uk/TWDavies/energy_conversion/Calculation%20of%20CO2%20emissions%20from%20fuels.htm
# room for improvement, London busses versus other locations.
