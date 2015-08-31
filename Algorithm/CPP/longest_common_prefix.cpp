# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;



class Solution {
public:	
	string longestCommonPrefi(vector<string>& strs)
	{
		if (strs.empty())return "";
		int n = strs.size();
		for (int i = 0; i < strs[0].size(); i++)
		{
			for (int j = 1; j < strs.size(); j++)
			{
				if (strs[j][i] != strs[0][i] || i >= strs[j].size())
					return strs[0].substr(0, i);
			}
		}
		return strs[0];

	}
};
