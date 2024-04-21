# Task 1 Code Correction

place = input("Choose a place (forest or cave): ")
action = input("Choose an action if you're in the forest (climb a tree or cross a river): ")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
else:
    print("You find a hidden treasure!")


'''
The first major change I implemented to debug this code was removing the action input
from any part of the nested if statement and assigning it prior to the conditionals 
being executed. I also changed the wording and presentation of the input's slightly 
to make it easier for the user to put executable input. Inside the nested if statement 
itself I changed both if statements to == so it acts as a comparison rather an assignment.
I also eliminated any syntax after the initial else statement to avoid syntax errors 
and modified the last elif statement to an else statement to create a default if the cave 
is chosen regardless of action.
'''

# Task 2 Setting the Scene
print("\n") # added a line to help separate code from Task 1 from Task 2

place = input("Choose a place (forest or cave): ")
forest_action = input("Choose an action if you're in the forest (N/A, climb a tree, or cross a river): ")
cave_action = input("Choose an action if you're in the cave (N/A, light a torch, or proceed in the dark): ")

if place == "forest":
    if forest_action == "climb a tree":
        print("You found a bird's nest!")
    elif forest_action == "cross a river":
        print("You found a boat!")
    else:
        print("Be sure that your place selected matches the actions inputs selected!")
else:
    if cave_action == "light a torch":
        print("You found a treasure chest covered in ants!")
    elif cave_action == "proceed in the dark":
        print("You are safe from danger but struggle to find the chest.")
    else:
        print("Be sure the place you selected matches the actions inputs selected")

'''
After being careful to separate code form Task 1 to Task 2, I added a decision path 
under else to account for actions taken in the cave.I also modified the original nested 
else into an elif and added path's for incorrectly chosen N/A's if the user chooses forest 
or river but fails to enter an appropriate action.
'''

# Task 3 Default Path

print("\n") # added a line to help separate code from Task 2 from Task 3

place = input("Choose a place (forest or cave): ")
forest_action = input("Choose an action if you're in the forest (N/A, climb a tree, or cross a river): ")
cave_action = input("Choose an action if you're in the cave (N/A, light a torch, or proceed in the dark): ")

if place == "forest":
    if forest_action == "climb a tree":
        print("You found a bird's nest!")
    elif forest_action == "cross a river":
        print("You found a boat!")
    else:
        pass
else:
    if cave_action == "light a torch":
        print("You found a treasure chest covered in ants!")
    elif cave_action == "proceed in the dark":
        print("You are safe from danger but struggle to find the chest.")
    else:
        pass

'''
I created the N/A path in Task 2 before I had read the task for Task 3. 
Because of that and the planning I had accounted for with incorrect user choices, 
all I had to do was change the print statements in both nested elses' that alerted 
the user of their input error into pass statements instead.
'''