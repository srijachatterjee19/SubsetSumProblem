# Solve the Subset-sum problem using brute force and
# return the smallest difference to the target sum

from itertools import combinations
import pandas as pd


# If target sum is not found, then return
#  the closest possible match to target
def closestSum(numbers, targetSum):
  resultDictionary = {}
  # initialise closest sum
  closestSum = -1
  # perform bruteforce to get all the combinations of subsets and add them to a list
  for r in range(1, len(numbers) + 1):
    combinationsList = combinations(numbers, r)
    #for each element in the list, check for the subset which has the highest sum
    # this is done by updating the closestSum variable for each time the sum of a subset is greater than the previous subset sum and less than the target
    for combination in combinationsList:
      # return the subsets and the sum of each subset as a dictionary first
      resultDictionary[combination] = sum(combination)
      if sum(combination) > closestSum and sum(combination) <= targetSum:
        closestSum = sum(combination)
        # display the absolute value of the difference
        smallestDiff = abs(targetSum - closestSum)
  return smallestDiff, resultDictionary


# used to return the dictionary data into a dataframe table
def returnData(sumResult):
  dataFrame = pd.DataFrame.from_dict(sumResult,
                                     orient='index',
                                     columns=['Sum'])
  return dataFrame


# used to test the nearest sum function
def testClosestSum(S, t):

  closestSumResult, dictionary = closestSum(S, t)
  subsetsReturned = returnData(dictionary)

  # closestSumResult = closestSum(S, t)
  print(S)
  print("Target is")
  print(t)

  print(subsetsReturned)
  print("Smallest difference is: ", closestSumResult)
  print(" ")
  return closestSumResult


def main():
  # case 1
  print("Target greater than the largest element in the multiset")
  set = [3, 5, 4, 4, 8]
  t = 9
  testClosestSum(set, t)

  # case 2
  print("Target greater than the largest element in the multiset")
  set = [100, 50, 1, 20]
  t = 200
  testClosestSum(set, t)

  # case 3
  print("Target is at the end of the multiset")
  set = [35, 5, 20, 7]
  t = 7
  testClosestSum(set, t)

  # case 4
  print("Target is at the end of the multiset")
  set = [10, 20, 5]
  t = 5
  testClosestSum(set, t)

  # case 5
  print("Target is equal to the sum of all elements")
  set = [35, 5, 20, 7, 10]
  t = 77
  testClosestSum(set, t)

  # case 6
  print("Target is equal to the sum of all elements")
  set = [35, 10, 20]
  t = 65
  testClosestSum(set, t)

  # case 7
  print("Target is greater than the sum of all the elements")
  set = [35, 20, 7, 10]
  t = 100
  testClosestSum(set, t)

  # case 8
  print("Target is greater than the sum of all the elements")
  set = [35, 10, 2]
  t = 50
  testClosestSum(set, t)


if __name__ == "__main__":
  main()
