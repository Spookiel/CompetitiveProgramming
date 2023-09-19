
#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
#define INF 1e12

vi dp[100005];
vi graph[100005];

int dfs(int u, int par){
    //cout << u << " " << par << "\n";

    vi plens = {0};
    for(auto child: graph[u]){
        if(child == par){
            continue;
        }
        plens.push_back(1+dfs(child, u));

    }
    sort(plens.begin(), plens.end(), greater<int>());
    dp[u] = plens;
    return plens[0];

}


int main(){

    int n,k;
    cin >> n >> k;
    vi skills(k);
    for(int i=0; i < k; i++) cin >> skills[i];

    for(int i=0; i < n; i++) graph[i] = {};
    
    int x;
    for(int i=1; i < n; i++){
        cin >> x;
        graph[x].push_back(i);
    }
    sort(skills.begin(), skills.end(), greater<int>());

    dfs(0, -1);
    vi ans = {dp[0][0]};
    for(int i=0; i < n; i++){
        for(auto j=1; j < dp[i].size(); j++){
            ans.push_back(dp[i][j]);
        }
    }
    sort(ans.begin(), ans.end(), greater<int>());

    long long tot = 0;
    
    for(int i=0; i < k; i++){
        tot += (long long) ans[i]*skills[i];
    }
    cout << tot << "\n";


    return 0;
}