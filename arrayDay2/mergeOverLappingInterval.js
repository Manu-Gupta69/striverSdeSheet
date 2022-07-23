// Example 1:

// Input: intervals=[[1,3],[2,6],[8,10],[15,18]]

// Output: [[1,6],[8,10],[15,18]]

// Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
//  intervals.

let intervals = [
  [1, 3],
  [2, 6],
  [8, 10],
  [15, 18],
];

function mergeOverLappingInterval(intervals) {
  intervals.sort((a, b) => {
    return a[0] - b[0];
  });

  let mergedIntervals = [intervals[0]];
  for (let i = 1; i < intervals.length; i++) {
    if (mergedIntervals[mergedIntervalPointer][1] >= intervals[i][0]) {
      mergedIntervals[mergedIntervalPointer][1] = Math.max(
        intervals[i][1],
        mergedIntervals[mergedIntervalPointer][1]
      );
      mergedIntervals[mergedIntervalPointer][0] = Math.min(
        intervals[i][0],
        mergedIntervals[mergedIntervalPointer][0]
      );
    } else {
      mergedIntervals.push(intervals[i]);
      mergedIntervalPointer += 1;
    }
  }
  return mergedIntervals;
}

console.log(mergeOverLappingInterval(intervals));
