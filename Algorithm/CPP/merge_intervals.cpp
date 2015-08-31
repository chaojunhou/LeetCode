# include<stdio.h>
# include <iostream>
# include <string>
# include <array>
# include <vector>
using namespace std;


struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};
class Solution {
public:
	static bool cmp(Interval left, Interval right)
	{
		return left.start < right.start;
	}
	vector<Interval> merge(vector<Interval>& intervals) 
	{
		sort(intervals.begin(), intervals.end(), cmp);
		vector<Interval> res;
		if (intervals.empty()) return res;
		res.push_back(intervals[0]);
		for (int i = 1; i < intervals.size(); ++i)
		{
			if (intervals[i].start > res.back().end)
			{
				res.push_back(intervals[i]);
			} else
			{
				res.back().end = max(res.back().end,intervals[i].end);
			}
		}
		return res;
	}
};


int main()
{
	vector<Interval> intervals = { Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18) };
	Solution sol;
	for (auto k : sol.merge(intervals))
	{
		cout << "(" << k.start << ","<<k.end << ")" << endl;
	}
	system("pause");
}

