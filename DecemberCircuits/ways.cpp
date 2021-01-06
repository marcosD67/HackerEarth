/*
    Result: 1/100
    Solved: 75:41:24
*/
#include <bits/stdc++.h>
using namespace std;
 
#define lli long long int
#define str string
#define MOD 1000000007
#define pb push_back
#define timesaver ios_base::sync_with_stdio(false); cin.tie(NULL)
int main()
{
    timesaver;
    
    int t;
 
    cin >> t;
 
    while(t--) {
        int n,m;
        cin >> n >> m;
 
        char arr[n][m];
 
        for(int i =0 ; i < n; ++i) {
            for(int j =0; j < m; ++j) {
                cin >> arr[i][j];
            }
        }
 
        int dp[n][m];
        memset(dp, 0, sizeof(dp));
 
        vector<int> row = {1, 1, 2};
        bool isBlocked = false;
        for(int i = 0; i < n; ++i) {
            if(arr[i][0] == '*')
                isBlocked = true;
            
            if(isBlocked) {
                dp[i][0] = -1;
                continue;
            }
            if(i < 2) {
                dp[i][0] = row[i];
            }
            else {
                row.push_back(row[i-1] + row[i-2] + row[i-3]);
                dp[i][0] = row[i] % MOD;
            }
        }
        isBlocked = false;
        for(int i = 0; i < m; ++i) {
            if(arr[0][i] == '*')
                isBlocked = true;
            
            if(isBlocked) {
                dp[0][i] = -1;
                continue;
            }
            dp[0][i] = row[i] % MOD;
        }
 
        for(int i = 1; i < n; ++i) {
            for(int j = 1; j < m; ++j) {
                if(arr[i][j] == '*') {
                    dp[i][j] = -1;
                    continue;
                }
                // cout << i << ' ' << j << ": ";
                lli row = 0, col = 0;
 
                for(int k = 0; k <= j; ++k) {
                    if(dp[i][k] == -1) {
                        row = 0;
                        break;
                    }
                    row += dp[i][k];
                }
 
                // cout << row << ", ";
                for(int k = i; k >= 0; --k) {
                    if(dp[k][j] == -1) {
                        col = 0;
                        break;
                    }
                    col += dp[k][j];
                }
                // cout << col << '\n';
 
                dp[i][j] = (row + col) % MOD;
 
            }
        }
 
        // for(int i =0 ; i < n; ++i) {
        //     for(int j =0; j < m; ++j) {
        //         cout << dp[i][j] << ' ';
        //     }
        //     cout << '\n';
        // }   
 
        cout << dp[n-1][m-1] << '\n';     
 
 
    }
    
    return 0;
}