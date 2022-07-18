def generate(self, numRows: int) -> List[List[int]]:
    result = []

    for i in range(numRows):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(result[i-1][j-1] + result[i][j-1])
        result.append(temp)
    return result



# Time Complexity = O(numRow^2)  because We are creating a 2D array of size (numRows * numCols) (where 1 <= numCols <= numRows), and we are traversing through each of the cells to update it with its correct value.
# Space Coplexity = O(numRow^2)  because We are creating a 2D array of size