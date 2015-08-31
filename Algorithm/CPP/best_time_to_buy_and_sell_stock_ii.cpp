# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;

class Solution {
public:
	int maxProfit(vector<int>& prices) {
		int res = 0;
		int n = prices.size();
		if (n < 2) return 0;
		int minPrice = prices[0];
		for (int i = 1; i < n; ++i)
		{
			if (prices[i - 1] > prices[i])
			{
				res += prices[i - 1] - minPrice;
				minPrice = prices[i];
			}
			else
			{
				minPrice = min(minPrice, prices[i]);
			}
		}
		if (prices[n - 1] != minPrice) res += prices[n - 1] - minPrice;
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
