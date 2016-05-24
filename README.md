#ELEVATOR CONTROL SYSTEM
This project implements a simple elevator control system.

An `ElevatorControlSystem` implements a set of `Elevator`s. It will dispatch
elevators to floors as riders request them. Once a rider boards, he can then
select the desired floor. See `run.py` for a simple example.

## Scheduling
A simple scheduling algorithm is used by the control system to dispatch
individual elevators.

1. Check if an elevator is already moving in the same direction and hasn't yet
   passed by the waiting rider, stop by the waiting rider's floor.
2. Otherwise, dispatch a stopped elevator.
3. Lastly, simply dispatch an elevator moving in the opposite direction.

This improves upon first-come, first-served order as elevators already traveling
in the direction of a waiting rider will stop along the way.
