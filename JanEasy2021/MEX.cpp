/*Result: 10/100 TLE
Naive solution in C++
Same approach as my Python solution 
Sometimes HackerEarth gives more points to C++ solutions with similar Time Complexities as Python solutions
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
        int n;
        cin >> n;
        int arr[n];
 
        for(int i = 0; i < n; ++i) {
            cin >> arr[i];
        }
 
        set<int> divs;
 
        for(int i = 0; i < n; ++i) {
            for(int j = i+1; j < n; ++j) {
                divs.insert(__gcd(arr[i], arr[j]));
            }
        }
 
        int test = 1;
 
        while(1) {
            if(divs.find(test) == divs.end()) {
                cout << test << '\n';
                break;
            }
            ++test;
        }
    }
    
    return 0;
}