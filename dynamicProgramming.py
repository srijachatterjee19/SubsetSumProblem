# Subset sum problem solved using Dynamic Programming


def dynamicSubsetSum(set, target):
  # n is the number of items in the array nums
  arrayItems = len(set)
  # Fill the dynamicArray table with False values
  dynamicArray = [[False] * (target + 1) for _ in range(arrayItems + 1)]

  # Base case
  # The first value can be set to True considering the
  #  possibility of a null/empty subset
  for i in range(arrayItems + 1):
    dynamicArray[i][0] = True

  # Dynamic programming to fill the rest of the table
  # The base code for the table is from
  # https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

  for i in range(1, arrayItems + 1):
    for j in range(1, target + 1):
      # If the target is less than the current number, then don't add it to subset
      if j < set[i - 1]:
        dynamicArray[i][j] = dynamicArray[i - 1][j]
      else:
        #  if not, then either not add the current number  or the difference between the current sum(j) and current number in the set[i-1]
        dynamicArray[i][j] = dynamicArray[i -
                                          1][j] or dynamicArray[i -
                                                                1][j -
                                                                   set[i - 1]]

  # Next, backtrace to find subset that adds up to target
  subset = []
  row, column = arrayItems, target

  # If current cell is not the first cell, move up one row
  while row > 0 and column > 0:
    # if cell value is True, then move up one row
    if dynamicArray[row - 1][column]:
      row -= 1
    else:
      # if the cell value is False, add that number in subset and move
      # diagonally up and to the left
      subset.append(set[row - 1])
      column -= set[row - 1]
      row -= 1

  if sum(subset) == target:

    return subset
  else:
    return None


def testDynamicProgramming(numbers, target):
  result = dynamicSubsetSum(numbers, target)
  # print the input array numbers
  print("Input array is :", numbers)
  output = "Target is " + str(target) + " Subset found: " + str(
    result) + " with sum " + str(sum(result))
  print(output)
  print("")
  print("")


# Test cases
# Test 1
numbers = [
  30, 12, 20, 5, 10, 100, 200, 3, 22, 10, 14, 89, 10, 11, 35, 34, 67, 99
]
target = 30
testDynamicProgramming(numbers, target)
# Output: [30]

# Test 2
print("")
numbers = [
  30, 12, 20, 5, 10, 100, 200, 3, 22, 10, 14, 89, 10, 11, 35, 34, 67, 99
]
target = 2
result = dynamicSubsetSum(numbers, target)
print("Target is:", target, ",Subset found:", result)
print("Input array is :", numbers)
print("")

# Output: None

# Test 3
numbers = [30, 12, 20, 5, 10]
target = 40
testDynamicProgramming(numbers, target)

# Test 4
numbers = [3, 11, 1, 7, 9, 5]
target = 14
testDynamicProgramming(numbers, target)

# Test 5
numbers = [3, 11, 1, 7, 9, 5, 20, 11, 22, 33, 44, 55, 66]
target = 22
testDynamicProgramming(numbers, target)

# Test 6
number = 50
numbers = list(range(1, number + 1))
print("50 numbers set")
target = number * (number + 1) // 2  # Sum of all numbers from 1 to 50
print("target is ", target)
testDynamicProgramming(numbers, target)

# Test 7
number = 100
numbers = list(range(1, number + 1))
print("100 numbers set")
target = number * (number + 1) // 2  # Sum of all numbers from 1 to 100
print("target is ", target)
testDynamicProgramming(numbers, target)

# Test 8
number = 200
numbers = list(range(1, number + 1))
print("200 numbers set")
target = number * (number + 1) // 2  # Sum of all numbers from 1 to 200
print("target is ", target)
testDynamicProgramming(numbers, target)

# Test 9
number = 500
numbers = list(range(1, number + 1))
print("500 numbers set")
target = number * (number + 1) // 2  # Sum of all numbers from 1 to 500
print("target is ", target)
result = testDynamicProgramming(numbers, target)
