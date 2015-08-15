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
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
	{
		int m = nums1.size();
		int n = nums2.size();
		int length = m + n;
		if (length % 2) // the odd
		{
			return  findKth(nums1.begin(), m, nums2.begin(), n, (length+1) / 2);
			//return  static_cast<double>(findKth(nums1.begin(), m, nums2.begin(), n, (length + 1) / 2));
		}
		else  // the even
		{
			return (findKth(nums1.begin(),m, nums2.begin(), n, length / 2) + findKth(nums1.begin(),m, nums2.begin(), n, length / 2 + 1))/2.0;
		}
	}
	int findKth(vector<int>::iterator start1, int size1, vector<int>::iterator start2, int size2, int k)
	{
		if (size1 == 0) return *(start2 + k - 1);
		if (size1 > size2)
		{
			return findKth(start2, size2, start1, size1, k);
		}
		if (k == 1)
			return min(*start1, *start2);
		int pa = min(size1, k / 2);
		int pb = k - pa;
		if (*(start1 + pa - 1) < *(start2 + pb -1))  return findKth(start1 + pa, size1 - pa, start2,size2, k - pa);
		else return findKth(start1, size1, start2 + pb, size2 - pb, pa);
	}
};
int  main()
{
	Solution sol;
	vector<int> nums1, nums2;
	for (int i = 0; i < 10; ++i)
	{
		nums1.push_back(rand() % 100);
		nums2.push_back(rand() % 100);
	}
	for (auto num1 : nums1) cout << num1 << " ";
	cout << endl;
	for (auto num2 : nums2) cout << num2 << " ";
	cout << endl;

	sort(nums1.begin(), nums1.end());
	sort(nums2.begin(), nums2.end());

	nums1 = {};
	nums2 = { 1 };
	for (auto num1 : nums1) cout << num1 << " ";
	cout << endl;
	for (auto num2 : nums2) cout << num2 << " ";
	cout << endl;
	cout<<sol.findMedianSortedArrays(nums1, nums2);
	cout<< endl;
	cin.get();
	return 0;
}
