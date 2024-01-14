#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

template<typename T> 
ostream& operator << (ostream& out, vector<T> v) {
    for(auto& i : v) {
        out << i << " ";
    }
    return out;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

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
