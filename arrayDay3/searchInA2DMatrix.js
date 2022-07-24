// Input: matrix =
// [[01,03,05,07],
//  [10,11,16,20],
//  [23,30,34,60]],

// target = 3

// Output: true

// Explanation: As the given integer(target) exists in the given 2D matrix, the function has returned true.

let matrix = [
  [01, 03, 05, 07],
  [10, 11, 16, 20],
  [23, 30, 34, 60],
];
let value = 30;
function search(matrix, value) {
  let row = matrix.length;
  let col = matrix[0].length;

  function binarySearchInMatrix(matrix, value) {
    let low = 0;
    let high = row * col - 1;
    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      let midRow = Math.floor(mid / col);
      let midCol = Math.floor(mid % col);
      if (matrix[midRow][midCol] < value) {
        low = mid + 1;
      } else if (matrix[midRow][midCol] > value) {
        high = mid - 1;
      } else {
        return { midRow, midCol };
      }
    }
    return { row: null, col: null };
  }
  return binarySearchInMatrix(matrix, value);
}

console.log(search(matrix, value));
