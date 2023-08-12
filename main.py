import requests
import os
from datetime import datetime

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = os.environ['NUTRITIONIX_APP_ID']
NUTRITIONIX_API_KEY = os.environ['NUTRITIONIX_API_KEY']
NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}

SHEETY_ENDPOINT = ("https://api.sheety.co/02cf0db9fdbf9c243cb6bd20502be4be/workoutTracking/workouts")
SHEETY_BEARER_TOKEN = os.environ['SHEETY_BEARER_TOKEN']
SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

GENDER = "male"
WEIGHT_KG = round(180 * 0.45359237, 1)
HEIGHT_CM = round(6 * 12 * 2.54, 1)
AGE = 35

exercises_performed = input("Which exercises did you do?\n")

nutritionix_params = {
    "query": exercises_performed,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT,
                         json=nutritionix_params,
                         headers=NUTRITIONIX_HEADERS
                         )
response.raise_for_status()
data = response.json()
exercise_name = (data['exercises'][0]['name'])
exercise_duration = data['exercises'][0]['duration_min']
exercise_calories = data['exercises'][0]['nf_calories']

datetime_now = datetime.now()
date = datetime_now.strftime("%m/%d/%Y")
time = datetime_now.strftime("%H:%M:%S")

sheety_payload = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise_name.title(),
        "duration": exercise_duration,
        "calories": exercise_calories,
    }
}

response = requests.post(url=SHEETY_ENDPOINT,
                         json=sheety_payload,
                         headers=SHEETY_HEADERS
                         )
response.raise_for_status()
