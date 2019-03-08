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
              catch
              {
                  cout<<"\nInteger exception caught.";
              }

              cout<<"\nEnd of program.";

       }
