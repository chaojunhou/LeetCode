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
		vector<int> grayCode(int n)
		{
			vector<int> res(1, 0);
			for (auto i = 1; i < (1 << n); ++i)
			{
				res.push_back(res[i - 1] ^ (i&(-i)));  // find the rightmost bit and xor with the previous number
			}
			return res;
		}
};
int  main()
{
	Solution sol;




	for (auto num1 : sol.grayCode(4)) cout << num1 << " ";
	cout << endl;
	cin.get();
	return 0;
}
