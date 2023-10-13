#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<int> vi;


int main(){
    int w,h;
    
    cin >> w >> h;
    vi heights(w);
    vector<vector<int>> blockers(w);
    for(int i=0; i < w; i++){
        cin >> heights[i];
        blockers[i].push_back(h);
        if(heights[i] > h){
            cout << "impossible\n";
            exit(0);
        }
    }

    bool can = true;
    for(int col=0; col < w; col++){
        // Try fill this column
        int cur = heights[col];
        sort(blockers[col].begin(), blockers[col].end());
        reverse(blockers[col].begin(), blockers[col].end());
        // cout << "COLUMN: " << col << "\n";
        // for(auto s: blockers[col]) cout << s << " ";
        // cout << "\n";
        while(blockers[col].size()){
            int nb = blockers[col].back();
            blockers[col].pop_back();
            // Try to fill to the next blocker if we can
            int diff = nb-cur;
            //cout << "CURRENT RANGE " << cur << " " << nb << "\n";
            if(diff%2 == 1){
                //Need to add a blocker at nb-1 in the next col
                if(col == w-1 || nb-1 < heights[col+1]){
                    // Can't put it here because it's blocked
                    //cout  << "FAILED " << col << " " << nb << "\n";
                    can = false;
                    break;
                }
                //cout << "ADDING BLOCKER TO NEXT COL " << col+1 << " " << nb-1 << "\n";
                blockers[col+1].push_back(nb-1);
                
            }
            cur = nb+1;

        }
        if(!can) break;
    }

    if(can) cout << "possible\n";
    else cout << "impossible\n";

    


    return 0;
}