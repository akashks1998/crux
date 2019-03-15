### How to run
- To be added

### Features of our language
- Function overloading is allowed
- Class, Struct
- If Else
- For, while, do while
- Break, continue
- Other features of Vanilla C

## Some syntax changes
- Function of a class can only be declared like
```c++
class <Class_name> : <return type> <function name>( <function_parameters>){
	<function body>
}
class x: int f(int y){
	if(this->t > y){
    	return 0;
    }else{
    	return 1;
    }
}
```
Function declaration inside a class is not allowed, though function defination insde a class is allowed
- Paranthesis are must for start of new scope. Like
```c++
if(x>1)
	x++;
```
Is not allowed
```
if(x>1){
	x++;
}
```
Is allowed
