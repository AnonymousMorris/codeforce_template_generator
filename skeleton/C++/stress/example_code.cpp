```
#include<bits/stdc++.h>

using namespace std;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

int main() {
    cout << 1 << " ";
    int n = 1000, k = 1500;
    cout << n << " " << k << "\n";
    for(int i = 0; i < n; i++) {
        cout << rng() % 1500 + 1 << " ";
    }
    cout << "\n";
    for(int i = 0; i < n; i++) {
        cout << rng() % 1500 + 1 << " ";
    }
    cout << "\n";
}
```
