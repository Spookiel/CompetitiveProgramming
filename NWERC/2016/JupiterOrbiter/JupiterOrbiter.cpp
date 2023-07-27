#include <bits/stdc++.h>
using namespace std;
const double EPS = 1e-9;


// Min Cost Max Flow when cost is an integer
struct Edge
{
    int from, to, capacity, cost;
    Edge(int from, int to, int capacity, int cost):from(from),to(to),capacity(capacity),cost(cost) {}
};

vector<vector<int>> adj, cost, capacity;

const int INF = 1e9;

void shortest_paths(int n, int v0, vector<int>& d, vector<int>& p) {
    d.assign(n, INF);
    d[v0] = 0;
    vector<bool> inq(n, false);
    queue<int> q;
    q.push(v0);
    p.assign(n, -1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        inq[u] = false;
        for (int v : adj[u]) {
            if (capacity[u][v] > 0 && d[v] > d[u] + cost[u][v]) {
                d[v] = d[u] + cost[u][v];
                p[v] = u;
                if (!inq[v]) {
                    inq[v] = true;
                    q.push(v);
                }
            }
        }
    }
}

int min_cost_flow(int N, vector<Edge> edges, int K, int s, int t) {
    adj.assign(N, vector<int>());
    cost.assign(N, vector<int>(N, 0));
    capacity.assign(N, vector<int>(N, 0));
    for (Edge e : edges) {
        adj[e.from].push_back(e.to);
        adj[e.to].push_back(e.from);
        cost[e.from][e.to] = e.cost;
        cost[e.to][e.from] = -e.cost;
        capacity[e.from][e.to] = e.capacity;
    }

    int flow = 0;
    int cost = 0;
    vector<int> d, p;
    while (flow < K) {
        shortest_paths(N, s, d, p);
        if (d[t] == INF)
            break;

        // find max flow on that path
        int f = K - flow;
        int cur = t;
        while (cur != s) {
            f = min(f, capacity[p[cur]][cur]);
            cur = p[cur];
        }

        // apply flow
        flow += f;
        cost += f * d[t];
        cur = t;
        while (cur != s) {
            capacity[p[cur]][cur] -= f;
            capacity[cur][p[cur]] += f;
            cur = p[cur];
        }
    }
    //cout << "GOT FLOW OF " << flow << "\n";
    if (flow < K)
        return -1;
    else
        return cost;
}



int main(){
    int n,q,s;

    cin >> n >> q >> s;
    // Have zero as the virtual source
    // Have one as the virtual sink
    vector<int> feeds(s);
    for(int i=0; i < s; i++){
        cin >> feeds[i];
        feeds[i]--;
    }
    vector<int> qcaps(q);
    for(int i=0; i < q; i++) cin >> qcaps[i];

    int totnodes = n+2+n*q*2;
    int offset = n+2;
    int targetSum = 0;
    vector<Edge> edges;
    int d;
    int sd_size;
    // Add the nodes using data first
    for(int i=0; i < n; i++){
        cin >> d;
        edges.push_back(Edge(i+2, 1, d, 0));
        vector<int> qinc(q, 0);
        for(int si=0; si < s; si++){
            cin >> sd_size;
            targetSum += sd_size;
            qinc[feeds[si]] += sd_size;
        }
        for(int qi=0; qi < q; qi++){
            edges.push_back(Edge(0, 2*n*qi+2*i+offset, qinc[qi], 0));


        }



        // Otherwise should add edges to next layer

        for(int qi=0; qi < q; qi++){

            int left = 2*qi*n+i*2;
            //cout << qi << " qind " << left << "\n";
            edges.push_back(Edge(left+offset, left+1+offset, qcaps[qi], 0));
            edges.push_back(Edge(left+1+offset, i+2, INF, 0));

            if(i == n-1){
                continue;
            }

            edges.push_back(Edge(left+1+offset, left+offset+2, INF, 0));
        //cout << "ADDING TO NEXT LAYER " << left+1+offset << " " << left+2+offset << "\n";
        }
    }
    //cout << "REACHED " << edges.size() << "\n";
    //int res = 0;
    int res = min_cost_flow(totnodes, edges, targetSum,0,1);
    //cout << "ANSWER: " << res << "\n";
    if(res == 0){
        cout << "possible\n";
    }else{
        cout << "impossible\n";
    }



}