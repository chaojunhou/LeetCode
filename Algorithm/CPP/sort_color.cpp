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
	void sortColors(vector<int>& nums)
	{
		int low = 0, high = nums.size()-1;
		int i = 0;
		for (i = low; i <= high;)
		{
			if (nums[i] == 0)
			{
				int tmp = nums[i];
				nums[i] = nums[low];
				nums[low] = tmp;
				low++;
				i++;
			}
			else if (nums[i] == 2)
			{
				int tmp = nums[i];
				nums[i] = nums[high];
				nums[high] = tmp;
				high--;
			}
			else i++;
		}
	}
	void sortColors1(vector<int>& nums)
	{
		int zero = 0;
		int two = nums.size() - 1;
		for (auto num : nums)
		{
			if (num == 0) zero++;
			if (num == 2) two--;
		}
		for (int i = 0; i < nums.size(); ++i)
		{
			if (i < zero)	nums[i] = 0;
			else if (i > two) nums[i] = 2;
			else nums[i] = 1;
		}
	}
};
int  main()
{
	Solution sol;
	vector<int> nums;
	for (int i = 0; i < 10; ++i)
	{
		nums.push_back(rand() % 3);
	}
	for (auto num : nums) cout << num << " ";
	cout << endl;
	sol.sortColors(nums);
	for (auto num : nums) cout << num << " ";
	cout<< endl;
	cin.get();
	return 0;
}
