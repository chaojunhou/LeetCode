# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	int hIndex(vector<int>& citations) {
		int left = 0;
		int n = citations.size();
		int right = n - 1;
		while (left <= right)
		{
			int mid = (right - left) / 2 + left;
			if (citations[mid] == (n - mid))return citations[mid];
			else if (citations[mid] > (n - mid)) right = mid - 1;
			else left = mid + 1;
		}
		return n - right-1;

	}
};
int main()
{
	Solution sol;
	vector<int> citations = { 4, 0, 6, 1, 5 };//4
	sort(citations.begin(), citations.end());
	
	cout << sol.hIndex(citations);
	cout << endl;


	system("pause");
	return 0;

}
