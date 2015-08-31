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
	int trap(vector<int>& height) {
		int left = 0;
		int right = height.size() - 1;
		int maxLeft = 0, maxRight = 0;
		int res;
		while (left <= right)
		{
			if (height[left] <= height[right])
			{
				if (height[left]>= maxLeft) maxLeft = height[left];
				else res += maxLeft - height[left];
				left++;
			}
			else
			{
				if (height[right] >= maxRight) maxRight = height[right];
				else res += maxRight - height[right];
				right--;
			}
		}
		return res;

	}
};
