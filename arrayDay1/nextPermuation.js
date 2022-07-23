function nextPermutation(array) {
  function swap(idx1, idx2, arr) {
    let temp = arr[idx1];
    arr[idx1] = arr[idx2];
    arr[idx2] = temp;
  }
  function reverse(start, end, arr) {
    while (start < end) {
      swap(start, end, arr);
      start++;
      end--;
    }
  }

  if (array.length == 1) return array;
  let breakidx,
    breakpoint = false;
  for (let i = array.length - 1; i >= 0; i--) {
    if (array[i - 1] < array[i]) {
      breakidx = i;
      breakpoint = true;
      break;
    }
  }

  if (!breakpoint) return array.reverse();

  for (let i = array.length - 1; i >= breakidx; i--) {
    if (array[i] > array[breakidx - 1]) {
      swap(i, breakidx - 1, array);
      break;
    }
  }
  reverse(breakidx, array.length - 1, array);
  return array;
}
console.log(nextPermutation([1,3,2]))