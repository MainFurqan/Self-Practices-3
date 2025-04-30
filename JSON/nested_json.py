"""
You are given a JSON response from an API:

json
{
  "status": "success",
  "data": {
    "user": {
      "id": 1,
      "username": "furqan123",
      "email": "furqan@example.com"
    }
  }
}
✅ Task:

Extract and print the username and email.

"""
import json

with open("such_API_response.json", "r") as file:
    data = json.load(file)

# Option_1:
username = data["data"]["user"]["username"]
email = data["data"]["user"]["email"]

# Option_2:
"""
user = response.get("data", {}).get("user", {})
username = user.get("username", "N/A")
email = user.get("email", "N/A")
"""

print(f"username : {username}")
print(f"Email : {email}")