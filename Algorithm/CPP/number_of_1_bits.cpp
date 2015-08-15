# include <iostream>
# include <string>
# include <stdlib.h>
# include <algorithm>
# include <vector>
# include <unordered_map>
# include <map>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) 
	{
		int ans = 0;
		while (n)
		{
			ans++;
			n = n & (n-1);
		}
		return ans;
        
    }
};


int main()
{

	Solution sol;
	cout<<sol.hammingWeight(3)<<endl; 
	cin.get();
	return 0;
}
