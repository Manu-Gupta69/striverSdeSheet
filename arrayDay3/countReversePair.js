// Example 1:

// Input: N = 5, array[] = {1,3,2,3,1)

// Output: 2

let arr = [1, 3, 2, 3, 1];

function countReversePair(arr) {
  let reversePair = 0;

  function merge(arr1, arr2) {
    let mergedArray = [];
    let j = 0;
    for (let i = 0; i < arr1.length; i++) {
      while (j < arr2.length && arr1[i] > 2 * arr2[j]) {
        j += 1;
      }
      reversePair += j;
    }

    function mergeArrays(arr1, arr2) {
      let i = 0,
        j = 0;
      while (i < arr1.length && j < arr2.length) {
        if (arr1[i] < arr2[j]) {
          mergedArray.push(arr1[i]);
          i += 1;
        } else {
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
    }
    mergeArrays(arr1, arr2);
    return mergedArray;
  }

  function mergeSort(arr) {
    if (arr.length == 1) return arr;

    let mid = Math.floor(arr.length / 2);

    let left = mergeSort(arr.slice(0, mid));
    let right = mergeSort(arr.slice(mid));

    return merge(left, right);
  }

  const sortedArray = mergeSort(arr);
  return { reversePair, sortedArray };
}

console.log(countReversePair(arr));
