import requests
import json

USERNAME = "anamikajayan"

url = f"https://api.github.com/users/{USERNAME}/repos"

res = requests.get(url)
repos = res.json()

projects = []

for r in repos:
    projects.append({
        "name": r["name"],
        "url": r["html_url"],
        "description": r["description"],
        "stars": r["stargazers_count"]
    })

with open("projects.json", "w") as f:
    json.dump(projects, f, indent=4)

print("Done: projects.json created")