# include <vector>
# include <iostream>
using namespace std;
class Solution {
public:
	int lengthOfLastWord(char* s) {
		int len = 0;
		while (*s != '\0')
		{
			if (*s != ' ')
			{
				len++;
				s++;
			}
			else  {
				s++;
				if (*s && *s != ' ')
				{
					len = 0;
				}
			}	
		}
		return len;
	}
};
int  main()
{
	Solution sol;

	//nums = { -1 };
	char* s = " a";
	cout << sol.lengthOfLastWord(s);
	cin.get();
	return 0;
}
