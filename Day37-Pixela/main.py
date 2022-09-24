import requests
import datetime

now = datetime.datetime.now()

pixela_endpoint = 'https://pixe.la/v1/users'
Token = "gharja#marja@123"
Username = "lilpickrat"

user_params = {
    "token": Token,
    "username": Username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Step 2 -  Graphs
graph_endpoint = f"{pixela_endpoint}/{Username}/graphs"

graphs_params = {
    "id": "graphstudy1303",
    "name": "Study Schedule",
    "unit": "hrs",
    "type": "float",
    "color": "ajisai"
}

header1 = {
    "X-USER-TOKEN": Token
}

# graph_response = requests.post(url=graph_endpoint, json=graphs_params, headers=header1)
# print(graph_response)

# Step 3 - Pixels

pixs_end = f"{pixela_endpoint}/{Username}/graphs/{graphs_params['id']}"

pixs_params = {
    "date": f"{now.strftime('%Y%m%d')}",
    "quantity": input("How Many hours did you study today ? "),
}

# pixs_response = requests.post(url=pixs_end, json=pixs_params, headers=header1)
# print(pixs_response)

# Step 4 - Update pixel

up_endp = f"{pixs_end}/{pixs_params['date']}"
up_params = {
    "quantity": "18.6",
    "optionalData": "{\"Day\":\"Phurrr\"}"
}

# up_response = requests.put(url=up_endp, json=up_params, headers=header1)
# print(up_response)

# Step 5- Delete
# up_delete = requests.delete(url=up_endp, headers=header1)
# print(up_delete)