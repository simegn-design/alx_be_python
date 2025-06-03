task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        msg = f"Reminder: '{task}' is a high priority task"
    case "medium":
        msg = f"Reminder: '{task}' is a medium priority task"
    case "low":
        msg = f"Note: '{task}' is a low priority task"
    case _:
        msg = task

print(f"{msg} that requires immediate attention today!" if time_bound == "yes" else f"{msg}. Consider completing it later.")
