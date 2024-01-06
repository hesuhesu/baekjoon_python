#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string str;
    int result = 0;
    cin >> str;
    stack<int> s;		// 스택 생성
    for (int i = 0; i < str.size(); i++) {		// 문자열 크기만큼 반복
        if (str[i] == '(')		// '('가 들어오면 스택에 넣는다.
            s.push(str[i]);
        else {					// ')' 가 들어오는 경우
            if (str[i - 1] == '(') {	// 이전에 '('가 들어왔다면 pop하고 스택의 크기를 cnt에 더해준다.
                s.pop();
                result += s.size();
            }
            else {			// 그렇지 않다면 pop하고 cnt에 1을 더한다.
                s.pop();
                result++;
            }
        }
    }
    cout << result;
    return 0;
}