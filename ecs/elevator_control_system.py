#!/usr/bin/env python3

__all__ = ['ElevatorControlSystem']

from .elevator import Direction, Elevator


class ElevatorControlSystem(object):
    def __init__(self, num_elevators):
        self.elevators = [Elevator() for i in range(num_elevators)]

    def pickup_request(self, floor, direction):
        """Add a goal floor to one of the elevators."""
        if not (direction == Direction.DOWN or direction == Direction.UP):
            raise ValueError("Direction must be UP or DOWN.")

        #TODO: do something less stupid here
        for e in self.elevators:
            if (direction == e.direction and
                direction*floor > e.direction*e.floor):
                e.pickup_request(floor, direction)
                return
        for e in self.elevators:
            if (e.direction == Direction.NONE):
                e.pickup_request(floor, direction)
                return
        for e in self.elevators:
            if direction == Direction(-1 * e.direction):
                e.pickup_request(floor, direction)
                return
        self.elevators[-1].pickup_request(floor, direction)

    def step(self):
        """Simulate one step for all elevators."""
        for e in self.elevators:
            e.step()
        return

    def print_status(self):
        print("status: id, floor, direction, goal floors")
        for e in self.elevators:
            print(e.status())
        return






