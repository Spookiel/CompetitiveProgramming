
#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
#define INF 1e15

long long dp[16400][20];


vector<int> can_play(int i, int round){

    vi ans;
    int stem = (i >> round) << round;

    int roundth_bit = (i >> (round-1))&1;
    if(!roundth_bit){
        // Need to toggle the round-1th bit of the stem to one
        stem |= (1 << (round-1));
    }

    for(int i=0; i < 1 << (round-1); i++){
        ans.push_back(stem+i);
    }
    return ans;
}

int main(){

    int r;
    
    cin >> r;
    vector<long long> skills(1 << r);
    for(int i=0; i < 1 << r; i++){
        fill(dp[i], dp[i]+r+1, INF);
    }
    for(int i=0; i < 1 << r; i++) cin >> skills[i];
    ///for(auto o: can_play(4, 2)) cout << o << "\n";
    
    for(int i=0; i < 1 << r; i++) dp[i][0] = 0;



    for(int round = 1; round <= r; round++){
        // cout << "--- BEFORE ROUND " << round << "-----\n";
        // for(int player=0; player < 1 << r; player++) cout << dp[player][round] << " ";
        // cout << "\n";
        for(int player=0; player < 1 << r; player++){
            for(auto oplayer: can_play(player, round)){
                if(oplayer == player){
                    continue;
                }
                //cout << player << " PLAYS " << oplayer << " IN THE " << round << "th  ROUND\n";
                long long tcost = 0;
                if(skills[player] < skills[oplayer]){
                    tcost = (skills[oplayer]-skills[player])*(skills[oplayer]-skills[player]);
                }
                long long acost = dp[player][round-1]+dp[oplayer][round-1]+tcost;
                if(acost < dp[player][round]){
                    dp[player][round] = acost;
                    // oplayer loses in the round-1 round
                }
            
                //cout << "COST OF PLAYER " << player << " PLAYING " << oplayer << "IN ROUND " << round << " " << acost << "\n";
            }
        }
        // cout << "--- AFTER ROUND " << round << "-----\n";
        // for(int player=0; player < 1 << r; player++) cout << dp[player][round] << " ";
        // cout << "\n";
    }

    cout << dp[0][r] << "\n";
    
    return 0;
}