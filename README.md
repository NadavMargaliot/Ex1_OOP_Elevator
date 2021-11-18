# Ex1_OOP_Elevator
second assignment 

# Offline Algorithm Foe Elevators
The task of this program is to allocate a call for an elevator to the "best" elevator. 
The main target of this project is to minimize the average waiting time for an elevator per person.
We will deal with an offline case, which means we are getting all the calls for the elevator before we are starting to allocate a call.
This situation is diffrent than the last project when it was an online case.

So the program basicly gets a json file which represents a building, and a csv file which represents a calls list.
First we make a Building from the json file, and a Calls list from the csv file.

The main details in each Object:
Call - the time of the call , source floor , destination floor.
Building - minimum floor , maximum floor , elevators.
Elevator - speed , minimum floor , maximum floor and more.
Each elevator has a different speed!

## The Algorithm:
So we have the calls list and the building that we are working with.
First of all if the building only has 1 elevator so it's simple. Each call will allocate the same elevator.
Let's talk about what's happening when we have more than 1 elevator.

### Represent Elevator Array:
Our main thought was how to make sure that all the missions are split close to equaly between the elevators.
We didn't want there to be any chance that elevator 'a' will have 400 missions, while elevator 'b' has 30 missions.
We undersood that there is a difference if there are 100 calls or 1000 calls.
And a task with 100 calls with 10 elevators are not the same as a task with 100 calls with 2 elevators!
Let's say there is 100 calls with 2 elevators. There is a good chance that out of 10 calls it will be smarter for elevator 1 to take them,
so for this case we will fill the "represent elevator array" with 10 numbers of each elevator [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] (10 times).
Let's say there is 100 calls with 10 elevators. so the "represent elevator array" will be filled with [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9] (twice).

### High Mission Call:
High mission call is a call that the different amount of floors between the source floor to the destination floor is high.
But what is considered high? maybe the amount of floors in the building is divided by 2?
So for a building with 12 floors a high mission call will be a call for more than 6 floors.
But for a building with 110 floors it will be more than 55 floors!
Of course that a mission of 20+ floors needs to be considered as a "high mission call".
So we saw that we need to make a "high mission call" depending on the number of floors in the current building.

### Fastest Elevator:
So after we know what a "high mission call" is, we can see that it is very intuative to send this call a FAST elevator.
Now if the current call is considered a "high mission call" the call will allocate the fastest elevator from the "represent elevator" array.

After we know about all the above its kind of simple:
We are looking at a call. If the call is a "high mission call" we allocate this call to the fastest elevator from the "represent elevator" array.
Each time we allocate an elevator we'll remove one occurrence of the number that represents this elevator from the "represent elevator" array.
Otherwise the call is not a "high mission call" and then we can just allocate the call to one elevator from the "represent elevator" array.
As we can see the "represent elevator" array will become empty! Now whenever the array is empty we'll refill the array the same way as it wasfilled above.
With this program we can be sure that a call will always have an elevator to allocate to.

Diagram of the classes:
![WhatsApp Image 2021-11-18 at 20 26 18](https://user-images.githubusercontent.com/84914845/142474852-654ee94e-9bfa-4e54-8d97-547f3414a705.jpeg)


