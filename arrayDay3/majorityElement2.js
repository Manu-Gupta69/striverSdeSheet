// Input: N = 5, array[] = {1,2,2,3,2}

// Ouput: 2

// Explanation: Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.
//Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.
let arr = [1, 2, 2, 3, 2, 3, 3, 3, 3];
function majorityElement(arr) {
  let count1 = 0;
  let count2 = 0;
  let element1 = -1,
    element2 = -1;

  for (let ele of arr) {
    if (ele == element1) count1++;
    else if (ele == element2) count2++;
    else if (count1 == 0) {
      element1 = ele;
      count1 = 1;
    } else if (count2 == 0) {
      element2 = ele;
      count2 = 1;
    } else {
      count1--;
      count2--;
    }
  }
  count1 = 0;
  count2 = 0;
  for (let ele of arr) {
    if (ele == element1) count1 += 1;
    else if (ele == element2) count2 += 1;
  }

  if (count1 > arr.length / 3) return element1;
  if (count2 > arr.length / 3) return element2;
}

console.log(majorityElement(arr));
