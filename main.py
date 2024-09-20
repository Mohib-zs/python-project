import requests

response = requests.get("https://api.github.com/users/Mohib-zs/repos")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject URL: {project['html_url']}\n")