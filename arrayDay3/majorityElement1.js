// Input Format: N = 3, nums[] = {3,2,3}

// Result: 3

// Explanation: When we just count the occurrences of each
//number and compare with half of the size of the array, you will get 3 for the above solution.

let arr = [2, 2, 1, 1, 1, 2, 2];

function majorityElement(arr) {
  let count = 0;
  let element;

  for (let ele of arr) {
    if (count == 0) {
      element = ele;
    }
    if (element == ele) count += 1;
    else count -= 1;
  }
  return element;
}

console.log(majorityElement(arr));
