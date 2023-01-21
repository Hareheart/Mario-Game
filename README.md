# Ghoul Harvester
This game, created by the brilliant minds of Hareheart and Blaze, is a history inspired game designed for the evident pleasure of stressed students and workers. Enjoy!


### David's README
#### Video:

#### Program Functionality:
##### What does it do? This RPG, Ghoul Harvester, is a Python-structured game written in Pygame. Similarly to Mario, it features a pixelated character that defeats enemies to win the game. The game includes a single map that contains obstacles for the player to overcome and enemies at a regular basis across the map to stop the player from winning. The enemies come in different types (boss, mini-boss, and normal enemy), and they are regulated at a standard tempo and programmed as NPCs whereas the player can be controlled and affected by the user.
##### Who is it designed for? Although this game is quite irrelevant to our society and does not by any means function as a program that solves a real-world problem, it has the purpose of entertaining any audiences that wish to relieve stress by playing a pleasingly challenging game. This game can be applied to any audience group that wishes to relieve stress by playing video games.

#### New Skills
##### A new skill I learned while working on this project was classes, which was quite useful considering how important they were to the game and its functionality. Essentially, I learned that classes essentially function as blueprints, a specific layout for creation of objects to follow. The class includes the built-in __init__() function that initializes values or specific information to the object, and methods, other functions, are added after it to modify the class itself. In our example, the characters all have classes to give them specific attributes and allow us to reuse the same code for multiple objects.


###### Source about classes: https://www.w3schools.com/python/python_classes.asp
#### Data Abstraction
##### An example of data abstraction used in the program is the __init__() function and the specific attributes that is assigned to the object. The reason this can be considered data abstraction is that the initial attributes are later called and used in the methods that give the object its abilities.
<img width="482" alt="image" src="https://user-images.githubusercontent.com/89731534/213749577-98c235d7-cc45-4d9d-b2d0-5887703c7fda.png">
<img width="373" alt="image" src="https://user-images.githubusercontent.com/89731534/213749335-3de95844-ab42-4a83-9b51-8508d175f4de.png">

##### In this example, the Player class is given a speed value stating "self.speed = 3" basically assigning that value to the class to be used in a method. Later in the class, in the second picture, the attribute is used in the movement method, where if the left and right arrow keys are pressed, the player moves horizontally by the speed value.
##### This abstraction is necessary and much more efficient in comparison to other methods because it is easier to run the file and reference them outside of it, so before we implemented this, the code was much more difficult to run compared to before. Storing the value in a class also means we can use one line of code to implement it.

#### Procedural Abstraction
<img width="413" alt="image" src="https://user-images.githubusercontent.com/89731534/213758840-b4fe6545-de44-44cb-8c9a-e248f7a3f434.png">

##### Procedure
###### The procedure part in this code segment is the first line that initializes the function/method as "movement" and takes arguments by passing self, speed, position, and gravity, which means these variables that were initialized in the __init__() function can be used in the method itself.

##### Algorithm
###### Sequencing: Sequencing is used in this segment as the program constantly progresses through each line and runs it from top to bottom. It first defines keys_pressed, then it increases the value of gravity and adds it to the player's y-position, and then it checkes whether a key is being pressed, and if so, it moves the player by a certain amount. It follows a clear path throughout the code, hence the term sequencing.

###### Selection: Selection is used in the if-statements of the segment, where if the left or right arrow key is currently being pressed by the user, then the player's x position changes. In other words, an action only progesses if a certain condition is met, hence the term selection.

###### Iteration: Iteration is used when the actual method is called in the update method, where the iteration (looping) takes place.
<img width="172" alt="image" src="https://user-images.githubusercontent.com/89731534/213765547-c13c43a2-9415-4c6e-9960-4a326c4ce245.png">

###### The method is being called in the update method which is referenced 

##### Procedural Abstraction helps manage complexity in my code due to the organization that allows me to call the function/method in the update instead of having to write the actual code in the update, which would be a lot less readable. If I were to replace all the methods I call in the update method with the code it contained, there would be an unnecessary amount of lines of code, whereas using Procedural Abstaction, the reader can refer back to each individual method and the code would be a lot more readable.



### Matthew's README
