
import time as tm
import sys
from art import text2art
from strava_cz import StravaCZ, AuthenticationError, MealType
import os
from dotenv import load_dotenv

intro_text = "Hello, welcome to Strava.sh 🥘"

load_dotenv()
user_id = os.getenv("STRAVA_USERNAME")
user_password = os.getenv("STRAVA_PASSWORD")
user_canteen_num = os.getenv("STRAVA_CANTEEN_NUMBER")

strava_log = ""

def text_animation(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        tm.sleep(0.04)
    print()
    
def intro_text_ascii():    
    Cool_title = text2art("Strava.sh")
    print(Cool_title)

def strava_response_request():
    global strava_log
    try:
        strava_log = StravaCZ(
        username=user_id,
        password=user_password,
        canteen_number=user_canteen_num
        )
    
        print(strava_log.user)
        print()

    except AuthenticationError as error_mes:
        print(f"Login failed: {error_mes}")
    
    
def Logout():
      global strava_log
      strava_log.logout()

def ordered_meal():
    text_animation("These are your ordered meals:")
    
    strava_log.menu.fetch()
    ordered_meals = strava_log.menu.get_meals(meal_types=[MealType.MAIN], ordered=True)

    for meal in ordered_meals:
        name = meal["name"]
        date = meal["date"]
        print(f"Date:{date}, Meal name:{name}")



text_animation(intro_text)
intro_text_ascii()
strava_response_request()
ordered_meal()

Logout()