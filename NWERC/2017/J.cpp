#include <bits/stdc++.h>
using namespace std;


int main(){


    string s;
    cin >> s;
    int n = s.length();
    set<int> zeroes;
    zeroes.insert(-1);
    zeroes.insert(n);
    vector<int> to_solve;
    for(int i=0; i < n; i++){
        if(s[i]-48 == 0){
            zeroes.insert(i);
        }else if(s[i]-48 == 2){
            //cout << "Adding to solve " << i << "\n";
            to_solve.push_back(i);
        }
    }
    // cout << "{";
    // for(auto s: zeroes) cout << s << ",";
    // cout << "}\n";


    for(int two_ind=0; two_ind < n; two_ind++){
        if(s[two_ind]-48 != 2) continue;
        //cout << "Solving " << two_ind << "\n";
        auto leftit = zeroes.lower_bound(two_ind);
        auto rightit = zeroes.upper_bound(two_ind);
        leftit--;
        int adding = *rightit+*leftit-two_ind;
        //cout << "Left zero is " << *leftit << " Right zero is " << *rightit << "\n";
        //cout << "Adding one back at " << adding << "\n";
        if(adding == two_ind || s[adding]-48 != 2){
            zeroes.insert(adding);
        }else{
            if(adding != two_ind){
                s[adding] = 49;
            }
        }
        
        if(leftit != zeroes.begin()){
            zeroes.erase(leftit);
        }
        if(rightit != --zeroes.end()){
            zeroes.erase(rightit);
        }
        // cout << "{";
        // for(auto s: zeroes) cout << s << ",";
        // cout << "}\n";

        s[two_ind] = 48;

    }
//111111101111111111111111
//111111111111110111111111

    

    for(int i=0; i < n; i++){
        cout << 1-zeroes.count(i);
    }
    cout << "\n";
    
    return 0;

}