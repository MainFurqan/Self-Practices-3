"""
🔹 Q5: API Response Storage
✅ Task:

Simulate fetching data from a fake API (use a dictionary).

Convert it to JSON and store it in a file named api_response.json.

Later, read it and display the data.

"""
import json

fake_api_response = {
    "status": "success",
    "code": 200,
    "data": {
        "user": {
            "id": 1,
            "name": "Hamza",
            "email": "hamza@example.com",
            "is_active": True
        }
    }
}

with open("api_response.json","w", encoding="utf-8") as file:
    data = json.dump( fake_api_response, file, indent=4 )

print(json.dumps(fake_api_response, indent=4))