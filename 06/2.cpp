#include <iostream>

int counter = 0;
int getTo() {
    counter++;
    return 3;
}

int main() {
    // Обычный for: getTo() вызывается на каждой проверке условия
    counter = 0;
    for (int i = 0; i < getTo(); i++) {
        std::cout << i << " ";
    }
    std::cout << " | getTo вызвана " << counter << " раз" << std::endl;

    // Аналог forc: getTo() вызывается один раз
    counter = 0;
    {
        int __i = 0, __n = getTo();
        for (const int &i = __i; i < __n; __i++) {
            std::cout << i << " ";
        }
    }
    std::cout << " | getTo вызвана " << counter << " раз" << std::endl;
    return 0;
}
