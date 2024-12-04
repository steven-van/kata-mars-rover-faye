# Mars Rover Kata

Taken from : https://kata-log.rocks/mars-rover-kata

## Your Task

You’re part of the team that explores Mars by sending remotely controlled vehicles to the surface of the planet. You'll need to write some code to translate the commands sent from earth to instructions that are understood by the rover.

## Requirements

* You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
* The rover receives a character array of commands.
* Implement commands that move the rover forward/backward (f,b).
* Implement commands that turn the rover left/right (l,r).
* Implement wrapping at edges. But be careful, planets are spheres.
* Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point, aborts the sequence and reports the obstacle.

## Instructinos

* Draw an UML architecture by thinking hard about the project (but don't implement anything yet!)
 
 * Try to apply BDD:
    * Find a domain expert
    * Write test scenarios together

* Implement the test scenarios one by one

* Compare your architecture with what you designed
