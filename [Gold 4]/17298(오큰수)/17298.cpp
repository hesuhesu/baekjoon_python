#include <iostream>
#include <stack>

using namespace std;

stack<int> st;
int arr[1000001];
int NGE[1000001];

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < N; i++) {
        while (!st.empty() && arr[st.top()] < arr[i]) {
            NGE[st.top()] = arr[i];
            st.pop();
        }
        st.push(i);
    }

    while (!st.empty()) {
        NGE[st.top()] = -1;
        st.pop();
    }

    for (int i = 0; i < N; i++) {
        cout << NGE[i] << " ";
    }

    return 0;
}