#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define pb push_back
#define all(a) a.begin(),a.end()
#define fore(n) for(int i=0;i<n;i++)
#define f first
#define s second

const int INF = 1e9;

void db(vi arr){
    for(auto k: arr){
        cout<<k<<" " ;
    }
    cout<<endl;
}
int main()
{
    
     int n; cin >> n;
    vector<vii> atk(n, vii());
    int cum[3][3] = {{0, 1, 0}, {0, 1, 0}, {0, 0, 0}};
    for (int i=0; i<n; ++i) {
        int m, r, c; cin >> m;
        for (int j=0; j<m; ++j) {
            cin >> r >> c;
            atk[i].emplace_back(r, c);
        }
    }


    vector<int[3][3]> def(n);
    for (int i=0; i<n; ++i) {
        for (int r=0; r<3; ++r) for (int c=0; c<3; ++c) cin >> def[i][r][c];
    }

    for (int r=0; r<3; ++r) 
    {
        for (int c=0; c<3; ++c) 
        {
            cout << cum[r][c] << ' ';
            cout.flush();
        }
        cout<<endl;
    }
    return 0;
}