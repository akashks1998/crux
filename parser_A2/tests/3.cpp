
class Object //Abstract class in C++
{
public :
  void show () = 0; //pure virtual function 
};
//
class ArithmeticAdd : public Object 
{
  int res;
public:
  void add (int a, int b) {
    res = a + b ;
  }
  void add (int a, int b, int c) // Function overloading - Static Binding 
  {
    res = a + b + c;
  }
  void show () {
     cout << "Result = " << res;
  }
};
//
class Complex : public Object 
{
  int real;
  int img;
public :
  Complex Add (Complex C1, Complex2) {
    real = C1.real + C2.real;
    img = C1.img + C2.img;
    return this;
  }
  void show () {
    cout << real << " + " << img << "i"  <<endl;
  }
};
//
int main () 
{
    Object o [2];
   ArithmeticAdd a;
   a.add (2,6);
   o [0] = &a;
   o [0].show ();  // Dynamic dispatch - run time polymorphisms 
   a.add (9,11,23);
   o [0].show ();
   Complex C1, C2, C3, C4;
   cin >> C1;
   cin >> C2;
   C4 = C3.Add (C1, C2); // Message passing 
   o [1] = & C4;
   o [1].show ();
   return 0;
}
