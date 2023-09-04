#include <bits/stdc++.h>

using namespace std;


double EPS = 1e-9;
typedef long long LL;
typedef vector<pair<int, int>> vpii;
struct Edge {
  int u, v;
  LL cap, flow;
  Edge() {}
  Edge(int u, int v, LL cap): u(u), v(v), cap(cap), flow(0) {}
};

struct Dinic {
  int N;
  vector<Edge> E;
  vector<vector<int>> g;
  vector<int> d, pt;
  
  Dinic(int N): N(N), E(0), g(N), d(N), pt(N) {}

  void AddEdge(int u, int v, LL cap) {
    if (u != v) {
      E.emplace_back(u, v, cap);
      g[u].emplace_back(E.size() - 1);
      E.emplace_back(v, u, 0);
      g[v].emplace_back(E.size() - 1);
    }
  }

  bool BFS(int S, int T) {
    queue<int> q({S});
    fill(d.begin(), d.end(), N + 1);
    d[S] = 0;
    while(!q.empty()) {
      int u = q.front(); q.pop();
      if (u == T) break;
      for (int k: g[u]) {
        Edge &e = E[k];
        if (e.flow < e.cap && d[e.v] > d[e.u] + 1) {
          d[e.v] = d[e.u] + 1;
          q.emplace(e.v);
        }
      }
    }
    return d[T] != N + 1;
  }

  LL DFS(int u, int T, LL flow = -1) {
    if (u == T || flow == 0) return flow;
    for (int &i = pt[u]; i < g[u].size(); ++i) {
      Edge &e = E[g[u][i]];
      Edge &oe = E[g[u][i]^1];
      if (d[e.v] == d[e.u] + 1) {
        LL amt = e.cap - e.flow;
        if (flow != -1 && amt > flow) amt = flow;
        if (LL pushed = DFS(e.v, T, amt)) {
          e.flow += pushed;
          oe.flow -= pushed;
          return pushed;
        }
      }
    }
    return 0;
  }

  LL MaxFlow(int S, int T) {
    LL total = 0;
    while (BFS(S, T)) {
      fill(pt.begin(), pt.end(), 0);
      while (LL flow = DFS(S, T))
        total += flow;
    }
    return total;
  }
};

double sqdist(pair<int, int> p, pair<int, int> q){
    return (p.first-q.first)*(p.first-q.first)+(p.second-q.second)*(p.second-q.second); 

}


int solve(double minDist, vpii blues, vpii reds){

    int tot = blues.size()+reds.size()+2;

    double sqDist = minDist*minDist;

    Dinic graph = Dinic(tot);

    for(int i=0; i < blues.size(); i++){
        graph.AddEdge(0, i+2, 1);

        for(int j=0; j < reds.size(); j++){
            double pdist = sqdist(blues[i], reds[j]);

            if(sqDist-pdist >= EPS){
                graph.AddEdge(i+2, j+blues.size()+2,1);
            }
        }
    }

    for(int i=0; i < reds.size(); i++){
        graph.AddEdge(i+2+blues.size(), 1,1);
    }

    return graph.MaxFlow(0,1);


}

int main(){
    int n,b,r;
    cin >> n >> b >> r;
    vector<pair<int,int>> blues(b);
    vector<pair<int, int>> reds(r);

    for(int i=0; i < b; i++){
        cin >> blues[i].first >> blues[i].second;
    }

    for(int i=0; i < r; i++){
        cin >> reds[i].first >> reds[i].second;
    }

    //cout << solve(1, blues, reds) << "\n";

    double low = 1;
    double high = 30000;


    while(abs(high-low) > EPS){
        double mid = (low+high)/2;
        int res = solve(mid, blues, reds);

        if(r+b-res >= n){
            low = mid;
        }else{
            high = mid;
        }
        
    }
    cout << fixed << setprecision(8) << low << "\n";

    return 0;

}