def while_else():
    #Python While Else with a Break Statement
    numbers = [1, 3, 5, 7, 9]
    target = 2
    i = 0

    # While to search target in numbers
    while i < len(numbers):
        # Check the number
        if numbers[i] == target:
            print("Found the number!")
            break
        i = i + 1

    # Else condition run when while loop run completely
    else:
        print("Number not found.")

############################################################################################
    #Nested While-Else loop in Python
    nums = [3, 5, 7, 4, 11, 13]
    i = 0

    while i < len(nums):
        if nums[i] > 1:
            divisor = 2
            while divisor < nums[i]:
                if nums[i] % divisor == 0:
                    print(f"The first composite number in the list is: {nums[i]}")
                    break
                divisor += 1
            else:
                # The else part of the while loop; executed if the number is prime
                i = i + 1
                continue
            # Breaks the for loop if a composite number is found
            break
    else:
        # The else part of the for loop; executed if no composite numbers are found
        print("No composite numbers found in the list.")
############################################################################################
    #Python While Else with Continue Statement
    # Example of while else with continue statement

    counter = 1
    num = 2

    while (counter <= 10):

        if (counter % 2 == 0):
            counter += 1
            # Skip the rest of the loop body and go to the next iteration
            continue

        print(f"{num} * {counter} = {num * counter}")

        counter += 1

    else:
        print("Inside the else block")

    print("Outside the loop.")
    ############################################################################################
    #Python While Else with a pass Statement
    counter = 0
    target = 5

    # While loop to search for the target value
    while counter < 10:
        if counter == target:
            print(f"Target value {target} found!")
            break
        counter += 1
    else:
        pass

    # Rest of the code outside the loop
    print("Loop completed.")


while_else()