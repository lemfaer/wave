var params = {python_params},
	users = {pyhton_users},
	index = users.length,
	res = [],
	user,
	item;

while (index > 0) {{
	index = index - 1;
	user = users[index];
	params.user_id = user;
	item = API.groups.get(params);
	item.id = user;
	res.push(item);
}}

return {{ items : res }};
