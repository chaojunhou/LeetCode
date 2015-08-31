# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;


class Solution {
public:
	int trailingZeroes(int n) {
		int sum = 0;
		while (n)
		{
			
			n = n / 5;
			sum += n;
		}
		return sum;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 1,1,1,1,2,3 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	cout << sol.trailingZeroes(25) << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
