#using both while and for loops sum up all the numbers entered by user.
enter_number = int(input("number?: "))
final_number = 0
while enter_number > 0:
    for i in range(0, enter_number + 1):
        final_number = final_number + i
    print(final_number)
    break
if enter_number <= 0:
    print("no, i dont do negatives, OK?\nI know its the same math but Im too lazy\nIm not just checking for positives just to add a while loop ok?")

