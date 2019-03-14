 void main()
       {
            int a=2;

              try
              {

                  if(a==1)
                      throw a;                  //throwing integer exception

                  else if(a==2)
                      throw 'A';                //throwing character exception

                  else if(a==3)
                      throw 4.5;                //throwing float exception

              }
              catch(int a)
              {
                  cout<<"\nInteger exception caught.";
              }
              catch(char ch)
              {
                  cout<<"\nCharacter exception caught.";
              }
              catch(double d)
              {
                  cout<<"\nDouble exception caught.";
              }

              cout<<"\nEnd of program.";

       }
