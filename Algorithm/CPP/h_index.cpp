# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;



class Solution {
public:
	int hIndex(vector<int>& citations) {
		int n = citations.size();
		if (n < 1)return 0;
		int count = 0;
		for (auto citation : citations)
		{
			if (citation != 0)
			{
				count++;
			}
		}
	
		int i;
		int sum;
		while (count)
		{
			i = 0;
			sum = 0;
			for (int i = 0; i < n; i++)
			{
				if (citations[i] >= count)
				{
					sum++;
				}
			}
			if (sum >= count)return count;
			else count--;
		}
		return 0;
	}
	
};

int main()
{
	Solution sol;
	vector<int> res = { 3,0,6,1,5 };
	cout << sol.hIndex(res) << " ";
	cout<< endl;
	system("pause");
	return 0;

}
