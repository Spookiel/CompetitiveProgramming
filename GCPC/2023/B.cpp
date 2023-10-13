#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;

bool collinear(pll &a, pll &b, pll &c) {
  return (a.second - b.second) * (a.first - c.first) == (a.second - c.second) * (a.first - b.first);
}

bool solve(int k, vector<pll> points){
    if((int) points.size() <= 2*k) return true;
    if(k == 0){
        return points.size() == 0;
    }

    // Otherwise need to pick two random points
    int rp1 = rand() % points.size();
    int rp2;
    while(1){
        rp2 = rand() % points.size();
        if(rp2 != rp1) break;
    }

    pll p1 = points[rp1];
    pll p2 = points[rp2];

    vector<pll> rest;
    for(int i=0; i < points.size(); i++){
        if(i == rp1 || i == rp2)continue;

        //cout << "CALCULATING BETWEEN (" << p1.first << "," << p1.second << ") and (" << points[i].first << "," << points[i].second << ")\n"; 
        if(!collinear(p1, p2, points[i])){
            rest.push_back(points[i]);
        }
        
    }

    bool res = solve(k-1, rest);
    // if(res){
    //     cout << "FOUND ANSWER " << p1.first << " " << p1.second << " " << p2.first << " " << p2.second << "\n";
    //     for(auto p: rest) cout << "Point: " << p.first << " " << p.second << "\n";
    // }
    return res;


}


int main(){



    srand(time(NULL));
    int n;
    cin >> n;

    vector<pll> points(n);
    for(int i=0; i < n; i++) cin >> points[i].first >> points[i].second;


    bool can = false;
    for(int t=0; t < 2000000/n; t++){
        can = solve(3, points);
        if(can){
            cout << "possible\n";
            exit(0);
        }
    }
    cout << "impossible\n";







    return 0;
}