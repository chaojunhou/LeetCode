//# include <vector>
//# include <algorithm>
//# include <string>
//# include <deque>
//# include <iostream>
# include <vector>
# include <algorithm>
# include <string>
# include <deque>
# include <iostream>
using namespace std;
class Solution {
public:
	int findMin(vector<int>& nums) {
		int right = nums.size() - 1;
		int left = 0;
		while (left < right && nums[left] >= nums[right])
		{
			int mid = (right - left) / 2 + left;
			if (nums[mid] > nums[right])
			{
				left = mid+1;
			}
			else if (nums[mid] < nums[right])
			{
				right = mid;
			}
			else
			{
				left++;
			}

		}
		return nums[left];
	}
};

int main()
{
	Solution sol;
	vector<int> nums = {1,1,1,0,1};
	cout << sol.numDecodings("100") << endl;
	cout << sol.findMin(nums) << endl;
	system("pause");
}



