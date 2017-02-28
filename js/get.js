var params = {python_params},
	users = {pyhton_users},
	index = users.length,
	res = [],
	user,
	item;

while (index > 0) {{
	index = index - 1;
	user = users[index];
	params.user_ids = user;
	item = API.users.get(params);
	res.push(item);
}}

return res;
