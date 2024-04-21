# Task 1 Code Correction

attendees = int(input("Enter number of attendees: "))
# Added int() function because you can't have a fraction of a person
venue = "Large Hall" if attendees >= 50 else "Conference Room"
print(f"Given there are {attendees} attendees, the appropriate venue is {venue}")
'''
I modified the if statement by shrinking the comparison point to 50 and making it a greater 
than or equal to operator to bring it more in line with the size of an actual conference room.
I also modified the print statement by converting it into a f string where the 
number of attendees is listed and stating what the appropriate venue is for that size party.
The actual syntax to assign the variable was actually correct in the original code of the conditional
'''

# Task 2 Venue Selection

audio_visual_equipment = "Audio System" if attendees < 50 else "Projector"
print(f"Given there are {attendees} attendees and they will be in the {venue}, the {audio_visual_equipment} is right for that room.")
'''
I added another shorthand if statement that assigns an Audio System to 
parties with less than 50 attendees (parties that will be in the Conference Room)
and assigned a projector for parties of 50 or more as those will be in the Large Hall.
I lastly added an updated f string print statement to convey this information to the user.
'''

# Task 3 Catering Choices

food_preference = input("Do you want vegetarian food catered? (yes/no): ")
caterer = "Veggie Delight Caterers" if food_preference == "yes" else "Gourmet Meals Caterers"
print(f"Given the preference listed regarding vegetarian friendly catering options, we recommend {caterer} for your event.")

'''
The initial input gives a yes/no prompt for the end user to list if there will be a need
for vegetarian food, and a subsequent shorthand conditional is written to assign an 
appropriate caterer based off of that response. Lastly a f string is used in the print 
statement to communicate the final catering recommendation to the user.
'''