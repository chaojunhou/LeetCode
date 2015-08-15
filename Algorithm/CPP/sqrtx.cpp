# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;

# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
	public:
		int mySqrt(int x)
		{
			if (x == 1 || x == 0) return x;
			int n = x / 2;
			int pre = n;
			while (true)
			{
				n = (n + x / n) / 2;
				if (n < 46361)  // magic number, in case of that the number over flow
				{
					if (n*n == x || ((n*n < x) && ((n + 1)*(n + 1) > x)))return n;
				}
				if (pre == n)
					return n;
				pre = n;
			}
		}

	};

};
int  main()
{
	Solution sol;

	cout << sol.mySqrt(808909662) << "  1" << endl;
	cout<<sol.mySqrt(1)<<"  2"<<endl;
	cout << sol.mySqrt(INT_MAX)<<"  3"<<endl;
	cin.get();
	return 0;
}
