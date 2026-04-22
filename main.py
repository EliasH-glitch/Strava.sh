
import time as tm
import sys
from art import text2art
from strava_cz import StravaCZ

intro_text = "Hello, welcome to Strava.sh 🥘"

user_id = "Your_username"
user_password = "Your_password"
user_canteen_num = "Your_canteen_number"

def text_animation(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        tm.sleep(0.04)
    print()
    
def intro_text_ascii():    
    Cool_title = text2art("Strava.sh")
    print(Cool_title)
    print()

def strava_response_request():
    strava_log = StravaCZ(
        username=user_id,
        password=user_password,
        canteen_number=user_canteen_num
    )
    
    print(strava_log.user)

text_animation(intro_text)
intro_text_ascii()
text_animation("User info:")
strava_response_request()


