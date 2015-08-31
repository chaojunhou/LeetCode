# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
using namespace std;

class Solution {
public:
	string intToRoman(int num)
	{
		vector<int> values = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
		vector<string> numerals = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
		string res;
		for (int i = 0; i < values.size(); ++i)
		{
			while (values[i] <= num)
			{
				num -= values[i];
				res += numerals[i];
			}
		}
		return res;

	}

};


int main()
{
	Solution sol;
	vector<int> triangle = { 1,2,1,3,2,5};
	triangle = { 2, 1, 2, 3, 4, 1 };
	triangle = { 1, 2, 2 };
	vector<int> num = { 100, 4, 200, 1, 3, 2 };
	cout << sol.intToRoman(11) << endl;
	system("pause");
	return 0;
}
