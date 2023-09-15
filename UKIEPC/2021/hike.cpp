


#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;


vi order;

vi graph[200005];
int seen[200005];

void rec(int node, int first){
    seen[node] = 1;
    if(first == 1){
        order.push_back(node);
    }

    for(auto child: graph[node]){

        if(!seen[child]) rec(child, 1-first);
    }

    if(!first){
        order.push_back(node);
    }
}



int main(){

    int n,m;
    int x,y;
    cin  >> n >> m;

    for(int i=0; i <= n; i++)graph[i] = {};
    fill(seen, seen+n+1,0);

    for(int i=0; i < m; i++){
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    rec(1,1);

    for(auto c: order) cout << c << " ";


    return 0;
}