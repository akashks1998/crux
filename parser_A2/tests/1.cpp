<<<<<<< HEAD
int a(int c){
    int d;
    return 0;
}
int main(){
    int x=1;
    if(x=2){
        return 0;
    }else{
        return 1;
    }
}
=======
class student
{
    private:
	 char name[50];
   	 int a(){return 1;}
};

int main()
{
     int n, num, digit, rev = 0;

     cout << "Enter a positive number: ";
     cin >> num;

     n = num;

     do
     {
         digit = num % 10;
         rev = (rev * 10) + digit;
         num = num / 10;
     } while (num != 0);

     cout << " The reverse of the number is: " << rev << endl;

     if (n == rev)
         cout << " The number is a palindrome.";
     else
         cout << " The number is not a palindrome.";

    return 0;
}
>>>>>>> 3f606939ff7dc03fe4f8319d7ac9710bbf032262
