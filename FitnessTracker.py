# Task 1: Develop a function to log different fitness activities and their duration

def log_activities(activities, durations):
    if len(activities) != len(durations):
        print("Error: Number of activities does not match number of durations.")
        return None
    log = {}
    for activity, duration in zip(activities, durations):
        log[activity] = duration
    return log

# Task 2: Write a simple function that estimates calories burned based on the activity and duration

def calculate_calories_burned(duration):
    return duration * 3.5

# Task 3: Create a summary function that provides a report of all activities and total calories burned for the day

def generate_summary(log):
    total_calories = 0
    print("Fitness Activities Log:")
    for activity, duration in log.items():
        calories_burned = calculate_calories_burned(duration)
        total_calories += calories_burned
        print(f"{activity}: {duration} minutes, Calories Burned: {calories_burned}")
    print("Total Calories Burned for the Day:", total_calories)
def main():
    activities = ['Dancing', 'Swimming', 'Biking']
    durations = [10, 20, 15]
    
    # Task 1: Log activities
    activity_log = log_activities(activities, durations)
    
    # Task 3: Generate summary
    generate_summary(activity_log)

if __name__ == "__main__":
    main()
