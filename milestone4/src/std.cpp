int abs(int a){
    if(a>0){
        return a;
    }else{
        return -a;
    }
}
int pow(int base, int exp){
    int b=1;
    for(int i=0;i<exp;i++){
        b=base*b;
    }
    return b;
}
int isgreater(int a, int b){
    if(a>b){
        return 1;
    }else{
        return 0;
    }
}
int islesser(int a, int b){
    if(a<b){
        return 1;
    }else{
        return 0;
    }
}
int isgeq(int a, int b){
    if(a>=b){
        return 1;
    }else{
        return 0;
    }
}
int isleq(int a, int b){
    if(a<=b){
        return 1;
    }else{
        return 0;
    }
}
int mult_array(int a[], int n, int c){
    for(int i=0;i<n;i++){
        a[i]=a[i]*c;
    }
   return 0; 
}

int* slice_array(int a[], int i, int j){
    int* b = new(int)[j-i];
    for(int k=i;k<j;k++){
        b[k] = a[k];
    }
    return b;
}

int* mask_array(int a[], int mask[], int n){
    cnt=0;
    for(int i=0;i<n;i++){
        if(mask[i]!=0){
            cnt++;
        }
    }
    int* b = new(int)[cnt];
    cnt=0;
    for(int i=0;i<n;i++){
        if(mask[i]!=0){
            b[cnt] = a[i];
            cnt++;
        }
    }
    return b;
}

int* slice_array(int* a[], int i, int j){
    int* b = new(int)[j-i];
    for(int k=i;k<j;k++){
        b[k] = a[k];
    }
    return b;
}

int* mask_array(int* a[], int mask[], int n){
    cnt=0;
    for(int i=0;i<n;i++){
        if(mask[i]!=0){
            cnt++;
        }
    }
    int* b = new(int)[cnt];
    cnt=0;
    for(int i=0;i<n;i++){
        if(mask[i]!=0){
            b[cnt] = a[i];
            cnt++;
        }
    }
    return b;
}

class pairii{
    int a;
    int b;
}

class pairii : int add(class pairii p, class pairii *c){
    c->a = this->a + p.a;
    c->b = this->b + p.b;
}

class pairii : int sub(class pairii p, class pairii *c){
    c->a = this->a - p.a;
    c->b = this->b - p.b;
}

class pairii : int dot(class pairii p, class pairii *c){
    int x = this->a;
    int y = this->b;
    c->a = x*p.a;
    c->b = y*p.b;
}

int main(){
    int a = -6;
    print_int(abs(a));
    return 0;
}
