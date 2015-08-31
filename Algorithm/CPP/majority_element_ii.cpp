# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;


class Solution {
public:
	vector<int> majorityElement(vector<int>& nums) {
		vector<int> res(2);
		res[0] = -1;
		int count1 = 0;
		int count2 = 0;
		res[1] = -1;

		for (auto num : nums)
		{
			if (num == res[0])
			{
				count1++;
			}
			else if (num == res[1])
			{
				count2++;
			}
			else if (count1 == 0)
			{
				res[0] = num;
				count1 = 1;
			}
			else if (count2 == 0)
			{
				res[1] = num;
				count2 = 1;
			}else
			{
				count1--;
				count2--;
			}
		}
		vector<int> ans;
		//cout << res[0] << " " << res[1] << endl;
		if (check(nums, res[0])) ans.push_back(res[0]);
		if ((res[0]!= res[1]) && check(nums, res[1])) ans.push_back(res[1]);
		return ans;
	}
	bool check(vector<int>& nums, int target)
	{
		int count = 0;
		int n = nums.size();
		for (auto num : nums)
		{
			if (num == target) count += 1;
		}
		return (count > n / 3);
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 1, 1, 1, 3, 3, 2, 2, 2};
	//nums = { 1, 2 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	for(auto k: sol.majorityElement(nums)) cout<<k<< endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
