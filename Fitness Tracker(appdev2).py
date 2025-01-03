import json
from datetime import datetime

class Workout:
    def __init__(self, name, duration, sets, reps, exercise_type):
        self.name = name
        self.duration = duration  # in minutes
        self.sets = sets
        self.reps = reps
        self.exercise_type = exercise_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display(self):
        return f"{self.name} - {self.exercise_type} | Duration: {self.duration} min | Sets: {self.sets} | Reps: {self.reps} | Date: {self.date}"

class FitnessTracker:
    def __init__(self):
        self.workouts = []
        self.goals = {}

    def add_workout(self, workout):
        self.workouts.append(workout)
        self.save_data()

    def display_workouts(self):
        if not self.workouts:
            print("No workouts recorded yet.")
            return
        print("Workout History:")
        for workout in self.workouts:
            print(workout.display())

    def set_goal(self, goal_name, goal_value):
        self.goals[goal_name] = goal_value
        print(f"Goal set: {goal_name} = {goal_value}")

    def view_goals(self):
        if not self.goals:
            print("No goals set yet.")
            return
        print("Fitness Goals:")
        for goal, value in self.goals.items():
            print(f"{goal}: {value}")

    def check_progress(self):
        total_duration = sum([workout.duration for workout in self.workouts])
        print(f"Total workout duration: {total_duration} minutes")
        for goal, value in self.goals.items():
            print(f"Checking progress for {goal}:")
            if goal == "total_duration":
                print(f"Goal: {value} minutes, Progress: {total_duration} minutes")
            # You can add more progress checks based on different goal types

    def save_data(self):
        data = {
            "workouts": [vars(workout) for workout in self.workouts],
            "goals": self.goals
        }
        with open('fitness_data.json', 'w') as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open('fitness_data.json', 'r') as f:
                data = json.load(f)
                self.workouts = [Workout(**workout) for workout in data["workouts"]]
                self.goals = data["goals"]
        except FileNotFoundError:
            print("No previous data found, starting fresh.")
            return

def main():
    tracker = FitnessTracker()
    tracker.load_data()

    while True:
        print("\nFitness Tracker")
        print("1. Add Workout")
        print("2. View Workouts")
        print("3. Set Fitness Goal")
        print("4. View Goals")
        print("5. Check Progress")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            name = input("Enter exercise name: ")
            duration = float(input("Enter duration (in minutes): "))
            sets = int(input("Enter sets: "))
            reps = int(input("Enter reps per set: "))
            exercise_type = input("Enter exercise type (e.g., Cardio, Strength): ")

            workout = Workout(name, duration, sets, reps, exercise_type)
            tracker.add_workout(workout)

        elif choice == '2':
            tracker.display_workouts()

        elif choice == '3':
            goal_name = input("Enter goal name (e.g., total_duration): ")
            goal_value = float(input(f"Enter target value for {goal_name}: "))
            tracker.set_goal(goal_name, goal_value)

        elif choice == '4':
            tracker.view_goals()

        elif choice == '5':
            tracker.check_progress()

        elif choice == '6':
            print("Exiting the fitness tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
