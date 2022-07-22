// Input Format: N = 5

// Result:
//     1
//    1 1
//   1 2 1
//  1 3 3 1
// 1 4 6 4 1

// Explanation: There are 5 rows in the output matrix. Each row corresponds to each one of the rows in the image shown above.

//Time Complexity => 0(N) , Space Complexity => O(1)
let generate = function (numRows) {
  let answer = [];
  for (let i = 0; i < numRows; i++) {
    let nexticj = 1;
    let arr = [];
    for (let j = 0; j <= i; j++) {
      arr.push(nexticj);
      let val1 = i - j;
      let val2 = j + 1;
      nexticj *= val1 / val2;
    }
    answer.push(arr);
  }

  return finalarr;
};
