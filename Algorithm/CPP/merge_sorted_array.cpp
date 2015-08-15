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
		void merge(vector<int>& nums1, int m, vector<int>& nums2, int n)
		{
			int len = m + n;
			while (m > 0 && n > 0)
			{
				if (nums1[m - 1] > nums2[n - 1])
				{
					nums1[len - 1] = nums1[m - 1];
					m--;
				}
				else
				{
					nums1[len - 1] = nums2[n - 1];
					n--;
				}
				len--;
			}
			while (m) nums1[--len] = nums1[--m];
			while (n) nums1[--len] = nums2[--n];
		}

};
int  main()
{
	Solution sol;
	vector<int> nums1, nums2;
	for (auto i = 0; i < 5; ++i)
	{
		nums1.push_back(rand() % 41);
		nums2.push_back(rand() % 41);
	}

	sort(nums1.begin(), nums1.end());
	sort(nums2.begin(), nums2.end());
	nums1.resize(13);
	nums1 = { 0 };
	nums2 = { 1 };
	for (auto num1 : nums1) cout << num1 << " ";
	cout << endl;
	for (auto num2 : nums2) cout << num2 << " ";
	cout << endl;
	sol.merge(nums1, 0, nums2, 1);
	for (auto num1 : nums1) cout << num1 << " ";
	cout << endl;
	cin.get();
	return 0;
}
