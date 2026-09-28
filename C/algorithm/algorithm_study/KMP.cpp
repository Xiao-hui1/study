#include <bits/stdc++.h>
using namespace std;

vector<int> prefixFunction(const string &pattern)
{
    int patternLength = pattern.size();
    vector<int> prefix(patternLength);

    // prefix[i] 是 pattern[0..i] 的最长相等真前后缀长度。
    for (int i = 1; i < patternLength; i++)
    {
        int matchedLength = prefix[i - 1];

        // 当前字符不匹配时，利用前缀表回退，无需重新比较已匹配部分。
        while (matchedLength > 0 && pattern[i] != pattern[matchedLength])
            matchedLength = prefix[matchedLength - 1];

        if (pattern[i] == pattern[matchedLength])
            matchedLength++;

        prefix[i] = matchedLength;
    }

    return prefix;
}

vector<int> kmpSearch(const string &text, const string &pattern)
{
    vector<int> positions;
    if (pattern.empty())
        return positions;

    // 先预处理模式串，再在线性扫描文本串时复用已匹配的信息。
    vector<int> prefix = prefixFunction(pattern);
    int matchedLength = 0;

    for (int i = 0; i < static_cast<int>(text.size()); i++)
    {
        // 失配时按前缀表回退，文本指针 i 不后退。
        while (matchedLength > 0 && text[i] != pattern[matchedLength])
            matchedLength = prefix[matchedLength - 1];

        if (text[i] == pattern[matchedLength])
            matchedLength++;

        if (matchedLength == static_cast<int>(pattern.size()))
        {
            // 记录 0 下标起点；回退后可继续找到重叠的匹配。
            positions.push_back(i - matchedLength + 1);
            matchedLength = prefix[matchedLength - 1];
        }
    }

    return positions;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string text, pattern;
    // 输入：文本串 模式串；输出所有匹配位置（从 0 开始）。
    cin >> text >> pattern;

    for (int position : kmpSearch(text, pattern))
        cout << position << ' ';
    cout << '\n';

    return 0;
}