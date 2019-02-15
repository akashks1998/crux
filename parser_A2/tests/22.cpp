#include<"bits/stdc++.h">
#include<"blah.h">
int foo() {
  struct Local {
    static int my_number() {
      return 42;
    }
  };

  int i = 0;
  i = Local.my_number();
  return i + 1;
}
