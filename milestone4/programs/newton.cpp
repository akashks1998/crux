// An example function whose solution is determined using 
// Bisection Method. The function is x^3 - x^2  + 2 
float func(float x) 
{   
    return x*x*x - x*x + 2; 
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
    while (abs(h) >= EPSILON and i < 10) 
    { 
        h = func(x)/derivFunc(x); 
   
        // x(i+1) = x(i) - f(x) / f'(x)   
        x = x - h; 
        // print_float(h);
        print_char(10);
        i = i + 1;
        print_int(i);
    }

    
    return x;

} 
  
// Driver program to test above 
int main() 
{ 
    float x0 = -20; // Initial values assumed 
    float a = newtonRaphson(x0); 
    print_float(a);
    return 0; 
} 