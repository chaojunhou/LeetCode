# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;



class Solution {
public:
	int countDigitOne(int n) {
		long long base = 1, res = 0, last = 0;
		while (n >= base)
		{
			int index = (n / base) % 10;
			long long remain = n%base;
			if (index > 1) res += index*last + base;
			else if (index == 1) res += index*last + remain + 1;
			else res += index*last;
			last = last * 10 + base;
			base *= 10;
		}
		return res;
	}
};
int main()
{
	Solution sol;

	cout << sol.countDigitOne(1410065408);
	cout << endl;
	system("pause");
	return 0;

}

