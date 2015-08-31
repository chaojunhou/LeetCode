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
	bool isScramble(string s1, string s2) {
		//cout << s1 << " s1 " << s2 << " s2" << endl;
		if (s1 == s2) return true;
		int n = s1.size();
		if (n != s2.size())return false;
		string s(s1);
		string t(s2);
		sort(s.begin(), s.end());
		sort(t.begin(), t.end());
		if (s != t)return false;

		
		for (int i = 1; i < n; i++)
			if ((isScramble(s1.substr(0, i), s2.substr(0, i)) && isScramble(s1.substr(i), s2.substr(i))) ||
				(isScramble(s1.substr(0, i), s2.substr(n-i,i)) && isScramble(s1.substr(i,n-i), s2.substr(0, n-i))))
				return true;
		return false;


	}
};



int  main()
{
	Solution sol;
	string s1 = "abc";
	string s2 = "bca";
	cout << sol.isScramble(s1, s2);
 	cout << endl;

	system("pause");
	return 0;
}
