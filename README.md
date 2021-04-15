# Robot Controller
A small program to guide robot along a grid.

## Running the Robot
From your terminal you should run:

`./run.sh`

The robot will then prompt you to input the information needed for the Robot to start on its course.

## Testing
To run unit tests:
`python3 -m unittest test`

## Comments
This was a really interesting assignment. What I found most interesting was the amount of depth I could have explored (given more time). For example: I came up with the simple rule of if a move requires the robot to move outside of the grid, it just throws and error. But I could have the robot respond telling that it was turning around because it reached the edge. Or that it stands still until it gets a valid command. 

Additionally, the instructors assume that the human giving the commands is a good actor. I included a check that the command was actually a command that they could receive, but there are other ways to handle this. You could have the robot ignore a command not in its programming, instead of throwing an error and stopping.

Notably: I didn't have time to build a proper front end. I tried to improve the user experience, by giving informative errors when the input is incorrect. But this is not an ideal situation, and I would have liked to spend more time improving the user interface. 

Other things I thought about but ran out of time for: 

