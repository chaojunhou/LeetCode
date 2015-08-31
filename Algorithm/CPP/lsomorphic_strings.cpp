# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
# include <queue>
using namespace std;


class Solution {
public:
	bool isIsomorphic(string s, string t) 
	{  // two chars is injected to the same char 
		if (s.size() != t.size()) return false;
		unordered_map<char, char> myMap;
		for (int i = 0; i < s.size(); ++i)
		{
			if (myMap.find(s[i]) == myMap.end())
			{
				for (auto it = myMap.begin(); it != myMap.end(); ++it)
				{
					if (it->second == t[i]) return false;
				}
				myMap[s[i]] = t[i];
			}
			else
			{
				if (myMap[s[i]] != t[i] ) return false;
			}
		}
		return true;
	}
};
int  main()
{
	Solution sol;

	string path = "/a/./b/../../c/";
	//path = "/";
	path = "/...";
	path = "A man, a plan, a canal: Panama";
	path = " ";
	path = "1a2";
	string s = "ab";
	string t = "aa";
	cout << sol.isIsomorphic(s,t) << endl;

	system("pause");
	return 0;
}

