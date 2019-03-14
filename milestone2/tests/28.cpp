
// CPP program to illustrate  
// usage of global variables  
#include<"iostream"> 

struct employee
{
    char name[50];
    int salary;
};

typedef struct employee emp;


// global variable 
int global = 5; 
  
// global variable accessed from 
// within a function 
void display() 
{ 
    cout<<global<<endl; 
} 
  
// main function 
int main() 
{   
    typedef int** hey; 
    display(); 
      
    // changing value of global 
    // variable from main function 
    global = 10; 
    display(); 
} 