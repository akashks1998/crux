
// Function for calculating sin value 
float cal_sin(float n) 
{     
    float accuracy = 0.0001, denominator, sinx, sinval; 
      
    // Converting degrees to radian 
    n = n * (3.142 / 180.0);  
  
    float x1 = n; 
      
    // maps the sum along the series 
    sinx = n;          
      
    // holds the actual value of sin(n)   
    int i = 1; 
    do
    { 
        denominator = 2 * i * (2 * i + 1); 
        x1 = -x1 * n * n / denominator; 
        sinx = sinx + x1; 
        i = i + 1; 
    } while (i < 30); 
    
    return sinx;
} 
  
float cal_cos(float n) 
{ 
    float accuracy = 0.0001, x1, denominator, cosx, cosval; 
      
    // Converting degrees to radian 
    n = n * (3.142 / 180.0); 
      
    x1 = 1; 
      
    // maps the sum along the series 
    cosx = x1;          
      
    // holds the actual value of sin(n) 
    int i = 1; 
    do
    { 
        denominator = 2 * i * (2 * i - 1); 
        x1 = -x1 * n * n / denominator; 
        cosx = cosx + x1; 
        i = i + 1; 
    } while ( i < 30 ); 
    return cosx; 
} 