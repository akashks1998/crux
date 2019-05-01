int main(){
    int c = 3;
    int *p = new (int);
    // int *p = new int; // will give error bracket is needed;
    // int *a = new (int)[6][4]; // will give error , not allowed in c++
    int rowCount = 6, colCount = 10;
    int** a = new (int*) [rowCount];
    for(int i = 0; i < rowCount; ++i){
        a[i] = new (int)[colCount];
    }
    float *q = new (float);

    delete [] p;
    return 0;
}