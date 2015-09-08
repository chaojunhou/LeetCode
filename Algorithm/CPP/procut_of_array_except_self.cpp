# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	vector<int> productExceptSelf(vector<int>& nums) {
		
		int product = 1;
		int n = nums.size();
		vector<int> res(n,0);
		int count = 0;
		for (int i = 0; i < n; i++)
		{
			if (nums[i] == 0) count++;
			else 	product *= nums[i];
		}
		if (count > 1)
		{
			return res;
		}
		else if (count == 1)
		{
			for (int i = 0; i < n; i++)
			{
				if (nums[i] == 0) res[i] = product;
			}
		}
		else{
			for (int i = 0; i < n; i++)
			{
				res[i] = product / nums[i];
			}
		}
		return res;
		
	}
};

int main()
{
	Solution sol;
	vector<int> res = { 1, 2, 3, 4 };
	for (auto k : sol.productExceptSelf(res)) cout << k << " ";
	cout<< endl;
	system("pause");
	return 0;

}

