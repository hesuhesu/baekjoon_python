# 문제

Teams from variaous universities compete in ICPC regional contests for tickets to the ICPC World Finals. The number of tickets allocated to every regional contest may be different. The allocation method in our super region, Asia Pacific, is based on a parameter called site score.

Site scores will only count teams and universities solving at least one problem, in the regional contest or its preliminary contest TOPC. In 2020, the formula for calculating the site score of the Taipei-Hsinchu regional contest is much simpler than past years. Let

- $U_R$ be the number of universities solving at least one problem in the regional contest.
- $T_R$ be the number of teams solving at least one problem in the regional contest.
- $U_O$ be the number of universities solving at least one problem in TOPC.
- $T_O$ be the number of teams solving at least one problem in TOPC.

The site score of 2020 Taipei-Hsinchu regional contest will be $56U_R + 24T_R + 14U_O + 6T_O$. Please write a program to compute the site score of the 2020 Taipei-Hsinchu regional contest.

# 입력

The input has only one line containing four blank-separated positive integers $U_R, T_R, U_O,$ and $T_O$.

# 출력

Output the site score of the 2020 Taipei-Hsinchu regional contest.

# 제한

- $0 < U_R ≤ T_R ≤ 120$
- $0 < U_O ≤ T_O ≤ 1000$

[출처](https://www.acmicpc.net/problem/20254)
