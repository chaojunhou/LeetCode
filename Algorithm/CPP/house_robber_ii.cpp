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
	int rob(vector<int>& nums) {
		int n = nums.size();
		if (n == 0) return 0;
		if (n == 1) return nums[0];
		return max(rob(nums, 0, n - 1), rob(nums, 1, n));
	}
	int rob(vector<int>& nums, int start, int end) {

		int n = end - start;
		if (n == 1) return nums[start];
		vector<int> dp(n);
		dp[0] = nums[start];
		dp[1] = max(nums[start], nums[start + 1]);
		for (int i = 2; i < n; ++i)
		{
			dp[i] = max(dp[i - 2] + nums[i + start], dp[i - 1]);
		}
		return dp[n - 1];
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
	cout<< sol.rob(nums)<< endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}

