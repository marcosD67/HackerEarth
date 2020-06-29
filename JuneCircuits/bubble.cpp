//Result: 100/100
//Solved: 2:10:43
#include <bits/stdc++.h>
using namespace std;
 
#define lli long long int
#define str string
#define MOD 1000000007
#define max(a, b) { return a > b }
#define min(a, b) { return a < b }
#define pb push_back
#define timesaver ios_base::sync_with_stdio(false); cin.tie(NULL)
#define For(i, a, b) for(int i = a; i < b; ++i)
int main()
{
    timesaver;
    
    int n;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }
 
    lli count = 0;
    bool hasSwapped = true;
 
    while(hasSwapped)
    {
        hasSwapped = false;
        count+=1;
        for(int i = 0; i < n-1; ++i)
        {
            if(arr[i] > arr[i+1])
            {
                hasSwapped = true;
                swap(arr[i], arr[i+1]);
            }
        }
    }
    cout << count << '\n';
}