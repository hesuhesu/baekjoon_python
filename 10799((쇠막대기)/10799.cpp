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
    stack<int> s;		// ���� ����
    for (int i = 0; i < str.size(); i++) {		// ���ڿ� ũ�⸸ŭ �ݺ�
        if (str[i] == '(')		// '('�� ������ ���ÿ� �ִ´�.
            s.push(str[i]);
        else {					// ')' �� ������ ���
            if (str[i - 1] == '(') {	// ������ '('�� ���Դٸ� pop�ϰ� ������ ũ�⸦ cnt�� �����ش�.
                s.pop();
                result += s.size();
            }
            else {			// �׷��� �ʴٸ� pop�ϰ� cnt�� 1�� ���Ѵ�.
                s.pop();
                result++;
            }
        }
    }
    cout << result;
    return 0;
}