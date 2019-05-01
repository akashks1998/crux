int odd(int n);
int even(int n);
int main()
{
	// set an integer number here
	int number = 23940;
	// if the number is odd (1 = TRUE)
	if(odd(number)==1){
		print_int(1);
    }
	else{ 
		print_int(0);
    }
	return 0;
}
 
// returns 0 if the given number becomes 0, so the given number is odd
// returns even(number - 1) elsewhere
int odd(int number){
	if (number==0){ 
		return 0;
    }
	else{
		return even(number-1);
    }
}
 
// returns 0 if the given number becomes 0, so the given number is even
// returns odd(number - 1) elsewhere
int even(int number){
	if(number==0){ 
		return 1;
    }
	else{
		return odd(number-1);
    }
}