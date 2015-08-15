
# include <iostream>
# include <string>
# include <stdlib.h>
# include <algorithm>
using namespace std;



class Solution {
public:
	int reverse(int x) {
		int sign = 1;
		if (x < 0)
		{
			sign = -1;
			x = -x;
			if (x<0) return 0;
		}
		int sum = 0;
		while (x)
		{
			if (sum > INT_MAX / 10) return 0;
			sum = sum * 10 + (x % 10);
			//cout << sum << " ";
			if (sum < 0)return 0;
			x = x / 10;
		}
		
		return sign*sum;
		
	}
};


int main()
{

	Solution sol;
	cout << sol.reverse(-2147483648) << endl;
	cout << sol.reverse(1463847412) << endl;
	cout << sol.reverse(1056389759) << endl;
	cin.get();
	return 0;
}
