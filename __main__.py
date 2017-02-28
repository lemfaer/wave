import config
import setup
from time import time
from pprint import pprint
from app.conf import stan
from app.request.next import next

# action
state = stan(config, setup)

for req in next(state):
	st = time()
	req.send()
	end = time()
	print(req, end - st)

print(len(state["tmp"]["items"]))
pprint(state["tmp"]["items"])
