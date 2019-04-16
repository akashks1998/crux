struct S

{

int a;

char b;

};

int main()

{

char f1,f2,f3;

char fa[3];

int ia[6];

int i1,i2;

struct S x;

f1 = f2 = 3;

x.a = 5;

x.b = 7;

fa[0] = 2;

ia[5] = 9;

i2 = 1;

i1 = f1 + f2;    // i1 = (int) f1 +char f2

f3 = f1 / i2;    // f3 =  f1 /char ((char) i2)

f1 = i1 * x.a;   // f1 = (char) i1 +INT x.a

i1 = fa[0] + ia[5]; // i1 = (int) fa[0] +char ((char) ia[0])

print_int(i1);

print_int(f3);

print_int(f1);
return 0;

}