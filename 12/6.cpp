#include <vector>


int sum_range(const int* begin, const int* end) {
    int s = 0;
    for (int x : std::vector<int>(begin, end)) {
        s += x;
    }
    return s;
}
