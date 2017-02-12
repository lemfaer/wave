# config
import config
import setup
from app.conf import stan

# request
from app.request import *


# action
state = stan(config, setup)
country = country.CountryGet(state)
print(country.url())
