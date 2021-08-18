Running the app:
Create a database called "travel_emissions"
Within the project files folder, run "psql -d travel_emissions -f db/travel_emissions.sql"
Run "python3 console.py" to initiate the program and pre-populate some values
type "flask run" into the console which will allow you to open up the app in chrome.


Carbon Travel Tracker
Build an app that allows a user to track their carbon emissions through travel.

MVP
The app should allow the user to create and edit transport types (merchants), e.g. Car, bus, rail.
The app should allow the user to create and edit travel purpose (tags) for their spending, e.g. to/from work, for work, leisure.
The user should be able to assign purposes (tags) and types (merchants) to a journey, as well as the distance travelled. This will then be converted to a journey emission.
The app should display all the journeys a user has made in a single view, with each journey's emission, type and purpose, and a total emission.
Inspired by:
Monzo, MoneyDashboard, lots of mobile/online banking apps

Possible Extensions
The user should be able to mark transport types and purposes as deactivated. Users will not be able to choose deactivated transports/types when creating a journey.
Journeys should have a timestamp, and the user should be able to view journeys sorted by the time they took place.
The user should be able to supply a target emission cap, and the app should alert the user somehow when when they are nearing this cap or have gone over it.
The user should be able to filter their view of journeys, for example, to view all journeys in a given month, or view all emissions from going to work.


Some sources for data used (also held within the files where it is used as comments):

plane CO2e = 145 g/mile
rail CO2e = 56.5g/mile
bus CO2e = 100g/mile
petrol car = 2.3 kg CO2/litre = 10.45 kg CO2/gallon
diesel car = 2.7 kg CO2/litre = 12.27 kg CO2/gallon

plane CO2e emissions is 90g/RPK (revenue passenger kilometer) globally on average: https://theicct.org/sites/default/files/publications/CO2-commercial-aviation-oct2020.pdf
rail CO2e emissions is 35.1g/km: https://dataportal.orr.gov.uk/media/1843/rail-emissions-2019-20.pdf
bus CO2e emissions: https://www.carbonindependent.org/20.html
car emissions per litre: https://people.exeter.ac.uk/TWDavies/energy_conversion/Calculation%20of%20CO2%20emissions%20from%20fuels.htm
room for improvement, London busses versus other locations.
Tree offset figure = 10kg/year https://granthaminstitute.com/2015/09/02/how-much-co2-can-trees-take-up/
