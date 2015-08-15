# include <iostream>
# include <string>
using namespace std;



class Solution {
public:
	int strStr(string haystack, string needle) {
		if (needle.size() > haystack.size())
			return -1;
		for (auto i = 0; i <= (haystack.size()-needle.size()); ++i)
		{
			if (haystack.substr(i, needle.size()) == needle)
				return i;
		}
		return -1;


	}
};


int main()
{
	string haystack = "abced";
	string needle = "bc";
	Solution sol;
	cout << sol.strStr(haystack, needle);
	cin.get();
	return 0;
}
