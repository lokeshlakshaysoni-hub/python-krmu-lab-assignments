print("Welcome to Daily Calorie Tracker!")
print("This program lets you note down your meals and total calories.\n")

meals = []
calories = []

n = int(input("How many meals you had today? "))

for i in range(n):
    name = input("Enter meal name " + str(i+1) + ": ")
    cal = float(input("Enter calories for " + name + ": "))
    meals.append(name)
    calories.append(cal)

total = sum(calories)
avg = total / len(calories)

limit = float(input("\nEnter your daily calorie limit: "))

if total > limit:
    msg = "You went over your daily limit!"
else:
    msg = "You are within your daily limit!"

print("\nMeal\tCalories")
print("----------------")
for i in range(len(meals)):
    print(meals[i], "\t", calories[i])

print("----------------")
print("Total\t", total)
print("Average\t", round(avg, 2))
print(msg)

save = input("\nDo you want to save this? (yes/no): ").lower()

if save == "yes":
    f = open("calorie_log.txt", "w")
    f.write("Daily Calorie Tracker\n")
    f.write("----------------\n")
    for i in range(len(meals)):
        f.write(meals[i] + ": " + str(calories[i]) + "\n")
    f.write("\nTotal: " + str(total) + "\n")
    f.write("Average: " + str(round(avg, 2)) + "\n")
    f.write("Status: " + msg + "\n")
    f.close()
    print("Saved in calorie_log.txt")