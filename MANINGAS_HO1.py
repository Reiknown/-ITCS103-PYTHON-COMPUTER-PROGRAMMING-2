# FUNCTION TO CALCULATE AVERAGE
def get_average(my_list):
    total = 0

    # add all numbers
    for x in my_list:
        total = total + x

    # calculate average
    answer = total / len(my_list)
    return answer


# FUNCTION TO COMPARE & DISPLAY RESULT
def compare_result(avg, length, word):
    if length > avg:
        print(f"The length of the word '{word}' is greater than the average.")
    elif length < avg:
        print(f"The length of the word '{word}' is less than the average.")
    else:
        print(f"The length of the word '{word}' is equal to the average.")



# EXECUTION
# 1. Ask the user to enter a word
word = input("Enter a word: ")

# 2. Determine the length of the word
word_length = len(word)

# create an empty list for numbers (for # 4)
nums = []
# 3. Ask the user to enter numbers (no. of inputs is = to the no. of charact in the word)
for i in range(word_length):
    val = eval(input(f"Enter number {i + 1}: "))
    
    # 4. Store all the entered numbers in a list
    nums.append(val)

# 6. Display the list
print(nums)

# Display word length
print(f"The length of the word is {word_length}")

# 5a. Computes and returns the average
my_avg = get_average(nums)
print(f"The average of the numbers is {my_avg}")

# 5b. Compares the average
compare_result(my_avg, word_length, word)