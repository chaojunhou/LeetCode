# include<stdio.h>
# include <iostream>
# include <string>
# include <array>
# include <vector>
using namespace std;
class Solution {
public:
    string convert(string s, int numRows) {
	 if (numRows == 1) return s;
		int position=-1, direction = 1;
  
		vector<string> vec(numRows);
    	for ( auto chr:s)
    	{
    		position += direction;
    		if (position == 0)
			{
				direction = 1;
			}
			else if (position == numRows-1)
			{
				direction = -1;
			}
			vec[position] += chr;
		}
		string ans;
		for (auto s:vec)  ans += s;
		return ans;
    }
};
int main()
{
	Solution sol;
	string s = "PAYPALISHIRING";
	int numRows = 3;

	cout<< sol.convert(s,numRows);

    return 0;
}

