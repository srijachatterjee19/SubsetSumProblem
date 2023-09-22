#  Brute Force

The Brute Force approach is used to solve the subset sum problem i.e. iterating through all the possible subsets for a given set, computing the sum of this subset and checking if it is equal to the given target. The function bruteForce takes a multiset and the target as inputs. It then uses itertools1 python library to generate the possible combinations of subsets
A multiset with length n can have 2! subsets. For example, a multi-set with 3 numbers [1, 2, 3] will produce 8 subsets [],[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3] among which one is a null set. Then, the function returns True if the sum of any of the subsets matches the target value, if it does the function returns True, if it doesn’t False is returned. The values True/False mapped to the corresponding subsets using a dictionary and pandas2 library is used to return the result. The function maps each subset as index and the result for each subset(True or False) as keys. One of the values being True signiMies the result is True. The returnData function takes a dictionary as an input and returns a pandas Dataframe object, which is used to make the result easy to read. Since the function uses itertools and iterates through all possible combinations except for the null set i.e. 2^n − 1 and to check if the sum of each target is equal to the sum of subset elements. This is done for each element in the subset inside the second for loop in the code below for bruteForce function, the time complexity is (2n − 1)^2 which is simpliMied as O(2^n ) which is quite high.

# Nearest sum returned

The Brute force approach is used here again to solve the Subset sum problem. Instead of returning True/False as the result the sum of subsets that is closest to the target value is returned. The bruteForce function from the previous section was used to perform get the sum of all the subsets and return a dictionary object with the subsets as the keys and the sum of the subset values, this shows the table with t. Similarly, the result is returned as a data frame to show result in table format with the subset and it’s sum next to it.
The main closestSum function is used to calculate the smallest difference between the largest sum among all the subsets and the target sum. The function takes an array and target sum as input, using itertools to iterate through all subsets and a variable closestSum is updated with the largest sum among all of the sums of subsets. The closestSum is then subtracted from the target, thus giving the smallest difference between the largest sum and given target

# Dynamic Programming

The Brute force approach used in the previous sections to Mind a solution for the subset sum i.e. iterates through all the items, excluding the null set iterating through 2^n − 1 possibilities giving the Minal time complexity 0(2^n), which is really high. In general, determining if there are even any solutions to subset sum is NP-hard. The dynamicSubsetSum function does the following. It takes in inputs as a set of number and a target value. The 2D array dynamicArray is of size (arrayItems + 1) * (target + 1) and is Mirst initialised to all False values, where arrayItems is the number of values in the set. The 2D dynamic array rows(i) represent the index of the input array set[] and the columns(j) represent the sum. The dynamicArray[i][j] Mirst value can be Mirst set to true considering the possibility of a null set. Then, dynamic programming is used to Mill the rest of the table.If the current target sum (j) is less than the current number input set, set[i-1], if true it will not be added to subset since it would exceed the target sum which is not desired. The dynamicArray [i][j] value is then set to the value of a previous state in that case. But, if the current sum is greater than or equal to the current number in the input set, it is either include it in the subset or exclude it. In this case, the dynamicArray [i][j] is set to either not to the current sum OR the difference between the current sum(j) and current number in the set[i-1].The dynamicArray will then be Milled with True or False values depending on whether there is a subset in the input set which sums to the target sum or not. The dynamicArray is back traced until Mirst index is reached dynamicArray[0][0] to then Mind a subset that adds up to the target. If cell value is True, then move up by one row and if the cell value is False, append number in subset array and move diagonally up and to the left ‘column -= set[row - 1]’ and ‘row -= 1’. If the sum of the subset is then equal to the target sum, the subset is returned, or ‘None’ is returned as output.The Dynamic Programming approach gives the time-complexity 𝑂(𝐚𝐫𝐫𝐚𝐲𝐈𝐭𝐞𝐦𝐬 ×target) where target is the target sum and arrayItems is the number of elements (n).
