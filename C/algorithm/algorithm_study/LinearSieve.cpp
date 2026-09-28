#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int limit;
    cin >> limit;

    // minPrimeFactor[x] 为 x 的最小质因子；值为 0 代表尚未被筛去。
    vector<int> minPrimeFactor(limit + 1, 0);
    vector<int> primes;

    for (int number = 2; number <= limit; number++)
    {
        // 没有更小的质因子，说明 number 本身是质数。
        if (minPrimeFactor[number] == 0)
        {
            minPrimeFactor[number] = number;
            primes.push_back(number);
        }

        for (int prime : primes)
        {
            ll composite = 1LL * number * prime;
            if (composite > limit)
                break;

            minPrimeFactor[composite] = prime;

            // prime 已是 number 的最小质因子时停止，
            // 使每个合数只被其最小质因子标记一次，复杂度为 O(n)。
            if (prime == minPrimeFactor[number])
                break;
        }
    }

    // 输出 [2, limit] 内所有质数。
    for (int prime : primes)
        cout << prime << ' ';
    cout << '\n';

    return 0;
}