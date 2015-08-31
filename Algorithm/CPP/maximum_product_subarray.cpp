# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	int maxProduct(vector<int>& nums)
	{
		if (nums.empty()) return 0;
		int n = nums.size();
		int maxhere = 1;
		int minhere =1;
		int maxsofar = INT_MIN;
		for (int i = 0; i < n; ++i)
		{
			if (nums[i] < 0) swap(maxhere, minhere); 
			maxhere = max(maxhere*nums[i], nums[i]);// compare with the now element
			minhere = min(minhere*nums[i], nums[i]);
			maxsofar = max(maxsofar, maxhere);
		}
		return maxsofar;
	}
};
int main()
{
	Solution sol;
	vector<int> nums = { -2};
	nums = { 3, 2, -2, 4 };
	//nums = { -4, -3 };
	nums = { -2, -3, 7 };
	int n = sol.maxProduct(nums);
	cout<<n<<endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
