
# Crux Compiler
Compiler for crux language ( a subset of C/C++ ) written in python with X86 32bit, AT&T format assembly as the target language. This is being done as part of the course project in CS335(Compiler Design).

## Structure
This project is done in a series of milestones.
Structure of each milestone-
 - Doc: Contains problem statement and help regarding running the code.
 - Src: Contains the source code
 - Test: Contains test cases.

The final and complete project is in milestone 4.

## Intermidiate files:
- code.crux: Contains 3AC representation of code
- sym.dump: Contains symbol table
- m.s: Contains assembly code in X86 32bit, AT&T format
- m.out: BInary file for the compiled code


## SymbolTable : 
- This is a list of symbol Tables; One for global and one each for functions and classes
- each local and temp variables contain a base address, offset and size
- All entries for activation record are in function entry of symbol table

## Features :
### Basic features:
- Native data types: Int, Char, Float
- Variables and Expressions
- Conditional: if, if-else, switch-case
- Loops: for, while, do-while
- Break, continue
- Arrays: Single and multidimensional
- Input,output
- Functions, recursion
- User-defined types (struct, class)
- Pointers: Single and multilevel
- Simple library functions
- Arithmetic operators
- Logical and bitwise operators

### Additional features
-   Function overloading
-   Class and its functions
-   Auto-type inference
-   Dynamic memory allocation: new, delete
-   Basic nested function(Can’t access variables of parent functions)
-   Class as a function parameter, Class Assignment.
-   An array as a function parameter
-   Global variables

Following are the differences from vanilla implementation of the above[^1]
## Array
- Variable sized arrays cannot be declared :
  ```
  int a[5]; //allowed
  int a[c]; //not allowed
  ```
  Dynamic array can be allocated via new
  Array initialisation at the time of declaration is not allowed
  ```
  int a[5]={1,2,3,4,5}; //not allowed
  ```
## Branches
 - Same as vanilla C++ except following changes
 - We have no else if clause so you have to write if-else as :
   ```
   if(i==0){
      y=1;
   }else{
      if(i==1){
        y=2;
      }
   }
   ```
 - You have to use curly braces for all loops,branches,etc... single lines not allowed
   ```
   if(i==0) y=1;    //not allowed
   if(i==0){ y=1; } //allowed
   ```
   
## Loops
- All 3 for, while and do-while loops are allowed and same as vanilla C++ except for the compulsory use of braces
  ```
  for(;;)int i=0; //not allowed
  for(;;){;}      //allowed
  ```
- break gets attached to nearest switch-case/\{for,while,do-while\}loop, while continue gets attached to nearest \{for,while,do-while\}loop. See tests/34.cpp.

## Classes
- Class variables are accessed only by ``this``.
- A class function can be prototyped inside class declaration itself
- The class function should be defined outside of class as in the given example, it does not need to prototyped for definition.
- No Constructor and Destructor, we have to call them explicitly.
- Class functions can be prototyped inside a class and can be added later using "::" operator.
  ```
  class x{
    int a;
    int f(int b);
  };
  class x:: int f(int y){
    	if(this->a > y){
       	return 0;
      }else{
      	return 1;
      }
  }
  ```

## Functions
- Function overloading allowed.
  - 2 Functions are the same only if their name is the same, and order of type of arguments are exactly the same.
  - Class Functions can also be overloaded.
  - return type overloading is not allowed. E.g.
    ```
    void func(int b, int c){;}  //1,2,3,4 are all different
    void func(int b, float c){;}
    void func(int b){;}
    void func1(int b, int c){;}
    int func(int a, int h){return 1;} //same as 1
    ```
- Function code is generated as follows:
  - offset of all local variables except parameters are calculated during function definition.
  - offset of parameters is calculated during function call.
  - Stack space is increased using offset calculated earlier using BeginFunc and EndFunc reverts to original space

## Include
- Presently you can only include std.cpp, it contains a function for new and deletes. And include a statement(if used) should be at the top of the file.

## Allocation/Deallocation
- the new keyword is used for allocation and is used as ```new (int)[c]``` round brackets are compulsory and square braces are optional and if mentioned returns array of allocated objects. Here variable sized arrays are possible.
- to delete a variable previously allocated, use ``delete id`` and for array use ``delete [] id``. Currently, the id should be an identifier only.

## I/O
You can scan int, char using scan_int, scan_char respectively and print them using print_int, print_char respectively. For printing float we are printing hex of float(using print_float), you can check its value using [this site](https://gregstoll.com/~gregstoll/floattohex/).

### Team
 - [Ashish Kumar](https://github.com/aasis21)
 - [Akash Kumar Singh](https://github.com/akashks1998)
 - [Jenil Mewada](https://github.com/Jenil2910)

### References
 - [PLY for Lexing and Parsing](http://www.dabeaz.com/ply/)
 - [Stanford 3AC Examples](https://web.stanford.edu/class/archive/cs/cs143/cs143.1128/handouts/240%20TAC%20Examples.pdf )
 - [Grammar](https://www.nongnu.org/hcb/)
