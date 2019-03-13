class A{
    int a;
    char hi(char a){
        int c = 1;
        return 0;
    }
    int hi(int a){
        int c = 1;
        return 0;
    }
};
int main()
{
    class A **a,b;
    // a.a = 1;
    (*a)->a = 1;
    int c;
    a->hi(c);

    return 1;
}
