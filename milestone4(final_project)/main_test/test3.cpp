struct hello {

       int a;

       float b;

};

 

struct hello_world {

       int a;

       float b;

};

 

int get_a(struct hello k) {

       return k.a;

}

 

int main() {

       int b;

       int a;

       struct hello k;  

 

       a = get_a(k);

 

       return 0;

}

