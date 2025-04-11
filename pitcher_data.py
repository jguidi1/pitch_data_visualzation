from pybaseball import statcast_pitcher
from datetime import date
from pybaseball import playerid_lookup

# Get data for Gerrit Cole (pitcher ID: 543037) from a single game or range
#data = statcast_pitcher('2023-06-01', '2023-06-01', 543037)

def player_lookup(firstname, lastname):# Last name, first name
    data = playerid_lookup("'"+ lastname +"'", "'"+ firstname +"'")
    return data

input_firstname = input("Enter the pitcher's first name: ")
input_lastname = input("Enter the pitcher's last name: ")
data = player_lookup(input_firstname, input_lastname)
print(data.head())