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
	int removeElement(vector<int>& nums, int val) {
		int slow = 0;
		int fast = 0;
		int n = nums.size();
		while (fast < n)
		{
			if (nums[fast] != val)
			{
				nums[slow++] = nums[fast++];
			}
			else{
				fast++;
			}
		}
		return slow;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 1,1,2,3,3 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	cout << sol.removeElement(nums,2) << endl;
	for (auto k :nums )cout << k << endl;
	system("pause");
	return 0;
}
