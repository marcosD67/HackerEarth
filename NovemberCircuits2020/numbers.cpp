//Result: 100/100
#include <bits/stdc++.h>
using namespace std;

typedef long long int lli;
typedef string str;
#define MOD 1000000007;
#define timesaver ios_base::sync_with_stdio(false); cin.tie(NULL)

bool customSort(pair<lli, lli>&a, pair<lli, lli>&b) {
    return b.second - b.first > a.second - a.first;
       
}
int main()
{
    timesaver;
    int t;
    cin >> t;

    while(t--) {
        lli n;
        cin >> n;

        lli leftArr[n], rightArr[n];

        for(int i = 0; i < n; ++i){
            cin >> leftArr[i];
        }
        for(int i = 0; i < n; ++i){
            cin >> rightArr[i];
        }

        vector<pair<lli, lli>> arr(n);

        for(int i = 0; i < n; ++i) {
            arr[i] = {leftArr[i], rightArr[i]};
        }
        
        sort(arr.begin(), arr.end(), customSort);
        
        lli ans = 0;

        for(int i = 1; i <= n; ++i){
            pair<lli, lli> p = arr[i-1];
            lli total = (p.first * (i-1)) + (p.second * (n-i));
            ans += total;
        }
        cout << ans << '\n';
    }
    return 0;
}