#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pb push_back
#define sz(x) (int)(x.size())
#define itr(x) x.begin(), x.end()
#define ref(x) (*(x))
#define prv(x) for(auto& pval : x) cout << pval << " "; cout << "\n";
#ifdef LOC
#define debug(...) cerr << #__VA_ARGS__ << " : "; for(auto& dval : {__VA_ARGS__}) cerr << dval << " "; cerr << "\n";
#else 
#define debug(...)
#endif

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
