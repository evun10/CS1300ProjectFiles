CS 1300 
Project Using Files, 100 pts.

Objectives
Demonstrate the ability to apply basic Python programming concepts learned throughout the semester in the development of a simple application.
Specifications
The project is broken into three parts.
Part 1 is worth 84 points. Parts 2 is worth 16. You are not required to complete Part 2 . However, if you only do Part 1 the maximum you can earn is 84/100. Part 2 will be a more difficult than Part 1. Part 2 will not be graded if you do not earn 60 of the 84 points on Part 1. 
Requirements
Getting started
1.	Download the file AtlantaTemps2017.csv which will be the file that this project will read
data from. Make sure to store this file in the same folder where your Python file is located.
a. The AtlantaTemps2017.csv file is a CSV file that has temperature data for Atlanta for 2017. The data on each line is stored in the following format:
day,high,low 
For example, the line: 6/19/2017,88,71 is the day June 19th, 2017 and on that day there was a low temp of 71 and a high temp of 88 degrees Fahrenheit.
2.	Start IDLE.
3.	Create a new Python program file named: FirstnameLastnameProjectFiles.py, e.g.,
SallyWhiteProjectFiles.py.
4.	Define a main function that will be the entry point and control for the program.
a. Remember as you are writing functionality you will need to write helper functions to help implement the various requirements.
5.	Within the main function body add a print statement that will print out Project Files by your name, e.g., Project Files by Sally White.

Part 1 – Basic stats for all temperature data stored in file
1. Add functionality that for the data stored in the file the program can determine and display the following:
a. The highest temperature of the year.
b. The lowest temperature of the year.
c. The lowest high temperature of the year.
d. The highest low temperature of the year.
e. The average high temperature for the year.
f. The average low temperature for the year.
g. The number of low temps below a threshold value where you prompt the user for the threshold value.
h. The number of high temps above a threshold value where you prompt the user for the threshold value.

2. This completes the requirements for Part 1 of the project, so add a comment at the top of the
file that states you: Successfully completed Part 1 of the project. If you didn’t complete
all of Part 1, then in the comment state what you did complete.

3. I would encourage you to upload what you have completed to Moodle. I would also suggest keeping a backup of this file.

4. If you successfully completed all of Part 1 and you so desire, you may proceed onto Part 2 of
the project.

Part 2 – Adding the date of occurrence and a monthly breakdown of the stats (16 pts.)
1. Modify the output for part 1, for the high and low temp of the year and the lowest high temp and highest low temp to also display the day that it occurred on.
Example format for this output is below: (Real data is not used below.)
The highest temp was 96 and occurred on 8/12/2017.
The lowest temp was 9 and occurred on 2/11/2017.
The lowest high temp was 29 and occurred on 2/10/2017.
The highest low temp was 74 and occurred on 7/29/2017.
2. After the output for part 1, display a monthly breakdown of the following stats for each month.
a. The output for each month must be preceded by the name of the month.
b. The highest temperature of the month and the day it occurred on.
c. The lowest temperature of the month and the day it occurred on.
d. The average high temperature for the month.
e. The average low temperature for the month.

Example output: (Real data not used.)
January
Highest temp: 56 occurred on 1/12/2017
Lowest temp: 5 occurred on 1/27/2017
Average high: 40.8
Average low: 25.4
February
Highest temp: 61 occurred on 2/15/2017
Lowest temp: 12 occurred on 2/2/2017
Average high: 45.3
Average low: 29.125
March
Highest temp: 78 occurred on 3/25/2017
Lowest temp: 24 occurred on 3/8/2017
Average high: 51.387
Average low: 35.105
…

3. Make sure all your code adheres to the SRP and DRY principles.

4. This completes the requirements for Part 2 of the project, so add a comment at the top of the file that states you: Also, successfully completed Part 2 of the project. If you didn’t complete all of Part 2, then in the comment state what you did complete.

5.sumbit your completed file

