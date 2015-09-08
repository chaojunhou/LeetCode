# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
		int n = nums.size();
		if (n == 1) return nums[0];
		k = n - k;
		//cout << k << " k " << n << " n " << endl;
		return findKthSmallest(nums,0,n-1, k);
	}
	int findKthSmallest(vector<int>& nums, int left, int right, int k)
	{
		int pivort = nums[right];
		int i = left;
		for (int j = left; j < right; j++)
		{
			if (nums[j] <= pivort)
			{
				swap(nums[i++], nums[j]);
			}
			
		}
		swap(nums[i], nums[right]);
		if(i-left == k) return nums[i];
		if (i-left > k) return findKthSmallest(nums,left,i-1, k);
		else return findKthSmallest(nums, i+1, right, k - (i -left+1));
	}
};
int main()
{
	Solution sol;
	int numRows = 5;
	for (auto k : sol.generate(numRows))
	{
		for (auto x : k) cout << x << " ";
		cout << endl;
	}
	system("pause");
	return 0;
}

