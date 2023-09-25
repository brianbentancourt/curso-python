import requests


token = "132456"
headers = {
    "Authorization": f"Bearer {token}"
}

# GET
# url = "https://jsonplaceholder.typicode.com/users"

# r = requests.get(url=url, timeout=10, headers=headers)
# # print(
# #         r.status_code,
# #         r.text,
# #     )

# r = r.json()

# for user in r:
#     print(user["name"])


# POST
url = "https://jsonplaceholder.typicode.com/users"

user = {
    "name": "User456"
}
r = requests.post(url=url, timeout=10, data=user, headers=headers)
print(r.status_code)
