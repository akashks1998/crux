
int a;
a = 0;
class Geeks 
{  
    string geekname; 
    int id = 0, bg = 2; 
    
    void printname(){ 
   	 cout << "Geekname is: " << geekname;  
	} 
}; 
  
int main(int a[][], int b) { 
      
    class Geeks obj1; 
    obj1.geekname = "xyz"; 
    obj1.id=15; 
      
    obj1.printname(); 
    cout << endl; 
      
    obj1.printid(); 
    return 0; 
} 
