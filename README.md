# Robot Controller
A small program to guide a robot along a grid.

## Running the Robot
First you need to ensure that the file is executable, so within the folder containing the run.sh file input the following:

`chmod 755 run.sh`

Now that you are able to execute the file and start the robot you can do so in the terminal by running:

`./run.sh`

The robot will then prompt you to input the information needed for the Robot to start on its course.

## Testing
To run unit tests:

`python3 -m unittest test`

## Comments
This was a really interesting assignment. What I found most interesting was the amount of depth I could have explored (given more time). For example: I came up with the simple rule for the scenario of a move requiring the robot to move outside of the grid. It throws an error, which prevents it from continuing. But I could have the robot respond telling that it was turning around because it reached the edge. Or the robot could stand still until it gets a valid command. 

Additionally, the instructors assume that the human giving the commands is a good actor, and will only give valid commands. I included a check that the command was actually a command that the robot could receive, but there are other ways to handle this. You could have the robot ignore a command not in its programming, instead of throwing an error and stopping. You could also increase the user interaction, but telling the user the command is incorrect and waiting for better input.

Unfortunately, I didn't have time to build a proper front end. I tried to improve the user experience, by giving informative errors (see `exceptions.py`). But this is not an ideal situation, and I would have liked to spend more time improving the user interface. However, I am a big proponent of the idea "Finished is more important than perfect". This philosophy often wrestles with me desire for clean code and reducing technical debt, but in this case I ran out of time.

Most notably, this task doesn't have any data, making it difficult to assess how a data scientist will perform. While it was a fun and interesting engineering project, I dedicated some time to thinking about how the task could be modified to include machine learning or artificial intelligence. Here is a non-exhaustive list:
* Assume the robot needs to be in a certain space at a certain time. Given data of where the robot is every hour over the course of a year, predict where the robot will be every hour over the course of a week. Create a list of commands that maps the robots predicted moves.
* There are 100 robots, 10 of which are misbehaving. Using movement data from the last month, build a machine learning algorithm which predicts which robots are broken. Deploy the algorithm locally to an API with a plan how you could use this deployed algorithm to identify broken robots in the future.
* You have two battle robots in a grid. With the data collected over 1000 battles, determine if there are traits of the robot, or positions on the grid that are predictive of victory. Use this to predict the upcoming matches, and quantify how much I should bet on each robot.

Thank you for sending and reviewing this! 