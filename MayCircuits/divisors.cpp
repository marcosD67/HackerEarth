//Result: 73/100
//Solved: 31:21:41
#include <bits/stdc++.h>
using namespace std;
 
#define lli long long int
#define str string
#define MOD 1000000007
#define max(a, b) { return a > b }
#define min(a, b) { return a < b}
#define pb push_back
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t = 0;
    lli n, k = 0;
		cin >> t;
		while(t--)
		{
			cin >> n >> k;
 
			lli total = n*(n+1)/2;
 
			for(int i = k; i <= n; i += k)
			{
					total -= i;
					lli curr = i;
 
					while(curr % k == 0)
					{
						curr /= k;
					}
 
					total += curr;
			}
 
			cout << total << '\n';
		}
    return 0;
}