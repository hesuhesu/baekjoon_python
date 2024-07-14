# 문제

There are five ways to score points in american professional football:

1. Touchdown - 6 points
2. Field Goal - 3 points
3. Safety - 2 points
4. After touchdown
    
    a. 1 point (Field Goal or Safety) - Typically called the “Point after”
    
    b. 2 points (touchdown) - Typically called the “Two-point conversion”

(https://operations.nfl.com/the-rules/nfl-video-rulebook/scoring-plays/)

Given the box score values for two competing teams, calculate the point total for each team.

# 입력

There are two lines of input each containing five space-separated non-negative integers, T, F, S, P and C representing the number of Touchdowns, Field goals, Safeties, Points-after-touchdown and two-point Conversions after touchdown respectively. (0 ≤ T ≤ 10), (0 ≤ F ≤ 10), (0 ≤ S ≤ 10), (0 ≤ (P+C) ≤ T). The first line represents the box score for the visiting team, and the second line represents the box score for the home team.

# 출력

The single output line consists of two space-separated integers showing the visiting score and the home score respectively.

[출처](https://www.acmicpc.net/problem/24736)
