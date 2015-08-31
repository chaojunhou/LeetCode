# include <vector>
# include <algorithm>
# include <string>
# include <stack>
# include <algorithm>
# include <deque>
# include <iostream>
# include <time.h>
using namespace std;

class Solution {
public:
	vector<string> findRepeatedDnaSequences(string s) {
		int n = s.size();
		vector<string> res;
		if (n < 11) return res;
		unordered_map<int, int> dic;
		for (int i = 0; i <= n - 10; i++)
		{
			if (dic[str2int(s.substr(i, 10))]++ == 1)
				res.push_back(s.substr(i,10));
		}
		return res;
	}
	int str2int(string s)
	{
		int res = 0;
		for (int i = 0; i < s.size(); ++i)
		{
			res = (res << 3) | (s[i] & 7);
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

	string s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
	for (auto k : sol.findRepeatedDnaSequences(s))cout << k << " , ";
	cout<<endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
