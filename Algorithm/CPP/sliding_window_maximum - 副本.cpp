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
	int getMax(const deque<int> &deq)
	{
		int Max = INT_MIN;
		for (auto s : deq)
		{
			
			if (s > Max)
				Max = s;
		}
		return Max;
	}
	vector<int> maxSlidingWindow(vector<int>& nums, int k) {
		deque<int> deq;
		auto n = nums.size();
		int Max = INT_MIN;
		for (int i = 0; i < k; i++)
		{
			if (Max < nums[i])
				Max = nums[i];
			deq.push_back(nums[i]);
		}
		vector<int> res;
		res.push_back(Max);
		for (int i = k; i < n; ++i)
		{
			deq.pop_front();
			deq.push_back(nums[i]);
			if (nums[i] > Max)
				Max = nums[i];
			else
				Max = getMax(deq);
			res.push_back(Max);
		}
		return res;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 1, 3, -1, -3, 5, 3, 6, 7 };
	int k = 3;
	for (auto s : sol.maxSlidingWindow(nums, k))
	{
		cout << s<<",";
	}
	cin.get(); 
	return 0;
}



