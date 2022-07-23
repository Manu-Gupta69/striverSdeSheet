// Example 1:

// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and 
// sell on day 5 (price = 6), profit = 6-1 = 5.

// Note: That buying on day 2 and selling on day 1 
// is not allowed because you must buy before 
// you sell.
let arr = [7,1,5,3,6,4];
function buyAndSellStock1(arr){
   let runninMin = arr[0];
   let profit = 0;
   for(let i=1 ; i<arr.length ;i++){
     profit = Math.max(profit , arr[i]-runninMin);
     runninMin = Math.min(runninMin , arr[i]);
   }
   return profit;
}

console.log(buyAndSellStock1(arr));