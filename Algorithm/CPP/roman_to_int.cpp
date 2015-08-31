# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	int romanToInt(string s) 
	{
		unordered_map<char, int> myMap;
		myMap['M'] = 1000;
		myMap['D'] = 500;
		myMap['C'] = 100;
		myMap['L'] = 50;
		myMap['X'] = 10;
		myMap['V'] = 5;
		myMap['I'] = 1;
		int res = myMap[s[0]];
		for (int i = 1; i < s.size(); ++i)
		{
			cout << res << endl;
			res += myMap[s[i]];
		
			if (myMap[s[i-1]] < myMap[s[i]])
			{
				res -= 2 * myMap[s[i - 1]];
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
	cout << sol.romanToInt("MMXIV") << endl;
	system("pause");
	return 0;
}
