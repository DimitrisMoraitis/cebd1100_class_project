# program for while and if statements
# assign variables
counter = 0
score_total = 0
test_score = 0

# get scores
while test_score != 999:
    test_score = int(input('Enter test score > '))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score     # add test score to total
        counter += 1                  # add 1 to counter

# calculate average score
average_score = round(
    score_total / counter)

# display result
print("===============================")
print("Total Score: " + str(score_total)
      + "\nAverage Score: " + str(average_score))
