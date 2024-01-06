#include <iostream>
#include <string>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string A, B, C, D;
    long long result;

    cin >> A >> B >> C >> D;

    A += B;
    C += D;

    result = stoll(A) + stoll(C);
    cout << result;

    return 0;
}