int count;
int ackermann(int x, int y){
    // print_int(x);
    // print_int(y);
	count++;
	if(x<0 || y<0){
        return -1;
    }
	if(x==0){
        return y+1;
    }
	if(y==0){
		return ackermann(x-1,1);
    }
	return ackermann(x-1, ackermann(x,y-1) );
}

int main(){
    count = 0;
    int accr = ackermann(3,4);
    print_int(accr);
    return 0;
}