from collections import Counter
from collections import Iterable

def count(state):
	al = {}

	for item in state["tmp"]["items"]:
		for key, val in item.items():
			al.setdefault(key, [])

			if isinstance(val, Iterable):
				al[key].extend(val)
			else:
				al[key].append(val)

	for key, val in al.items():
		al[key] = Counter(val)

	state["tmp"].setdefault("analysis", {})
	state["tmp"]["analysis"].setdefault("count", {})
	state["tmp"]["analysis"]["count"].update(al)
