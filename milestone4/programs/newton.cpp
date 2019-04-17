// An example function whose solution is determined using 
// Bisection Method. The function is x^3 - x^2  + 2 
// # include<stdio.h>
float func(float x) 
{   
    return (x*x*x - x*x )+ 2; 
} 
  
// Derivative of the above function which is 3*x^x - 2*x 
float derivFunc(float x) 
{ 
    return 3*x*x - 2*x; 
} 
  
float abs(float h){
    if(h > 0){
        return h;
    }else{
        return -h;
    }
}
// Function to find the root 
float newtonRaphson(float x) 
{ 
    float EPSILON = 0.001;
    float h = func(x) / derivFunc(x); 
    int i =0;
    print_float(abs(h));
    print_int(32);
    print_int(abs(h) >= EPSILON);
    while ( (abs(h) >= EPSILON) && i < 100) 
    { 
        float a = func(x);
        float b = derivFunc(x);
        h = a/b; 
   
        // x(i+1) = x(i) - f(x) / f'(x)   
        x = x - h; 

        // printf("%x", h);

        print_int(i);
        print_float(h);
        print_char(32);
        print_float(abs(h));
        print_char(32);
        print_int(abs(h) >= EPSILON);
        print_float(x);
        print_char(32);
        print_float(a);
        print_char(32);
        print_float(b);
        print_char(10);
        i = i + 1;
        
    }

    
    return x;

} 
  
// Driver program to test above 
int main() 
{ 
    float x0 = -20; // Initial values assumed 
    float a = newtonRaphson(x0);
    int b = (6.7 >= 0.001);
    // printf("%f", b);
    print_int(b);
    print_float(a);
    return 0; 
} 