// checking multi dim array
int main(){
    int s = 1;
    int *a[4][5][6], *b;
    b = &s;
    a[1][3][4] = b;
    return 0;
}