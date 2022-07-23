// Example 1:

// Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

// Output: 6 
let arr = [-2,1,-3,4,-1,2,1,-5,4];
function kadane(arr){
    let runningMax = arr[0];
    let currentMax = arr[0];
    for(let i=1 ; i<arr.length ;i++){
        currentMax = currentMax + arr[i];
       currentMax = Math.max(currentMax , arr[i]);
       runningMax = Math.max(runningMax , currentMax);
    }
    return runningMax;
}

console.log(kadane(arr))