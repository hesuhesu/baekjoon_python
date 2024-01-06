#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    /*
        모듈러 연산 공식

        x mod n = (x mod n) mod n
        (a + b) mod n = (a mod n + b mod n) mod n
        (a * b) mod n = (a mod n * b mod n) mod n

    */

    long long n;
    long long num = 1;
    int result = 1;
    while (cin >> n) {
        num = 1;
        result = 1;
        while (1) {
            num = num % n;
            if (num == 0) {
                break;
            }
            num = (num * 10) + 1;
            num %= n;
            result++;
        }
        cout << result << '\n';
    }

    return 0;
}