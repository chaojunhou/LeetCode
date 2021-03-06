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
	uint32_t reverseBits1(uint32_t n) 
	{
		int res = 0;
		for (int i = 0; i < 32; ++i)
		{
			res = res << 1;
			res |= n & 1;
			n = n >> 1;
		}
		return res;
	}
	uint32_t reverseBits(uint32_t n)
	{
		n = (n >> 16) | (n << 16);
		n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
		n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
		n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
		n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
		return n;
	}

};
int  main()
{
	Solution sol;
	uint32_t n = 43261596;
	cout << sol.reverseBits(n) << endl;

	system("pause");
	return 0;
}
