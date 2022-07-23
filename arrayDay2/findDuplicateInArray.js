// Example 1:

// Input: arr=[1,3,4,2,2]

// Output: 2

// Explanation: Since 2 is the duplicate number the answer will be 2.

let arr = [1, 3, 4, 2, 2];
//
function findDuplicateUsingMap(arr) {
  let map = {};
  for (let ele of arr) {
    if (map[ele] > 0) map[ele] += 1;
    else map[ele] = 1;
  }
  for (let key in map) {
    if (map[key] > 1) return key;
  }
}

console.log(findDuplicateUsingMap(arr));

let arr1 = [1, 3, 4, 2, 3];
function findDuplicateUsingLinkedListLoop(arr) {
  let slow = arr[0];
  let fast = arr[0];

  do {
    slow = arr[slow];
    fast = arr[arr[fast]];
  } while (slow !== fast);

  fast = arr[0];
  while (slow !== fast) {
    slow = arr[slow];
    fast = arr[fast];
  }
  return slow;
}

console.log(findDuplicateUsingLinkedListLoop(arr1));
