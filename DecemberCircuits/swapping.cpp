/*
    Result: 61/100 TLE
    Solved: 129:04:15
*/
#include <bits/stdc++.h>
using namespace std;
 
#define lli long long int
#define str string
#define MOD 1000000007
#define pb push_back
#define timesaver ios_base::sync_with_stdio(false); cin.tie(NULL)
 
lli merge(int arr[], int temp[], int left, 
          int mid, int right) 
{ 
    int i, j, k; 
    int inv_count = 0; 
  
    i = left; 
    j = mid; 
    k = left;
    while ((i <= mid - 1) && (j <= right)) { 
        if (arr[i] <= arr[j]) { 
            temp[k++] = arr[i++]; 
        } 
        else { 
            temp[k++] = arr[j++]; 
  
            inv_count = inv_count + (mid - i); 
        } 
    } 
  
    while (i <= mid - 1) 
        temp[k++] = arr[i++]; 
  
    while (j <= right) 
        temp[k++] = arr[j++]; 
  
    for (i = left; i <= right; i++) 
        arr[i] = temp[i]; 
  
    return inv_count; 
} 
lli _mergeSort(int arr[], int temp[],  
                 int left, int right) 
{ 
    int mid = 0;
    lli inv_count = 0; 
    if (right > left) { 
        
        mid = (right + left) / 2; 
  
        
        inv_count += _mergeSort(arr, temp,  
                                left, mid); 
        inv_count += _mergeSort(arr, temp,  
                             mid + 1, right); 
  
        inv_count += merge(arr, temp, left,  
                           mid + 1, right); 
    } 
    return inv_count; 
} 
lli mergeSort(int arr[], int array_size) 
{ 
    int temp[array_size]; 
    return _mergeSort(arr, temp, 0, array_size - 1); 
}
 
int arr[7000];
 
int main()
{
    timesaver;
    
    int n;
 
    cin >> n;
 
    for(int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
 
    lli ans = 0;
 
    int between = 0;
    int first = 0, second = 0;
    for(int i = 0; i < n; ++i) {
        for(int j = i+1; j < n; ++j) {
            if(arr[j] < arr[i]) {
                int count = 0;
                for(int k = i+1; k < j; ++k) {
                    if(arr[k] > arr[j] && arr[k] < arr[i]) ++count;
                }
                if(count >= between) {
                    first = i;
                    second = j;
                    between = count;
                }
            }
        }
    }
    // cout << first << ' ' << second << '\n';
    swap(arr[first], arr[second]);
    
    ans = mergeSort(arr, n);
 
    cout << ans;
    return 0;
}
