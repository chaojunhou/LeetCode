# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;


class Solution {
public:

	int longestConsecutive(vector<int>& nums) 
	{
	
		unordered_map<int,int> myMap; // use the hash map to hold the start and the end of the sequence
		int res =1;
		for (auto num : nums)
		{
			if (myMap[num]) continue;
			myMap[num] = 1;
			if (myMap.find(num -1 ) != myMap.end())
			{
				int len = myMap[num] + myMap[num - 1];
				myMap[num] = len;
				myMap[num - len + 1]++;
				res = max(res, len);
			}
			if (myMap.find(num + 1) != myMap.end())
			{
				int len = myMap[num] + myMap[num + myMap[num+1]];
				myMap[num-myMap[num]+1] = len; // the start 
				myMap[num + myMap[num + 1]] = len; // the end of the sequence
				res = max(res, len);
			}
		}
		return res;
	}

};


int main()
{
	Solution sol;
	vector<int> triangle = { 1,2,1,3,2,5};
	triangle = { 2, 1, 2, 3, 4, 1 };
	triangle = { 1, 2, 2 };
	vector<int> num = { 100, 4, 200, 1, 3, 2 };
	cout << sol.longestConsecutive(num) << endl;
	system("pause");
	return 0;
}
