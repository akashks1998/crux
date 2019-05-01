#include<bits/stdc++.h>
using namespace std;

// #pragma GCC optimize ("O3")
# define PI           3.14159265358979323846  /* pi */


#define pb push_back
#define vec vector
#define vi vector<int>
#define pi pair<int,int>
#define ll long long
#define pl pair<long long ,long long>
#define X first

#define Y second
ll gcd(ll a,ll b){ return b==0?a:gcd( b, a%b ); }
ll power(ll a,ll b,ll m){ return b?(b&1? (a*power( (a*a)%m,b>>1,m))%m:power( (a*a)%m,b>>1,m)):1; }

int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        int l1,l2,r1,r2;
        cin>>l1>>r1>>l2>>r2;
        if(l1!=r2){
            cout<<l1<<' '<<r2<<endl;
        }else{
            cout<<r1<<' '<<l2<<endl;
        }
    }
    return 0;
}