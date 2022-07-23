// Input Format:  array[] = {3,1,2,5,3}

// Result: {3,4)

// Explanation: A = 3 , B = 4 
// Since 3 is appearing twice and 4 is missing

let arr = [3,1,2,5,3]
function repeatAndMissingNumber(arr){
let map = {};
let reapeatingNumber, missingNumber;
for(let i=0 ; i<arr.length ;i++){
    if(map[arr[i]] > 0) map[arr[i]] +=1;
    else map[arr[i]] = 1;
}

for(let i=1 ; i<= arr.length ;i++){
    if(map[i] > 1) reapeatingNumber = i;
    if(!map.hasOwnProperty(i)) missingNumber = i;
}
return {reapeatingNumber, missingNumber};
}

console.log(repeatAndMissingNumber(arr));