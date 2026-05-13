
import time as tm
import sys
from art import text2art
from strava_cz import StravaCZ, AuthenticationError, MealType, InvalidMealTypeError, InsufficientBalanceError
import os
from dotenv import load_dotenv

intro_text = "Hello, welcome to Strava.sh 🥘"

load_dotenv()
user_id = os.getenv("STRAVA_USERNAME")
user_password = os.getenv("STRAVA_PASSWORD")
user_canteen_num = os.getenv("STRAVA_CANTEEN_NUMBER")

global strava_log 
strava_log = "any data"

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
    

    except AuthenticationError as error_mes:
        print(f"Login failed: {error_mes}")
    
    
def Logout():
    
      strava_log.logout()
      text_animation("Your are loged out now 🤓")

def ordered_meal():

    text_animation("These are your ordered meals:")
    
    strava_log.menu.fetch()
    ordered_meals = strava_log.menu.get_meals(meal_types=[MealType.MAIN], ordered=True)
    soups = strava_log.menu.get_meals(meal_types=[MealType.SOUP])

    position = 0

    for meal in ordered_meals:
        name = meal["name"]
        date = meal["date"]
        soup_dict = soups[position]
        soup = soup_dict["name"]
        print(f"Date:{date}:\n Soup: {soup}\n Meal name: {name}")
        position += 1

def jidelnicek_vypsani():

    strava_log.menu.fetch()
    strava_log.menu.print()

def order_food():
    text_animation("This is full menu:")
    jidelnicek_vypsani()
    id_to_order = int(input("Which meal by ID (the fist number) u want to order:\n"))

    if strava_log.menu.is_ordered(id_to_order):
        text_animation("Meal is already ordered")
    
    else:
        try:
            strava_log.menu.order_meals(id_to_order)
            text_animation("Meal is now ordered")
        except InvalidMealTypeError as error:
            print(f"Error: {error}")
        except InsufficientBalanceError as error:
            print(f"Error: {error}")


strava_response_request()
text_animation(intro_text)

while True:
    
    intro_text_ascii()

    action = int(input(f"What u want to know??\n1. Account info\n2. Ordered food only\n3. All the food items\n4. Order food\n5. Logout\n"))

    if action == 1:
        print(strava_log.user)

    elif action == 2:
        ordered_meal()
    
    elif action == 3:
        jidelnicek_vypsani()

    elif action == 4:
        order_food()

    elif action == 5:
        Logout()
        break

    else:
        print("Try again")