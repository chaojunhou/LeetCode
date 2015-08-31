# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
# include <queue>
using namespace std;


class Solution {
public:
	int titleToNumber(string s) {
		int res = 0;
		for (auto ch : s)
		{
			res = res * 26 + ch - 'A' + 1;
		}
		return res;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 4, 1, 2, 7, 5, 3, 1};
	//nums = { 1, 2 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	string word1 = "vintner";
	string word2 = "writers";
	cout << sol.titleToNumber("AB") << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}

