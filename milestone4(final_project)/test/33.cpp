// checking size of class , pointer of class in same class,
// checking pointer addition

class bi{
    int a, b;
};
class hi{
    int a;
    class hi * to_same;
    class bi b;
    // class hi same; // should give error
};

int main(){
    class hi list[5];
    class hi *ptr1, *ptr2;
    ptr2 = ptr1 + 1;
    // return ptr2; // diff return type, error
    return 0;

}