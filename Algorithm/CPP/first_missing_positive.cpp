# include <vector>
# include <algorithm>
# include <string>
# include <stack>
# include <algorithm>
# include <deque>
# include <iostream>
# include <time.h>
using namespace std;
class Solution {
public:

	int firstMissingPostive(vector<int>& nums)
	{
		int i =0, n = nums.size();
		for(i=0; i<n; ++i)
		{
			while(nums[i]>0 && nums[i]<=n && nums[i] != nums[nums[i]-1])
			swap(nums[i], nums[nums[i]-1]); // loop until find the position,means the index plus one is the value
		}

		for(auto i=0; i<n; ++i)
		{
			if(nums[i] != i+1)
				return i+1;
		}
		return n+1;
	}

};

int main()
{
	Solution sol;
	srand((unsigned)time(NULL));

	vector<int>	 vec;
		for(int i=0; i<10;i++)
	{
		vec.push_back(rand()%11);         
	}
	//vec = {3, 4, -1, 1};
	for(auto v:vec) cout<<v<<" ";
	cout<<endl;
	cout<<sol.firstMissingPostive(vec)<<endl;

	system("pause");
	return 1;
}


