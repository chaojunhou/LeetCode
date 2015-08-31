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
	vector<int> getRow(int rowIndex) {
	
		vector<int> res;
		if (rowIndex == 0) return vector<int>(1, 1);
		for (int i = 1; i < rowIndex;++i)
		{
			res.push_back(1);
			for (int j = 1; j < tmp.size(); ++j)
				res.push_back(tmp[j] + tmp[j - 1]);
			res.push_back(1);
			tmp = res;
			res.clear();
		}
		return tmp;

	}
};
int main()
{
	Solution sol;


		for (auto x : sol.getRow(1)) cout << x << " ";
		cout << endl;

	system("pause");
	return 0;
}
