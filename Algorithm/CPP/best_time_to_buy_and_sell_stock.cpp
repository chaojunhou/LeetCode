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
	int maxProfit(vector<int>& prices) {
		int n = prices.size();
		int minPrice = INT_MAX;
		int res = 0;
		for (auto price : prices)
		{
			if (price < minPrice)
			{
				minPrice = price;
			}
			else
			{
				res = max(res, price - minPrice);
			}
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
	cout << sol.maxProfit(nums) << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}

