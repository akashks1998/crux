int multiply(int mat1[][2], int mat2[][2]) { 
    int n1 =2, n2 = 2,m1 = 2, m2 = 2;
    int x, i, j; 
    int res[2][2]; 
    for (i = 0; i < m1; i++) 
    { 
        for (j = 0; j < n2; j++) 
        { 
            res[i][j] = 0; 
            for (x = 0; x < m2; x++) 
            { 
                res[i][j] += mat1[i][x] * mat2[x][j] ;
            } 
        } 
    } 
    for (i = 0; i < m1; i++) 
    { 
        for (j = 0; j < n2; j++) 
        { 
            print_int(res[i][j]); 
        } 
        print_char(10);
    } 
    return 0;
} 
  
// Driver code 
int main() 
{ 
    int mat1[2][2];
    int mat2[2][2]; 
    for(int i=0;i<2; i++){
        for (int j=0; j < 2 ;j++){
            scan_int(mat1[i][j]);
        }
    }
    for(int i=0;i<2; i++){
        for (int j=0; j < 2 ;j++){
            scan_int(mat2[i][j]);
        }
    }
   
    multiply(mat1, mat2); 
    return 0; 
    // give input 2 4 3 4 1 2 1 3
    // should show 6 16  7 18
}