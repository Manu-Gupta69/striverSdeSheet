// Input Format: N = 5, array[] = {5,4,3,2,1}

// Result: 10

// Explanation: we have a reverse sorted array and we will
// get the maximum inversions as for i < j we will always
// find a pair such that A[j] < A[i].
// Example: 5 has index 0 and 3 has index 2 now (5,3) pair
// is inversion as 0 < 2 and 5 > 3 which will satisfy out
// conditions and for reverse sorted array we will get
// maximum inversions and that is (n)*(n-1) / 2.

// For above given array there is 4 + 3 + 2 + 1 = 10 inversions.

let arr = [5, 4, 3, 2, 1];
function countInversion(arr) {
  let inversion = 0;

  function merge(arr1, arr2) {
    let i = 0,
      j = 0;
    let mergedArray = [];
    while (i < arr1.length && j < arr2.length) {
      if (arr1[i] < arr2[j]) {
        mergedArray.push(arr1[i]);
        i += 1;
      } else {
        inversion += arr1.length - i;
        mergedArray.push(arr2[j]);
        j += 1;
      }
    }
    while (i < arr1.length) {
      mergedArray.push(arr1[i]);
      i += 1;
    }
    while (j < arr2.length) {
      mergedArray.push(arr2[j]);
      j += 1;
    }
    return mergedArray;
  }

  function mergeSort(arr) {
    if (arr.length == 1) return arr;

    let mid = Math.floor(arr.length / 2);

    let left = mergeSort(arr.slice(0, mid));
    let right = mergeSort(arr.slice(mid));
    console.log(left, right);
    return merge(left, right);
  }

  const sortedArray = mergeSort(arr);
  return {inversion , sortedArray}
}

console.log(countInversion(arr));

