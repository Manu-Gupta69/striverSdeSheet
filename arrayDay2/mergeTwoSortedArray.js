// Example 1:

// Input:
// n = 4, arr1[] = [1 4 8 10]
// m = 5, arr2[] = [2 3 9]

// Output:
// arr1[] = [1 2 3 4]
// arr2[] = [8 9 10]

// Explanation:
// After merging the two non-decreasing arrays, we get, 1,2,3,4,8,9,10.

let arr1 = [1, 4, 8, 10];
let arr2 = [2, 3, 9];

function mergeArray(arr1, arr2) {
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] > arr2[0]) {
      swap(i, 0, arr1, arr2);
      for (let j = 1; j < arr2.length; j++) {
        if (arr2[j] < arr2[0]) {
          let temp = arr2[0];
          arr2[0] = arr2[j];
          arr2[j] = temp;
          break;
        }
      }
    }

  }

  function swap(idx1, idx2, arr1, arr2) {
    let temp = arr1[idx1];
    arr1[idx1] = arr2[idx2];
    arr2[idx2] = temp;
  }
}
mergeArray(arr1 , arr2);
console.log(arr1);
console.log(arr2);
