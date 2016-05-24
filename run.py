#!/usr/bin/env python3

from elevator import Direction, Elevator

e = Elevator()
print("elevator status: ", e.status())

# Request elevator going up at floor 2, 3
e.pickup_request(2, Direction.UP)
e.pickup_request(3, Direction.UP)

e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())

# Request elevator going down at floor 4
e.pickup_request(4, Direction.DOWN)
e.step()
print("elevator status: ", e.status())

# Request to go to floor 0
e.pickup_request(0, Direction.DOWN)
e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())

e.step()
print("elevator status: ", e.status())
