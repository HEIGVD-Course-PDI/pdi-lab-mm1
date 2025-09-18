"""Perform simulation of a M/M/1 queueing system using SimPy."""
import simpy
import models.simpy_m_m_1 as simpy_mm1

ARRIVAL_RATE = 10.0  # Arrival rate (clients per second)
SERVICE_RATE = 50.0  # Service rate (clients per second)
SIM_DURATION = 10_000  # Duration of the simulation (seconds)

# Create the SimPy environment and the server
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)

# Create the M/M/1 queueing system
mm1Queue = simpy_mm1.SimpyQueue(env, server, ARRIVAL_RATE, SERVICE_RATE)

# Start the request generator and the statistics recorder
env.process(mm1Queue.generate_requests())
env.process(mm1Queue.record_statistics(sampling_interval=1.0))

# Run the simulation
env.run(until=SIM_DURATION)

# Compute and print the statistics
mean_response_time, mean_clients_in_system = mm1Queue.compute_statistics()
print(f"Mean response time: {mean_response_time:.4f} seconds")
print(f"Mean number of clients in the system: {mean_clients_in_system:.4f}")
