"""
-------------------------------------------------
Title   : GradeBook Analyzer
Author  : Lokesh Verma
Course  : Programming for Problem Solving using Python
-------------------------------------------------
Description:
A command-line tool to input or import student marks,
analyze grades, compute statistics, and generate a report.
-------------------------------------------------

"""

import csv
import statistics

# ---------------- Task 1: Project Setup ----------------
def welcome():
    print("=" * 50)
    print("🎓 Welcome to the GradeBook Analyzer 🎓")
    print("=" * 50)
    print("Choose an option:")
    print("1. Enter student marks manually")
    print("2. Load student marks from CSV file")
    print("3. Exit")
    print("-" * 50)


# ---------------- Task 2: Data Entry or CSV Import ----------------
def manual_entry():
    marks = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i + 1}: ")
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score
    return marks


def load_from_csv():
    marks = {}
    file_path = input("Enter CSV file name (e.g., marks.csv): ")
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header if present
            for row in reader:
                if len(row) >= 2:
                    name = row[0].strip()
                    try:
                        score = float(row[1])
                        marks[name] = score
                    except ValueError:
                        print(f"Invalid score for {name}, skipping.")
        print(f"✅ Loaded {len(marks)} students from {file_path}.")
    except FileNotFoundError:
        print("❌ File not found. Please check and try again.")
    return marks


# ---------------- Task 3: Statistical Analysis ----------------
def calculate_average(marks_dict):
    return statistics.mean(marks_dict.values()) if marks_dict else 0


def calculate_median(marks_dict):
    return statistics.median(marks_dict.values()) if marks_dict else 0


def find_max_score(marks_dict):
    if marks_dict:
        name = max(marks_dict, key=marks_dict.get)
        return name, marks_dict[name]
    return None, 0


def find_min_score(marks_dict):
    if marks_dict:
        name = min(marks_dict, key=marks_dict.get)
        return name, marks_dict[name]
    return None, 0


# ---------------- Task 4: Grade Assignment ----------------
def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades


def grade_distribution(grades_dict):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades_dict.values():
        if g in dist:
            dist[g] += 1
    return dist


# ---------------- Task 5: Pass/Fail Filter ----------------
def pass_fail_lists(marks_dict):
    passed = [name for name, score in marks_dict.items() if score >= 40]
    failed = [name for name, score in marks_dict.items() if score < 40]
    return passed, failed


# ---------------- Task 6: Display Results ----------------
def display_results(marks_dict, grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("-" * 40)
    for name, score in marks_dict.items():
        print(f"{name:<15}{score:<10}{grades_dict[name]}")
    print("-" * 40)


def display_statistics(marks_dict):
    avg = calculate_average(marks_dict)
    med = calculate_median(marks_dict)
    max_name, max_score = find_max_score(marks_dict)
    min_name, min_score = find_min_score(marks_dict)

    print("\n📊 Statistics Summary:")
    print(f"Average Marks : {avg:.2f}")
    print(f"Median Marks  : {med:.2f}")
    print(f"Highest Marks : {max_score} ({max_name})")
    print(f"Lowest Marks  : {min_score} ({min_name})")


# ---------------- Main Program Loop ----------------
def main():
    while True:
        welcome()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            marks = manual_entry()
        elif choice == "2":
            marks = load_from_csv()
        elif choice == "3":
            print("👋 Exiting GradeBook Analyzer. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
            continue

        if not marks:
            print("No data available. Returning to menu.\n")
            continue

        grades = assign_grades(marks)
        display_results(marks, grades)
        display_statistics(marks)

        dist = grade_distribution(grades)
        print("\n🎯 Grade Distribution:")
        for g, count in dist.items():
            print(f"Grade {g}: {count} student(s)")

        passed, failed = pass_fail_lists(marks)
        print("\n✅ Passed Students:", ", ".join(passed))
        print("❌ Failed Students:", ", ".join(failed))

        again = input("\nDo you want to analyze again? (y/n): ").lower()
        if again != "y":
            print("👋 Thank you for using GradeBook Analyzer!")
            break


# Run the program
if __name__ == "__main__":
    main()