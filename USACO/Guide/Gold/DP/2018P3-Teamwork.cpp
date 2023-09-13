


#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

int main(){

    ifstream fin("teamwork.in");
    ofstream fout("teamwork.out");

    int n,k;
    fin >> n >> k;

    int best[n+1];
    fill(best, best+n+1,0);
    vi nums(n);
    for(int i=0; i < n; i++) fin >> nums[i];


    for(int i=1; i <= n; i++){
        int cbest = nums[i-1];
        int maxgroup = k > i ? i : k;

        for(int j=1; j <= maxgroup; j++){
            best[i] = max(best[i], best[i-j]+cbest*j);
            cbest = max(cbest, nums[i-j-1]);
        }

    }
    long long ans = 0;
    for(int i=0; i <= n; i++) ans = max(ans, (long long) best[i]);

    fout << ans << "\n";





    return 1;
}