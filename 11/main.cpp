#include <iostream>
#include <vector>

int main() {
    int rows, cols;

    std::cin >> rows >> cols;

    std::vector<std::vector<int>> m(rows, std::vector<int>(cols));
    
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            std::cin >> m[i][j];

    long long sum = 0;
    int total = rows * cols;

    for (int k = 0; k < total; k++)
        sum += m[k / cols][k % cols];

    std::cout << sum << std::endl;
    
    return 0;
}
