import config
import setup
from app.conf import stan
from app.request.next import next
from pprint import pprint

# action
state = stan(config, setup)

for req in next(state):
	req.send()

print(len(state["tmp"]["items"]))
pprint(state["tmp"]["items"])
