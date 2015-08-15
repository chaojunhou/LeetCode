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
	double myPow(double x, int n) {

		if (n == 0) return 1.0;
		if (n < 0)
		{
			if (n != INT_MIN) 	return 1.0 / myPow(x, -n);
			else{
				return 1.0 / (myPow(x, INT_MAX)*x);
			}
		}
		if (n == 1) return x;
		if (n % 2 == 1)
		{
			return myPow(x*x,n/2)*x;
		}
		else{
			return myPow(x*x, n / 2);
		}
	}
};


int main()
{
	Solution sol;


	int target = 7;

	cout << sol.myPow(1.0,INT_MIN) << endl;

	system("pause");
	return 0;
}
