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

	vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
		
		if (intervals.empty()) return vector<Interval>{newInterval};
		vector<Interval> res;
		int i = 0;
		while (i < intervals.size() && intervals[i].end < newInterval.start)
		{
			res.push_back(intervals[i]);
			i++;
		}
		res.push_back(newInterval);
		if (i != intervals.size())
		{
			if (intervals[i].start < res.back().start) res.back().start = intervals[i].start;
		}
		
		for (; i < intervals.size(); ++i)
		{
			if (res.back().end < intervals[i].start)
			{
				res.push_back(intervals[i]);
			}
			else{
				res.back().end = max(res.back().end,intervals[i].end);
			}
		}
		return res;
		
	}
};


int main()

{
	vector<Interval> intervals = { Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10) ,Interval(12,16)};
	Solution sol;
	for (auto k : sol.insert(intervals,Interval(4,9)))
	{
		cout << "(" << k.start << ","<<k.end << ")" << endl;
	}
	system("pause");
}

