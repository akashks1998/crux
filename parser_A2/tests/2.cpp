class Geeks 
{ 
    public: 
    string geekname; 
    int id; 
      
    void printname(); 
      
    void printid() 
    { 
        cout << "Geek id is: " << id; 
    } 

	void printname() 
	{ 
   	 cout << "Geekname is: " << geekname;  
	} 
}; 
  
int main() { 
      
    class Geeks obj1; 
    obj1.geekname = "xyz"; 
    obj1.id=15; 
      
    obj1.printname(); 
    cout << endl; 
      
    obj1.printid(); 
    return 0; 
} 
