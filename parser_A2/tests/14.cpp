struct student
{
  char name[20];
  int roll;
};

void display(struct student stu);

void main()
{
  struct student stud;
  cout<<"Enter student's name: ";
  cin>>stud.name;
  cout<<"Enter roll number:";
  cin>>stud.roll;
  display(stud);   // passing structure variable stud as argument
  getch();
}
void display(struct student stu)
{
  cout<<"Name: "<<stu.name<<endl;
  cout<<"Roll: "<<stu.roll;
}
