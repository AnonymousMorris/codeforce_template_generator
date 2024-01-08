#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pb push_back
#define sz(x) (int)(x.size())
#define itr(x) x.begin(), x.end()
#define ref(x) (*(x))
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

// [ ] chill for one minute and evalute if the solution can be simpler

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
}
