
#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
#define INF 1e12

bool isPrime(int x){
    
    for(int div=2; div*div <= x; div++){
        if(x%div == 0){
            return false;
        }
    }
    return true;
}

int main(){

    int n;
    cin >> n;

    for(int i=2; i <= n; i++){
        //cout << i << " " << isPrime(i) << "\n";
        if(isPrime(i) && n%i != 0){
            cout << i << "\n";
            break;
        }
    }


    return 0;
}