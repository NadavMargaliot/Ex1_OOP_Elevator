# Ex1_OOP_Elevator
second assignment 



The task of this program is to allocate a call for elevator to the "best" elevator. 
the main target of this project is to minimize the average waiting time for a elevator per person.
we will deal with a offline case, which means we are getting all the calls for the elevator before we starting to allocate a call.
This situation is diffrent than the last project when it was online case.



so the program basicly gets a json file representing a building, and csv file representing calls list.
first we making a Building from the json file, and Calls list from the csv file.

the main details in each class:
Calls - the time of the call , source floor , destination floor.
Building - minimum floor , maximum floor , elevators.
Elevator - speed , minimum floor , maximum floor, close time door and more details.

## The algorithm:
So we have the calls list and the building that we working with.
first of all if the building have only 1 elevator so its simple. Each call will allocate to the same elevator.
let's talk about what's happening when we have more than 1 elevator.
we will create a array with all the numbers of the elevators in the building.

# high mission call:
a high misiion call is a call that the different amount of floors between the source floor to the destination floor is high.
but what is it high? maybe amount of floors in the building divide 2?
so a building with 12 floors a high mission call will be a call for more than 6 floors.
But a building with 110 floors it will be more than 55!
of course that a mission of 20+ floors need to be consider as a "high mission call".
so we saw that we need to make a "high mission call" depends on the number of floors in the building.

