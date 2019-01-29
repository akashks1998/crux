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
    int n,m;
    cin>>n>>m;
    vi a(n);
    vec<pi > c(m);
    for(int i=0;i<n;i++)
        cin>>a[i];
    for(int i=0;i<m;i++){
        cin>>c[i].X>>c[i].Y;
        c[i].X--;c[i].Y--;
    }
    vi minm(a);

    vec<vi >con(n);
    for(int i=0;i<m;i++){
        for(int j=c[i].X;j<=c[i].Y;j++){
            minm[j]--;
            con[j].pb(i);
        }
    }
    vec<vi > arr(n,vi(n,0));
    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            for(int k=0;k<m;k++){
                if(c[k].X<=j&&c[k].Y>=i){
                    arr[i][j]++;
                    if(i!=j){arr[j][i]++;}
                }
            }
        }
    }
    int maxm=0,b=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(maxm< abs( a[i]-minm[j]-arr[i][j] ) ){
                maxm=abs( a[i]-minm[j]-arr[i][j] );
                b=j;
            }
        }
    }
    cout<<maxm<<endl;
    cout<<con[b].size()<<endl;
    for(int i=0;i<con[b].size();i++){
        cout<<con[b][i]+1<<' ';
    }
    return 0;
}