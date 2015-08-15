# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
    bool isPowerOfTwo(int n) {
    	if (n<=0) return false;
    	return (!(n&(n-1))) ;        
    }
};
int  main()
{
	Solution sol;

	//nums = { -1 };
	cout<<sol.isPowerOfTwo(-2147483648);
	cin.get();
	return 0;
}
