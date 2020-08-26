// Result: 100/100
// Solved: 135:18:27
// Digit Dynamic Programming Solution C++ version (submitted first)
#include <bits/stdc++.h>
using namespace std;
 
#define lli unsigned long long int
#define str string
#define MOD 1000000007
#define max(a, b) { return a > b }
#define min(a, b) { return a < b}
#define pb push_back
 
const int M = 18;
lli dp[M][M][2];
lli count(int pos, int cnt, int tight, vector<int> num, int k)
{
    if(pos == num.size())
    {
        if(cnt == num.size())
        {
            return 1;
        }
        return 0;
    }
 
    if(dp[pos][cnt][tight] != -1)
    {
        return dp[pos][cnt][tight];
    }
 
    lli ans = 0;
 
    int limit = (tight ? 9 : num[pos]);
    for(int digit = 0; digit <= limit; ++digit)
    {
        int currCnt = cnt;
 
        if(digit % k == 0)
        {
            ++currCnt;
            int currTight = tight;
            if(digit < num[pos])
            {
                currTight = 1;
            }
            ans += count(pos+1, currCnt, currTight, num, k);
        }
 
       
    }
 
    return dp[pos][cnt][tight] = ans;
}
 
lli solve(lli n, lli k)
{
    vector<int> num;
    
    while(n)
    {
        num.push_back(n%10);
        n /= 10;
    }
 
    reverse(num.begin(), num.end());
 
    memset(dp, -1, sizeof(dp));
 
    return count(0,0,0,num,k);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
 
    while(t--)
    {
        lli l, r, k;
        cin >> l >> r >> k;
 
        cout << solve(r, k) - solve(l-1, k) << '\n';
    }
    return 0;
}