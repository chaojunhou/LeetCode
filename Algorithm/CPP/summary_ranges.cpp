# include <vector>
# include <algorithm>
# include <string>
# include <stack>
# include <algorithm>
# include <deque>
# include <iostream>
using namespace std;




class Solution {
public:
	string range2str(int start, int end)
	{
		string res;
		res += to_string(start);
		if (start == end)		return res;
		res += "->";
		res += to_string(end);
		return res;		
	}
	vector<string> summaryRanges(vector<int>& nums) {
		int n = nums.size();
		vector<string> res;
		if (n == 0) return res;
		int start = nums[0];
		int pre = nums[0];
		
		for (int i = 1; i < n; i++)
		{
			if (nums[i] > pre + 1)
			{
				res.push_back(range2str(start, pre));
				start = nums[i];
			}
			pre = nums[i];
		}
		res.push_back(range2str(start, pre));
		return res;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = {-1};

	for(auto k:sol.summaryRanges(nums)) cout<<k<<" ";

	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
