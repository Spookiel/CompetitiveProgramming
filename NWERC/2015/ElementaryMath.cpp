#include <bits/stdc++.h>
using namespace std;
const double EPS = 1e-9;
#define INF 1e9

#define MAXM 12000
#define MAXN 12000

int m, n;
bool graph[MAXM][MAXN];

bool seen[MAXN];
int matchL[MAXM], matchR[MAXN];

bool bpmDfs(int u) {
  for(int v = 0; v < n; v++) {
    if(graph[u][v]) {
      if(seen[v]) continue;
      seen[v] = true;

      if(matchR[v] < 0 || bpmDfs(matchR[v])) {
        matchL[u] = v; matchR[v] = u;
        return true;
      }
    }
  }
  return false;
}

int bpm() {
  memset(matchL, -1, sizeof(matchL));
  memset(matchR, -1, sizeof(matchR));
  int cnt = 0;
  for(int i = 0; i < m; i++) {
    memset(seen, false, sizeof(seen));
    if(bpmDfs(i)) cnt++;
  }
  return cnt;
}


int main(){
    int n1;
    cin >> n1;
    
    long long a,b;
    long long res;
    vector<long long> results;
    vector<pair<long long, long long>> nums(n1);
    for(int i=0; i < n1; i++){
        cin >> a >> b;
        nums[i].first = a;
        nums[i].second = b;
        res = a+b;
        if(find(results.begin(), results.end(), res) == results.end()){
            results.push_back(res);
        }
        res = a-b;
        if(find(results.begin(), results.end(), res) == results.end()){
            results.push_back(res);
        }
        res = a*b;
        if(find(results.begin(), results.end(), res) == results.end()){
           results.push_back(res);
        }
    }
    // Virtual src at 0, virt sink at 1
    //Join with weight one to sink
    sort(results.begin(), results.end());
    n = n1;
    m = results.size();
    cout << "SIZES: " << n << " " << m << "\n";
    for(int i=0; i < n1; i++){
        auto &[a,b] = nums[i];
        res = a+b;
        int ind = find(results.begin(), results.end(), res)-results.begin();

        graph[i][ind] = 1;
        
        res = a-b;
        ind = find(results.begin(), results.end(), res)-results.begin();

        graph[i][ind] = 1;

        res = a*b;
        ind = find(results.begin(), results.end(), res)-results.begin();

        graph[i][ind] = 1;
        //cout << "Finished " << i << "\n";

    }

    int bflow = bpm();
    cout << bflow << "\n";
    if(bflow < n1){
        cout << "impossible\n";
    }else{
        for(int i=0; i < n1; i++){
            auto &[a,b] = nums[i];
            long long res = a+b;
            int ind = find(results.begin(), results.end(), res)-results.begin();
            int cind = ind+n1+2;
            if(matchL[i] == ind){
                cout << a << " + " << b << " = " << res << "\n";
                continue;
            }

            res = a-b;
            ind = find(results.begin(), results.end(), res)-results.begin();
            cind = ind+n1+2;
            if(matchL[i] == ind){
                cout << a << " - " << b << " = " << res << "\n";
                continue;
            }

            res = a*b;
            ind = find(results.begin(), results.end(), res)-results.begin();
            if(matchL[i] == ind){
                cout << a << " * " << b << " = " << res << "\n";
                continue;
            }

            
        }
    }

    return 0;

}