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
	int maximumGap(vector<int>& nums) {
		int n = nums.size();
		if (n < 2)return 0;
		int res; 
		vector<int> num(radixSort(nums));
		for (int i = 1; i < n; i++)
			res = max(res, num[i] -num[i - 1]);
		return res;
	}
	vector<int> radixSort(vector<int>& nums)
	{
		int mask = 0;
		for (int i = 0; i < 32; i++)
		{
			vector<vector<int>>  bucket(2);
			mask = 1 << i;
			for (auto num : nums)
			{
				if (num&mask)
				{
					bucket[1].push_back(num);
				}
				else{
					bucket[0].push_back(num);
				}
			}
			nums.clear();
			for (auto lst : bucket)
				for (auto val : lst)
					nums.push_back(val);
		}
		return nums;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 1, 3, 2, 8 };
	cout << sol.maximumGap(nums) << endl;
	for (auto k : sol.radixSort(nums)) cout << k << " ";
	cout << endl;

		
			
	system("pause");
	return 0;
}

