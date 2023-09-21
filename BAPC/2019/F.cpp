
#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
#define INF 1e12
int main(){
    cin.tie(0);
    ios::sync_with_stdio(0);
    int n,k;
    cin >> k;
    vi ans;
    for(int photo_ind=0; photo_ind < k; photo_ind++){
        cin >> n;
        vi photo(n);
        set<int> left;
        set<int> right;
        

        for(int i=0; i < n; i++){
            cin >> photo[i];
            if(i > 1){
                right.insert(photo[i]);
            }
        }
        left.insert(photo[0]);
        for(int i=1; i < n-1; i++){
            // Try and find the smallest photo on the left which is bigger than the current photo
            auto next_bigger = left.lower_bound(photo[i]);
            if(next_bigger == left.end()){
                //cout << photo[i] << " IS BIGGER THAN ALL ELEMENTS IN LEFT\n";
                //for(auto i: left)cout << i << " ";
                //cout << "\n";
                left.insert(photo[i]);
                right.erase(photo[i+1]);
                continue;
            }
            int alice = *next_bigger;
            // Find bob
            //cout << "Have a bigger element to the left " << alice << "\n";
            auto maybe_bob = right.lower_bound(alice);
            if(maybe_bob != right.end()){
                ans.push_back(photo_ind+1);
                break;
            }
            //Failed to find them
            left.insert(photo[i]);
            right.erase(photo[i+1]);


        }

    }

    cout << ans.size() << "\n";
    for(auto a: ans) cout << a << "\n";
}