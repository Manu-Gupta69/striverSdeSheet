// Example 1:

// Input: [[1,2,3],[4,5,6],[7,8,9]]

// Output: [[7,4,1],[8,5,2],[9,6,3]]

// Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix.

let matrix = [[1,2,3],[4,5,6],[7,8,9]];

//1 2 3  Transpose   1 4 7
//4 5 6  =========>  2 5 8
//7 8 9              3 6 9
 
function rotateMatrix(matrix){
  
    function transposeOfMatrix(matrix){
      for(let i=0 ; i<matrix.length ;i++){
          for(let j=i ; j<matrix.length ;j++){
              let temp = matrix[i][j];
              matrix[i][j] = matrix[j][i];
              matrix[j][i] = temp;
          }
      }
    }

    function reverseOnMatrix (row ,start ,end , matrix){
        while(start < end){
            let temp = matrix[row][start];
            matrix[row][start] = matrix[row][end];
            matrix[row][end] = temp;
            start+=1;
            end -=1;
        }
    }

    transposeOfMatrix(matrix);
    for(let i=0 ; i<matrix.length ;i++){
        reverseOnMatrix(i ,0 , matrix[i].length-1 , matrix);
    }
}

rotateMatrix(matrix);
console.log(matrix);


