class sum
{
	int a,b,c;
	void sum()
	{
		a=10;
		b=20;
		c=a+b;
		cout<<"Sum: "<<c;
	}
	void ~sum()
	{
		cout<<"call destructor"<<endl;
		delay(500);
	}
	void delay(int x){
		cout<<"lol";
	}
};

void main()
{
	class sum s;
	cout<<"call main"<<endl;
	getch();
}
