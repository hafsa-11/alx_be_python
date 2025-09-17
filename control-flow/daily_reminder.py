#!/usr/bin/env python3

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority. Please review it."

# Handle time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif priority in ["low", "medium", "high"]:
    message += ". Consider completing it when you have free time."

# Display the final reminder
print("\n" + message)
