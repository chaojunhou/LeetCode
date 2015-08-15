# include <iostream>
# include <string>
# include <stdlib.h>
# include <algorithm>
using namespace std;

class Solution {
public:
	bool isPalindrome(int x) 
	{
		if (x < 0 || (x != 0 && x % 10 == 0)) return false;
		int left = x;
		int right = 0;
		while (left > right)
		{
			right = right * 10 + left % 10;
			left = left / 10;
		}
		cout << left << " left" << endl;
		cout << right << " right" << endl; 
		return (left == right || left == right/10);

	}
};
int  main()
{
	Solution sol;

	//nums = { -1 };
	cout << sol.isPalindrome(0);
	cin.get();
	return 0;
}
