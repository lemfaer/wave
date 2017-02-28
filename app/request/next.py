def next(state):
	objs = []

	while True:
		index = state["app"]["current"] + 1
		state["app"]["current"] = index

		if index < len(state["app"]["order"]):
			cls = state["app"]["order"][index]

			mp = map(lambda obj: isinstance(obj, cls), objs)
			mp = list(mp)

			if not any(mp):
				obj = cls(state)
				objs.append(obj)
			else:
				obj = objs[mp.index(True)]

			if obj.need():
				yield obj
		else:
			break

def repeat(state):
	state["app"]["current"] -= 1
