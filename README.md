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
each elevator has a different speed!

# The Algorithm:
So we have the calls list and the building that we working with.
first of all if the building have only 1 elevator so its simple. Each call will allocate to the same elevator.
let's talk about what's happening when we have more than 1 elevator.

# Represent Elevator array:
our main thought was how to make sure that all the missions are split close to equaly between the elevators.
We didn't want that there will be a chance that elevator a will have 400 missions, while elevator b will have 30 missions.
We undersood that there is a difference if there were 100 calls or 1000 calls.
And a task with 100 calls with 10 elevators are not the same as a task with 100 calls with 2 elevators!
Let's say 100 calls with 2 elevators. there is a good chance that out of 10 calls it will be smarter for elecator 1 to take them,
so for this case we will fill the "represent elevator array" with 10 numbers of each elevator ([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])

## High Mission Call:
a high misiion call is a call that the different amount of floors between the source floor to the destination floor is high.
but what is it high? maybe amount of floors in the building divide 2?
so a building with 12 floors a high mission call will be a call for more than 6 floors.
But a building with 110 floors it will be more than 55!
of course that a mission of 20+ floors need to be consider as a "high mission call".
so we saw that we need to make a "high mission call" depends on the number of floors in the building.

## Fastest Elevator:
So after we know what it is a "high mission call" we can see that it is very intuative to send this call a FAST elevator.
So if the current call are welcome to the club of the "high mission call" the call will allocate to a fast elevator.

After we know all about above so its kind of simple:
we looking at a call. if the call is a "high mission call" we allocate for this call the fastest elevator from the "represent elevator array".
After we allocate a elevator we will remove one occurence of the number that represent this elevator from the "represent elevator array".
else if the call is not a "high mission call" so we can just allocate the call to one elevator from the "represent elevator array".
as we all can see the "represent elevator array" will get empty! so whenever the array is empty we refilling the array the same way we filled it above.
