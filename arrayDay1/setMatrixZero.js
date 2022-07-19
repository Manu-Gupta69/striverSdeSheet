//Question

// Examples 1:

// Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

// Output: [[1,0,1],[0,0,0],[1,0,1]]

// Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
// Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

// Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

// Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0

//TIME COMPLEXITY => 0(N*M + M*N) SPACE COMPLEXTIY => 0(N)
let row = new Array(matrix.length).fill(-1);
let col = new Array(matrix[0].length).fill(-1);

for(let i=0 ;i<matrix.length;i++){
    for(let j=0 ;j<matrix[i].length;j++){
        if(matrix[i][j] == 0){
            row[i] = 0;
            col[j] = 0;
        }
    }
}

for(let i=0 ;i<matrix.length ;i++){
    for(let j=0 ;j<matrix[i].length; j++){
        if(row[i] == 0 || col[j] == 0) matrix[i][j] == 0;
    }
}

console.log(matrix);