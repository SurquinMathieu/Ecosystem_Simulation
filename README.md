# Ecosystem_Simulation
Simulation of a simplified ecosystem

This program requires pygame in order to run properly. Once you are ready, run the 'main.py' file.

The solid principles: 

1. Liskov substitution principle
This means that when an instance of a class is extended to another class, the inheriting class should have a use case for all the properties and behavior of the inherited class. 
In my case, you can see for example that the living class (which contain methods like inArea, digest, eat,...) is a superclass of both carnivores and herbivores classes. These child classes actually use the methods of the superclass.

2. Open closed principle
This means that software entities should be open for extension, but closed for modification. Classes should be created in a way that their core functionalities can be extended to other entities without altering the initial entity's source code.
In this ecosystem simulation, we can easily add or delete animals, plants, objects and so on without having to modify the rest of the code.
