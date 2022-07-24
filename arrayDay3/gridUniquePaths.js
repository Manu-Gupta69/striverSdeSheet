// Input Format: m = 2, n= 2
// Output: 2

let m = 3,
  n = 3;
function countPaths(row, col, n, m) {
  if (row == n - 1 && col == m - 1) return 1;
  if (row >= n || col >= m) return 0;
  else return countPaths(row + 1, col, n, m) + countPaths(row, col + 1, n, m);
}
function uniquePaths(m, n) {
  return countPaths(0, 0, m, n);
}

console.log(uniquePaths(m, n));
