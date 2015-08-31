# include <stdio.h>
# include <iostream>
# include <vector>
# include <array>
# include <string.h>

using namespace std;

class Solution {
public:
	vector<int> findSubstring(string s, vector<string>& words)
	{
		unordered_map<string, int>  counts;
		vector<int> res;
		for (auto word : words)
		{			
			counts[word]++;
		}
		int num = words.size();
		int len = words[0].size();
		for (int i = 0; i < s.size() - num*len+1; ++i)
		{
			unordered_map<string, int> seens;
			int j = 0;
			for (; j < num; ++j)
			{
				string word = s.substr(i + j*len, len);
				if (counts.find(word) != counts.end())
				{
					seens[word]++;
					if (seens[word] > counts[word]) break;
				}
				else break;
			}
			if (j == num) res.push_back(i);
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
	string s = "barfoothefoobarman";
	vector<string> words = { "foo", "bar" };
	for (auto k : sol.findSubstring(s, words)) cout << k << " ";
	cout<<endl;
	system("pause");
	return 0;
}
