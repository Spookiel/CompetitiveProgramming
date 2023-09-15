


#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

int main(){


    int n;
    cin >> n;

    string s1,s2;

    cin >> s1 >> s2;



    deque<char> d1 = {};
    deque<char> d2 = {};
    for(auto c: s1) d1.push_back(c);
    for(auto c: s2) d2.push_back(c);

    vector<char> ans;

    while(ans.size() < (n+1)/2){
        //cout << ans.size() << "\n";

        if(d1.size() <= d2.size()){
            vector<char> taken = {0,0,0,0};
            char comp = d1.front();
            d1.pop_front();
            int k=0;
            bool found = false;
            for(; k < 4; k++){
                taken[k] = d2.front();
                d2.pop_front();
                if(taken[k] == comp){
                    ans.push_back(comp);
                    found = true;
                    break;
                }
            }
            if(!found){
                for(int k=3; k >= 0; k--) d2.push_front(taken[k]);
            }


        }else{
            vector<char> taken = {0,0,0,0};
            char comp = d2.front();
            d2.pop_front();
            int k=0;
            bool found = false;
            for(; k < 4; k++){
                taken[k] = d1.front();
                d1.pop_front();
                if(taken[k] == comp){
                    ans.push_back(comp);
                    found = true;
                    break;
                }
            }
            if(!found){
                for(int k=3; k >= 0; k--) d1.push_front(taken[k]);
            }
        }


    }

    for(auto c: ans) cout << c;
    cout << "\n";



    return 0;
}