# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	vector<vector<string>> groupAnagrams(vector<string>& strs) {
		unordered_map<string, vector<string>> myMap;
		int n = strs.size();
		for (auto i = 0; i < n; ++i)
		{
			auto pre = strs[i];
			sort(pre.begin(), pre.end());
			myMap[pre].push_back(strs[i]);

		}
		vector<vector<string>> res(myMap.size());
		int k = 0;
		for (auto it = myMap.begin(); it != myMap.end(); ++it)
		{
			res[k].swap(it->second);
			sort(res[k].begin(), res[k].end());
			k++;
		}
		return res;

	}
};

int main()
{
	Solution sol;
	vector<string> strs = { "eat", "tea", "tan", "ate", "nat", "bat" };

	for (auto k : sol.groupAnagrams(strs))
	{
		for (auto x : k) cout << x << " ";
		cout << endl;
	}
	system("pause");
	return 0;
}
