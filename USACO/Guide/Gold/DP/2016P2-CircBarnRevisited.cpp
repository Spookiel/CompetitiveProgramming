

#pragma GCC optimize("Ofast")
#pragma GCC target("avx")
#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
#define INF 1e12


int main(){

    ifstream fin("cbarn.in");
    ofstream fout("cbarn.out");


    int N,K;

    fin >> N >> K;

    vi nums(N);
    for(int i=0; i < N; i++) fin >> nums[i];



    long long best[K+1][N+1];
    long long ans = INF;

    for(int pos=0; pos < N; pos++){

        for(int i=0; i <= K; i++) fill(best[i], best[i]+N+1, INF);

        best[0][N] = 0;
        for(int k=1; k <= K; k++){
            for(int i=0; i <= N; i++){
                long long pen = 0;

                for(int dafter=i+1; dafter <= N; dafter++){
                    pen += nums[dafter-1]*(dafter-i-1);
                    best[k][i] = min(best[k][i], pen+best[k-1][dafter]);
                }


            }
        }

        //cout << best[K][0] << "\n";
        ans = min(ans, best[K][0]);

        int f = nums[0];
        nums.erase(nums.begin());
        nums.push_back(f);

    }

    fout << ans << "\n";







    return 0;
}