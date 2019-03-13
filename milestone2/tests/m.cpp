class A{
    int a;
    char x;
    char hi(char a){
        int c = 1;
        return 0;
    }
    int hi(char a, int c){
        c = 1;
        return 0;
    }
};
int main()
{
    class A *b;
    b->x=b->hi('a');
    return 1;
}
