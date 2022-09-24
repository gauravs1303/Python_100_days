import requests
import datetime as dt

now = dt.datetime.now()
day = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M:%S")

APP_ID = "8da152ea"
API_KEY = "ff73774a7d3a40c7ffcc6af46112e69c"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exeercise_ep = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
     "query": "90sec sit ups 12 min run & 13min pull up, 10 reps dumbels",
     "gender": "female",
     "weight_kg": 97,
     "height_cm": 188,
     "age": 23
}

# Posting the Data
response = requests.post(url=exeercise_ep, json=exercise_params, headers=header).json()
# List of dictionary from json data received from website's NLP
data_list = [{"ex": n["name"], "dur": n["duration_min"], "cal": n["nf_calories"]} for n in response['exercises']]

# Posting to Google sheets
sheet_postep = 'https://api.sheety.co/3499cae0f127abe9e31d07b033a9af24/myWorkouts/workouts'

workout = [{"date": day, "time": time, "exercise": n["ex"], "duration": n["dur"], "calories": n["cal"]}
           for n in data_list]

# tkon = {
#     "Authorization": "Basic am9objpCWkUobzIhNnNZVCNRITVN"
# }


# for item in workout:
#     sheet_params = {
#         "workout": item
#     }
#     print(sheet_params)
#     requa = requests.post(url=sheet_postep, json=sheet_params)
#     requa.raise_for_status()
#     print(requa.json())

# Deleting
# res_del = requests.delete(url=f"{sheet_postep}/4")
# print(res_del)