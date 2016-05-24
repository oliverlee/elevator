#!/usr/bin/env python3

import enum
import bisect


class Direction(enum.IntEnum):
    DOWN = -1
    NONE = 0
    UP = 1


class Elevator(object):
    __i = 0

    def __init__(self):
        self.__id = Elevator.__i
        self.__floor = 0
        self.__goal_floors = []
        self.__direction = Direction.NONE
        Elevator.__i += 1

    @property
    def id(self):
        """Returns elevator id."""
        return self.__id

    @property
    def floor(self):
        """Returns current floor of elevator."""
        return self.__floor

    @property
    def goal(self):
        """Returns a list of goal floors."""
        return self.__goal_floors

    @property
    def direction(self):
        """Returns direction elevator to travel in next simulation step or NONE
        if stopped. This is the order of goal floor traversal.
        """
        return self.__direction

    def status(self):
        """Returns a tuple with elevator id, floor, direction, and goal floors.
        """
        return (self.id, self.floor, self.direction, self.goal)

    def update(self):
        raise NotImplementedError

    def pickup_request(self, floor, direction):
        """Add floor to list of goal floors if not already included."""
        if not (direction == Direction.DOWN or direction == Direction.UP):
            raise ValueError('Direction must be Direction.DOWN or Direction.UP')
        if not self.__goal_floors:
            self.__goal_floors = [floor]
            self.__direction = direction # set direction if stopped
        else:
            index = bisect.bisect_left(self.__goal_floors, floor)
            try:
                if self.__goal_floors[index] == floor:
                    # target floor already in list
                    return
            except IndexError:
                pass
            self.__goal_floors.insert(index, floor)
        return

    def step(self):
        if not self.__goal_floors:
            self.__direction = Direction.NONE
            return

        # TODO: Don't search entire list each time
        index = bisect.bisect_left(self.__goal_floors, self.__floor)

        # if goal floor is reached, stop to service floor
        try:
            if self.__floor == self.__goal_floors[index]:
                self.__goal_floors.pop(index)
                return
        except IndexError:
            pass

        # check if current direction is valid and change if not
        if (self.__direction == Direction.UP and
                index > len(self.__goal_floors) - 1):
            self.__direction = Direction.DOWN
        if (self.__direction == Direction.DOWN and index == 0):
            self.__direction = Direction.UP

        self.__floor += self.__direction
        return
