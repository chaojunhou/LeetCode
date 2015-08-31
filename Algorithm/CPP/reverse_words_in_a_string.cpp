//# include <vector>
//# include <algorithm>
//# include <string>
//# include <deque>
//# include <iostream>
# include <vector>
# include <algorithm>
# include <string>
# include <deque>
# include <iostream>
using namespace std;







class Solution {
public:
	void reverse(string& s, int start, int end)
	{
		end--;
		while (start < end)
		{
			char tmp = s[start];
			s[start] = s[end];
			s[end] = tmp;
			start++;
			end--;
		}


	}
	void reverseWords(string &s)
	{
		while (s.size() >0 && s[0] == ' ')
		{
			s.erase(0, 1);
		}
		while (s.size() > 0 && s.back() == ' ')
			s.erase(s.size() - 1, 1);
		int i = 1;

		reverse(s, 0, s.size());

		int start = 0;
		for (int i = 0; i <= s.size(); ++i)
		{
			while (s[i] == ' ' && i < s.size() - 1 && s[i + 1] == ' ')
			{
				s.erase(i, 1);
			}
			if (i == s.size() || s[i] == ' ')
			{
				reverse(s, start, i);
				start = i + 1;
			}
		}
	}
};

int main()
{
	Solution sol;
	string s = "ADOBECODEBANC";
	string t = "the sky is blue";
	t = "   a   b ";
	t = "   a   b  c d   e  ";
	sol.reverseWords(t);
	cout << t << endl;
	cout << t.size() << endl;
	cout<<endl;
	system("pause");
	return 0;
}
