#!/usr/bin/env python3

from ecs import Direction, ElevatorControlSystem

class Rider(object):
    def __init__(self, floor, goal):
        self.floor = floor
        self.goal = goal

    @property
    def direction(self):
        return Direction((self.goal - self.floor)/abs(self.goal - self.floor))

    def can_board(self, elevator):
        if ((elevator.direction == self.direction or
             elevator.direction == Direction.NONE) and
            (elevator.floor == self.floor)):
            return True


ecs = ElevatorControlSystem(4)

# 4 pickup requests at floors 1, 2, 3
riders = [Rider(1, 5), Rider(2, 0), Rider(3, 5), Rider(1, -2)]
# and a rider steps into elevator 0 at floor zero and goes towards floor -2
ecs.elevators[0].pickup_request(-2, Direction.DOWN)

# riders request elevators
for r in riders:
    ecs.pickup_request(r.floor, r.direction)
print("rider requests")
ecs.print_status()
print("")

j = 0
while True:
    # if rider enters elevator, add the goal floor for that rider/elevator
    for e in ecs.elevators:
        for i in range(len(riders) - 1, -1, -1):
            r = riders[i]
            if r.can_board(e):
                e.pickup_request(r.goal, r.direction)
                riders.pop(i)
    ecs.step()
    print("step", j, "riders waiting: ", len(riders))
    ecs.print_status()
    print("")
    j += 1
    if all(e.direction == Direction.NONE for e in ecs.elevators):
        break
