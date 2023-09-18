# Solve the Subset-sum problem using Brute Force
# and return True if subset found, False if not

import pandas as pd
from itertools import combinations


def bruteForce(multiset, target):
  # If sum of any of the subsets is an exact match to the target
  # sum return True, if no match found return False

  resultDictionary = {}  #to return the result as a dictionary
  for r in range(1, len(multiset) + 1):
    # use itertools combinations function to different
    # combinations possible for a given set,take the range to
    # produce every possible number of subsets
    # for example {1,2,3} would produce [1],[2],[3],[1,2],[2,3],[1,2,3]
    # https://docs.python.org/3/library/itertools.html

    combinationsList = combinations(multiset, r)
    # Iterate over all the subsets, add the elements for each subset and
    #  check if the sum matches the target and  return true, else return false.
    # Return a dictionary with the combinations as keys and true/false
    # outcome as the corresponding values.
    for combination in combinationsList:
      if sum(combination) == target:
        resultDictionary[combination] = True

      else:
        resultDictionary[combination] = False
  return resultDictionary


# Return the results from dictionary as a dataframe to
# make the results look more presentable
def returnData(sumResult):
  dataFrame = pd.DataFrame.from_dict(sumResult,
                                     orient='index',
                                     columns=['Subset found'])
  return dataFrame


def testBruteForce(S, target):
  print(S)
  result = bruteForce(S, target)
  data = returnData(result)
  print(data)
  print(" ")
  print(" ")


def main():

  #Test boundary cases
  # case 1
  print("Target found in the beginning for input multiset:")
  S = [5, 4, 8, 6]
  target = 5
  testBruteForce(S, target)

  # case 2
  print("Target found in the beginning for input multiset:")
  S = [10, 34, 22, 56, 77, 12, 23, 56, 78, 90]
  target = 10
  testBruteForce(S, target)

  # case 3
  print("Target found at the end for input multiset:")
  S = [5, 4, 8, 6]
  target = 6
  testBruteForce(S, target)

  # case 4
  print("Target found at the end for input multiset:")
  S = [10, 34, 22, 56, 77]
  target = 77
  testBruteForce(S, target)

  # case 5
  print("Target is sum of all numbers for input multiset:")
  S = [5, 4, 8, 6]
  target = 23
  testBruteForce(S, target)

  # case 6
  print("Target is sum of all numbers for input multiset:")
  S = [45, 12, 11, 34]
  target = 102
  print(S)
  testBruteForce(S, target)

  # case 7
  print("Target is repeated for input multiset:")
  S = [5, 4, 4, 8, 6]
  target = 8
  testBruteForce(S, target)

  # case 8
  print("Target is repeated for input multiset:")
  S = [2, 3, 4, 3, 1]
  target = 6
  testBruteForce(S, target)


if __name__ == "__main__":
  main()
