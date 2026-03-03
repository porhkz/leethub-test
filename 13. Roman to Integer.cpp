class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> m;

        m.insert({'I', 1});
        m.insert({'V', 5});
        m.insert({'X', 10});
        m.insert({'L', 50});
        m.insert({'C', 100});
        m.insert({'D', 500});
        m.insert({'M', 1000});

        int result = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (m[s[i]] < m[s[i+1]]) {
                result -= m[s[i]];
            } else {
                result += m[s[i]];
            }
        }

        return result + m[s[s.length() - 1]];
    }
};