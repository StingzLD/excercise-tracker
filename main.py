import requests
import os

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = os.environ['NUTRITIONIX_APP_ID']
NUTRITIONIX_API_KEY = os.environ['NUTRITIONIX_API_KEY']
HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
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
                         headers=HEADERS
                         )
response.raise_for_status()
print(response.json())
