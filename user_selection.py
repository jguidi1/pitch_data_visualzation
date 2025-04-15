import pybaseball as pyb


users_pitcher_firstname = input("Enter the first name of your desired pitcher: ")
users_pitcher_lastname = input("Enter the last name of your desired pitcher: ")
player_id = pyb.playerid_lookup(users_pitcher_lastname, users_pitcher_firstname)
print("nice!" + str(player_id))
while True:
    users_pitcher_firstname = input("Enter the first name of your desired pitcher: ")
    users_pitcher_lastname = input("Enter the last name of your desired pitcher: ")
    player_id = pyb.playerid_lookup(users_pitcher_firstname, users_pitcher_lastname)
    print("nice!" + str(player_id))
    continue_prompt = input("Do you want to look at another pitcher? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        break

