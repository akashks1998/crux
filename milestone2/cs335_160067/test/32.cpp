// Chcking class features

class e
{   
    int a;
    int hi(int s);
   
};
class  e :: int hi(int s){
    class e obj= *this;
    obj.a = 1;
    this-> a = 5;
    // a = 1; // can not access class member without this, uncommneting should give error
    int a;
    a = 1;
    return 1;
}

int main( ){
    return 0;
}