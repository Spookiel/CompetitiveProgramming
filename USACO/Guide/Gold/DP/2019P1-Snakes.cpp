
#pragma GCC optimize("Ofast")

#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

int main(){

    ifstream fin("snakes.in");
    ofstream fout("snakes.out");


    int n,k;
    fin >> n >> k;
    int tot=0;
    int best[n+1][k+1];

    vi nums(n);
    for(int i=0; i < n; i++){
        fin >> nums[i];
        tot += nums[i];
    }
    
    int curmax = nums[0];

    best[0][0] = 0;
    for(int i=0; i <=n; i++){
        for(int j=0; j <= k; j++){
            if(j == 0 || i == 0){
                best[i][j] = 0;
                continue;
            }
            best[i][j] = 999999999;
        }
    }
    for(int i=1; i <= n; i++){
        
        curmax = max(curmax, nums[i-1]);
        best[i][0] = curmax*i;
    }
    for(int i=0; i <= n; i++){
        for(int j=0; j <= k; j++){
            cout << best[i][j] << " ";
        }
        cout << "\n";
    }
    //cout << "-------\n";
    for(int m=1; m <= n; m++){
        for(int c=1; c <= k; c++){
            int mor = 0;
            for(int i=m-1; i >= 0; i--){
                mor = max(mor, nums[i]);
                //for(int j=i+1; j <= m; j++) mor = max(mor, nums[j-1]);
                //cout << "-----" << m << " " << c << " " << i << "----------\n";
                best[m][c] = min(best[m][c], best[i][c-1]+(m-i)*mor);
                //cout << best[m][c] << " " << best[i][c-1] << " " << (m-i)*mor << " " << mor << "\n";
            }

            // for(int i=0; i <= n; i++){
            //     for(int j=0; j <= k; j++){
            //         cout << best[i][j] << " ";
            //     }
            //     cout << "\n";
            // }
            // cout << "-------\n";
            

        }

    }

    for(int i=0; i <= n; i++){
        for(int j=0; j <= k; j++){
            //cout << best[i][j] << " ";
        }
        //cout << "\n";
    }
    fout << best[n][k]-tot << "\n";
    return 1;
}