struct s {

   int a;

   int b[5][5];

};

 

struct t{

   struct s x[10];

};

 

int f(int * a[10], int b[5][5]) {

   b[1][2] = 10;
   return 0;

}

 

int main() {

   int a[10][10];

   int b[10][10];

   int * c[5];

   struct t y;

   int i;

   int * fp;

   y.x[3].b[1][2] = 4;

   f(c,y.x[3].b);

   print_int(y.x[3].b[1][2]);
    return 0;
}

