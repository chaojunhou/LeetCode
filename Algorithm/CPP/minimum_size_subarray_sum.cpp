# include <vector>
# include <iostream>
using namespace std;

class Solution {
public:
	int minSubArrayLen(int s, vector<int>& nums) {
		int left = 0;
		int right = 0;
		int res = nums.size();
		int sum = 0;
		while (right < nums.size())
		{
			if (sum >= s)
			{
				if (res > (right - left)) res = right - left;
				sum -= nums[left++];
			}
			else
			{
				sum += nums[right++];

				if (right == nums.size())
				{
					if (left == 0 && sum < s) return 0;
					while (sum >= s)
					{
						sum -= nums[left++];
					}
					left--;
					if (res > (right - left)) res = right - left;
				}
			}

		}
		return res;
	}
};

int main()
{
	Solution sol;
	vector<int> nums= { 2,3,1,2,4,3 };
	
	int s = 7;
	//nums = { 1, 4, 4 };
	//s = 4;
	cout << sol.minSubArrayLen(s, nums);
	cout<<endl;
	system("pause");
	return 0;
}
