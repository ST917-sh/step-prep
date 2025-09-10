# Define a function to simulate optimized command execution
import time 
def check_response_time(command):
    """Simulates command execution and measures response time."""
    start_time = time.time()
    if command == "rotate_joint":
        time.sleep(0.15)  # Simulate delay for rotate_joint
    elif command == "move_arm":
        time.sleep(0.1)  # Simulate moderate response time
    elif command == "adjust_grip":
        time.sleep(0.05)  # Simulate fast response time
    response_time = time.time() - start_time
    return response_time


def optimized_command(command, improvement_factor=0.20):
    """Simulates optimized command execution."""
    print(f"Optimizing command: {command}")  # Placeholder action
    optimized_response_time = check_response_time(command) * (1 - improvement_factor)
    return optimized_response_time
print("\nTesting optimized command response times:")
commands=["rotate_joint","move_arm","adjust_arm"]
for cmd in commands:
    optimized_time = optimized_command(cmd)
    print(f"{cmd} optimized response time: {round(optimized_time, 3)} seconds")
    