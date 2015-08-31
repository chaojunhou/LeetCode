# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <stack>
# include <algorithm>
# include <time.h>
# include <queue>
using namespace std;

class Solution {
public:
	int addDigits(int num) {
		if (num == 0) return 0;
		//vector<int> res;
		while (true)
		{
			if (num < 10) return num;
			int sum = 0;
			while (num)
			{
				sum += (num % 10)*(num % 10);
				num = num / 10;
			}
			if (sum < 10) return sum;
			num = sum;
		}
	}


};


int main()
{
	Solution sol;
	vector<int> nums = {1,1,1,0,1
	};
	//cout << sol.numDecodings("101") << endl;
	//cout << sol.numDecodings("100") << endl; 
	//cout << sol.numDecodings("227") << endl;
	cout << sol.addDigits(2) << endl; //1
	//0
	system("pause");
}
