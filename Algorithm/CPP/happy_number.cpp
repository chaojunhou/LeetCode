# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;


class Solution {
public:
	bool isHappy(int n) {
		vector<int> ans;
		while (true)
		{
			int sum = 0;
			while (n)
			{
				sum = sum+ (n % 10)*(n % 10);
				n = n / 10;
			}
			if (sum == 1) return true;
			
			if (find(ans.begin(), ans.end(), sum) != ans.end()) return false;
			ans.push_back(sum);
			n = sum;
			for (auto k : ans) cout << k << " ";
			cout << endl;
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
	cout << sol.isHappy(2) << endl; //1
	//0
	system("pause");
}
