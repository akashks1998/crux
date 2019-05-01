// Chcking break, continue, switch, loops and branches
int main(){
    int x=3,y;
    while(x < 10){
        switch(x){
            case 3: y=7; break; for(int i=0;i<18;i++){ break; }
            default: y =5; break;
            case 'c' : y = 'd';
        }
        break;
        do{
            if(x==3){
                int b =1;
                break;
            }
            if(x==5){
                continue;
            }else{
                x = 7;  
            }
            
        }while(x>3);
    }
    return 0;
}
