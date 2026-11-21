#First Varibles
total_chores=4
oringal_cout=total_chores

print(f"you have {total_chores} left to do by the end of the day")

#second variables keeping counter for comleted chores
completed_chores=0
chore_number=1

#part 3 repeat if still chores

while chore_number <= total_chores:
    if chore_number==1 : next_chore = "make your bed"
    elif chore_number==2 : next_chore = "Feed the Pet"
    elif chore_number==3 : next_chore = "mop the floors"
    else:next_chore = "Clean the dishes"

    answer = input(f"have you finished: {next_chore}?  yes or no? ").lower()

    if answer == "yes":
        completed_chores += 1 
        chore_number += 1
        print("Greate job, Chore completed")
    else:
        print("Okay finish it and check again ")

    print("chores remaining;",total_chores-completed_chores)
    print("\n")
print("-------All chores completed---------")
print("Great work, u finishede all ur chores!")