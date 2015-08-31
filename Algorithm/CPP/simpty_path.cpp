# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;

class Solution {
public:
	string simplifyPath(string path) 
	{
		vector<string> vec;
		string name;
		path += "/";  // to deal with the last split word
		for (auto chr : path)
		{
			if (chr == '/')
			{
				if (name == "" ) continue;
				if (name == "..") { if (vec.size() != 0) vec.pop_back(); }
				else if (name == "."){} // clear the . value to 
				else vec.push_back(name);
				name.clear();
			}
			else
			{
				name += chr;
			}

		}
		string res;
		if (vec.empty()) return "/";
		for (auto s : vec)
		{
			res += "/" + s;
		}
		return res;
	}
};
int  main()
{
	Solution sol;

	string path = "/a/./b/../../c/";
	//path = "/";
	path = "/...";
	path = "/..";
	cout << sol.simplifyPath(path) << endl;
	system("pause");
	return 0;
}
