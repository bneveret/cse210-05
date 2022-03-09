# Cycle Game for CSE 210

## Status: in progress

## Description:
- Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them. The game continues until a player collides with their opponents trail. This project was created for CSE 210 at BYU Idaho.

## Project Structure:
- snake: folder housing all the parts for the game and where the __ main__.py and game design file live.
- __ main__.py: contains our main function utilizing the classes in different files and builds the game window definitions for video_service.py to use in drawing the game.
- game: a folder containing the files for the game to run.
- casting: a folder containing the files for the to create the different interactive pieces of the game.
- directing: a folder containing the files to direct the game including director.py.
- services: a folder containing the files that show and receive information from the user.
- shared: a folder containing the utility files for the any class to use in the game.
- director.py: a file containing all info relating to the "Director" class.
- keyboard_service.py: a file that intereprets user's keyboard input using the "KeyboardService" class.
- video_service.py: a file that draws the game window and shows the user any information they need using the "VideoService" class.
- point.py: a file containing all info relating to the "Point" class.
- color.py: a file containing all info relating to the "Color" class.
- actor.py: a file containing all info relating to the "Actor" class.
- cast.py: a file containing all info relating to the "Cast" class.
- cycle1.py: a file containing all info relating to the "Cycle1" class.
- cycle2.py: a file containing all info relating to the "Cycle2" class.
- score.py: a file containing all info relating to the "Score" class.
- action.py: a file containing all info relating to the "Action" class.
- control_actors_action.py: a file containing all info relating to the "control_actors_action" class.
- draw_actors_action.py: a file containing all info relating to the "Draw_Actors_Action" class.
- handle_collisions_action.py: a file containing all info relating to the "Handle_Collisions_Action" class.
- move_actors_action.py: a file containing all info relating to the "Move_Actors_Action" class.

## Technologies Used:
- The only software required for this program is Python. You can download it here: https://www.python.org
- The collaboration was done via github: https://github.com/nikasparks/cse210-04.git

## How to Start:
- Open __ main__.py file using python 3.

## Game Instructions:
- Players can move up, down, left and right...
- Player one moves using the W, S, A and D keys.
- Player two moves using the I, K, J and L keys.
- Each player's trail grows as they move.
- Players try to maneuver so the opponent collides with their trail.
- If a player collides with their opponent's trail that player loses the  game.

## Acknowledgements:
- Arnaldo Suarez: sua21007@byui.edu
- Camron Erickson: eri20010@byui.edu
- Jonathan Woster: jonathanwoster@gmail.com
- Monika Meyers: nikasparks@mac.com
- Wylee Everett: eve20003@byui.edu