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
	int maxArea(vector<int>& height) {
		int left = 0;
		int right = height.size()-1;
		int res = 0;
		while (left < right)
		{
			if (height[left] < height[right])
			{
				res = max(res, (right - left)*height[left]);
				left++;
			}
			else
			{
				res = max(res, (right - left)*height[right]);
				right--;
			}
		}
		return res;
	}
};

int main()
{
	Solution sol;
	vector<int> res = { 1, 3,2, 4 };
	cout<<sol.maxArea(res)<< " ";
	cout<< endl;
	system("pause");
	return 0;

}
