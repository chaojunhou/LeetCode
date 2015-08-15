# include <stdio.h>
# include <iostream>
# include <vector>
# include <array>
# include <string.h>

using namespace std;

class solution {
public:
	int lengthOfLongestSubstring(string s) 
	{
		int dic[256];
		memset(dic,-1,sizeof(dic));
		//for(auto i =0;i<256;++i) dic[i]=-1;
		auto start = 0;
		int res = 0;
		for (auto i = 0; i < s.size();++i)
		{
			if (dic[s[i]] >= start)
			{
				start = dic[s[i]]+1; // 上次出现该字母的位置
			}
			dic[s[i]] = i;
			if ((i - start+1)>res)
				res = i - start+1;
		}
		return res;

	}
};


int main()
{


	solution sol;

	string s("fuck");
	cout<<sol.lengthOfLongestSubstring("c");
	cin.get();
	return 0;
}
