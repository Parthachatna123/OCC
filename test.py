import requests
import json

def parse_users(users):
	result = ""
	for user in users: 
		result += ("Name - " + user["name"] + "\n" + "Phone - " + user["phone"] + "\n" + "Address - " + str(user["address"]) + "\n\n")
	return result


def parse_comments(comments):
	result = ""
	for comment in comments: 
		result += ("Name - " + comment["name"] + "\n" + "Email - " + comment["email"] + "\n" + "Body - " + comment["body"] + "\n\n")
	return result 


def parse_albums(albums):
	result = ""
	for album in albums: 
		result += ("Title - " + album["title"] + "\n\n")
	return result 

def parse_photos(photos):
	result = ""
	for photo in photos: 
		result += ("Title - " + photo["title"] + "\n" + "URL - " + photo["url"] + "\n\n")
	return result 

def parse_todos(todos):
	result = ""
	for todo in todos: 
		result += ("Title - " + todo["title"] + "\n\n")
	return result
	

def main():
	try:
		sub_domain = input("subdomain: ")
		if sub_domain not in ["users", "comments", "albums", "photos", "todos"]:
			print("Invalid Sub-domain")
			exit()
	except Exception:
		print("Invalid Sub-Domain")
		exit()

	try:
		parsed_data = ""
		data = requests.get("https://jsonplaceholder.typicode.com/" + sub_domain).json()
		if sub_domain == "users":
			parsed_data = parse_users(data)
		elif sub_domain == "comments":
			parsed_data = parse_comments(data)
		elif sub_domain == "albums":
			parsed_data = parse_albums(data)
		elif sub_domain == "photos":
			parsed_data = parse_photos(data)
		elif sub_domain == "todos":
			parsed_data = parse_todos(data)
	except Exception:
		pass

	try:
		if not parsed_data:
			exit()
		with open(f"{sub_domain}.txt", "w") as file:
			file.write(parsed_data)
	except Exception:
		pass



if __name__ == '__main__':
	main()
