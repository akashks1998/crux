struct s {

 int a;

 float b;

};

 

struct t {

 int a;

 float b;

};

 

int g(int x, float y) {

 print_int(x);

 print_char(10);

 print_float(y);
 return 0;

}

 

int main() {

 struct s x;

 struct s y;

 float q;

 x.a = 2;

 y = x;

 x.b = -4;

 g(x.a, y.b);
 return 0;

}

