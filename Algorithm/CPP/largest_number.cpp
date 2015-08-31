# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;

string largestNumber(vector<int>& nums) {
		int n = nums.size();
		vector<string> arr;
		for (auto i : nums)
			arr.push_back(to_string(i));
	
		mergeSort(arr, 0, n - 1);
		string res;
		for (auto num : arr)
		{
			res += num;
		}
		if (res[0] == '0') return "0";
		return res;
	}
	void mergeSort(vector<string>& nums, int left, int right)
	{
		if (left < right)
		{
			int mid = (right - left) / 2 + left;
			mergeSort(nums, left, mid);
			mergeSort(nums, mid + 1, right);
			merge(nums, left, mid, right);
		}
	}
	void merge(vector<string>& nums, int left, int mid, int right)
	{
		vector<string> tmp(right-left+1);
		int start = left;
		int k = 0;
		int j = mid + 1;
		
		while (left <= mid && j <= right)
		{
			if ((nums[left]+nums[j]) > (nums[j]+nums[left]))
			{
				tmp[k++] = nums[left++];
			}
			else
			{
				tmp[k++] = nums[j++];
			}
		}
		while (left <= mid) tmp[k++] = nums[left++];
		while (j <= right) tmp[k++] = nums[j++];
		for (int i = 0; i < k; ++i)	nums[start + i] = tmp[i];
	}
};

int main()
{
	Solution sol;
	vector<int> strs = { 3, 30, 34, 5, 9 };
	cout << sol.largestNumber(strs) << endl;
	system("pause");
	return 0;
}
