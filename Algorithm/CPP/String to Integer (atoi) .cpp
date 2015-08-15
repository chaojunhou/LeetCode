# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
	int myAtoi(string str)
	{
		int i = 0;
		while (i != str.size())
		{
			if (str[i] == ' ')
				i++;
			else
				break;
		}
		int sign = 1;
		if (str[i] == '-')
		{
			sign = -1;
			i++;
		}
		else if (str[i] == '+')
		{
			i++;
		}
		int sum = 0;
		while (i != str.size())
		{
			if (ispunct(str[i]))
			{
				return 0;
			}
			else
			{
				if ('0'<=str[i] && str[i]<='9')
				{
					int num = str[i] - '0';
					if (sum > INT_MAX / 10 || (sum ==INT_MAX/10 && num>=8))
					{
						if (sign == 1)
							return INT_MAX;
						else
							return INT_MIN;
					}
					sum = 10 * sum + (str[i] - '0');
				}
				else
				{
					return sign*sum;
				}
			}
			i++;
		}
		return sign*sum;
	}
};
int  main()
{
	Solution sol;
	string str = "  -21474836439";
	str = "  -0012a42";
	//if ('0' <= 'a' && 'a' <= '9') cout << "coa" << endl;
	cout << sol.myAtoi(str) << endl;
	cin.get();
	return 0;
}
