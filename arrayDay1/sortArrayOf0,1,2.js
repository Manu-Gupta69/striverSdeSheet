// Input: nums = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]

let arr = [2,0,2,1,1,0];

function dutchFlag(arr){
  let start =0 , end = arr.length-1;
  let i=0;
  while(i<= end){
      if(arr[i] == 0){
        swap(start,i , arr);
        start +=1;
        i+=1;
      }else if(arr[i] == 2){
          swap(end , i, arr);
          end -=1;
      }else{
          i+=1;
      }
  }
  return arr;
}

function swap(idx1, idx2, arr) {
    let temp = arr[idx1];
    arr[idx1] = arr[idx2];
    arr[idx2] = temp;
  }
console.log(dutchFlag(arr));

