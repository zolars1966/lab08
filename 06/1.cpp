#include <iostream>

int main() {
    // Обычный for: изменение i в теле разрешено
    for (int i = 0; i < 3; i++) {
        std::cout << i << " ";
        i++; // компилируется, меняет ход цикла
    }
    std::cout << std::endl;

    // Аналог forc: i — const-ссылка, i++ в теле не скомпилируется
    {
        int __i = 0, __n = 3;
        for (const int &i = __i; i < __n; __i++) {
            std::cout << i << " ";
            // i++; // ошибка компиляции: i — const
        }
    }
    
    return 0;
}
