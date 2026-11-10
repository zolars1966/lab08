#include <iostream>
#include <vector>

int main() {
    int n;

    std::cin >> n;

    std::vector<int> v(n);

    for (int &x : v)
        std::cin >> x;

    int last = v.back();

    for (int &x : v)
        x += last;

    int positive = 0, negative = 0;

    for (int x : v)
        if (x > 0) ++positive;
        else if (x < 0) ++negative;

    std::cout << positive << " " << negative << std::endl;
    
    return 0;
}
