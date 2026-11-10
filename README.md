# Языки программирования
## Лабораторная работа 8

#### Задание 1

```python
x = [int(t) for t in input().split()]
i = 0
while i < len(x) and x[i] >= i and x[i] <= 2*i:
   i += 1
print(i)
```

### Задание 2

```python
x = [int(t) for t in input().split()]
i = 0
while i < len(x) and (x[i] < i or x[i] >= 2*i) and (x[i] < 3*i or x[i] >= 4*i):
   i += 1
print(i)
```

### Задание 3

```java
public class FindZero {
    public static void main(String[] args) {
        int[][] a = {
            {1, 2, 3},
            {4, 0, 6},
            {7, 8, 9}
        };

        int foundRow = -1, foundCol = -1;

        search:
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                if (a[i][j] == 0) {
                    foundRow = i;
                    foundCol = j;
                    break search;
                }
            }
        }

        if (foundRow != -1) {
            System.out.println("Первый ноль найден в позиции: [" + foundRow + "][" + foundCol + "]");
        } 
        else {
            System.out.println("Ноль не найден");
        }
    }
}
```

Инструкция `break search;` прерывает оба вложенных цикла сразу, так как `search` — это метка внешнего цикла.

### Задание 4

Программа:

```python
a = list(range(10))
b = [a.pop() - x for x in a]
print(*b)
```

`a.pop()` удаляет последний элемент списка `a`, а итератор `for x in a` идёт по тому же самому списку, который изменяется во время итерации.

На каждой итерации:

1. `x = a[0] = 0`; `a.pop()` возвращает 9, удаляет его; `b.append(9 - 0) = 9`. Список стал `[0,1,2,3,4,5,6,7,8]`.
2. `x = a[1] = 1`; `a.pop()` возвращает 8; `b.append(8 - 1) = 7`. Список `[0,1,2,3,4,5,6,7]`.
3. `x = a[2] = 2`; `a.pop()` возвращает 7; `b.append(7 - 2) = 5`. Список `[0,1,2,3,4,5,6]`.
4. `x = a[3] = 3`; `a.pop()` возвращает 6; `b.append(6 - 3) = 3`. Список `[0,1,2,3,4,5]`.
5. `x = a[4] = 4`; `a.pop()` возвращает 5; `b.append(5 - 4) = 1`. Список `[0,1,2,3,4]`.

Теперь индекс итератора равен 5, а длина списка — 5, поэтому итерация завершается (индекс вышел за границы).

Итог: `b = [9, 7, 5, 3, 1]`, и `print(*b)` выводит `9 7 5 3 1`.

### Задание 5

```cpp
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
```

### Задание 6

1. **Переменная цикла `i` — константная ссылка (`const int &`) на изменяемую переменную `__i`.** Внутри тела цикла нельзя изменить `i` (компилятор запретит), но при этом `i` — это ссылка, а не копия. В обычном `for (int i = from; ...)` переменная `i` изменяема, и её можно менять в теле цикла (что часто приводит к ошибкам). Здесь изменение счётчика `__i` спрятано, а `i` доступна только для чтения. Что (очевидно) спасает от случайных изменений переменной в теле цикла.

2. **Значения `from` и `to` вычисляются один раз до начала цикла и сохраняются в `__i` и `__n`.** В стандартном `for (int i = from; i < to; i++)` выражение `to` вычисляется на каждой проверке условия, а `from` — один раз. Если `to` — вызов функции с побочными эффектами или дорогое выражение, поведение и производительность различаются. Здесь граница фиксируется. Что полезно, например, при изменении длины массива/вектора, по которому мы "бежим" в цикле.

Демонстрация первого различия (нельзя изменить `i`):

```cpp
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
```

Демонстрация второго различия (граница вычисляется один раз):

```cpp
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
```

В первом случае `getTo()` вызывается 4 раза (для i = 0, 1, 2 и финальная проверка), во втором — ровно 1 раз.

### Задание 7

Python с конструкцией `for ... break ... else`:

```python
nums = [int(t) for t in input().split()]

for x in nums:
    if x < 0:
        print(x)
        break
else:
    print("Отрицательных чисел нет")
```

Если найден отрицательный элемент — печатаем его и выходим по `break`, блок `else` пропускается. Если цикл дошёл до конца без `break` — срабатывает `else` и печатается сообщение.

Аналогичная программа на C++:

```cpp
#include <iostream>
#include <vector>

int main() {
    int n;

    std::cin >> n;

    std::vector<int> v(n);
    
    for (int &x : v) std::cin >> x;

    bool found = false;

    for (int x : v) {
        if (x < 0) {
            std::cout << x << std::endl;
            found = true;
            break;
        }
    }

    if (!found)
        std::cout << "Отрицательных чисел нет" << std::endl;

    return 0;
}
```

Изменения в алгоритме: в C++ нет конструкции `for ... else`, поэтому приходится вводить флаговую переменную `found`. В Python факт выхода по `break` отслеживается самим циклом, а в C++ — вручную. Это делает C++ версию чуть более громоздкой.

### Задание 8

<img width="960" height="960" alt="task8_regions" src="https://github.com/user-attachments/assets/e699693b-7908-42f6-a03b-f0df11f2e98f" />

Множества на координатной плоскости:

- **0**: правая полуплоскость от вертикальной прямой x = 5 (включая её) вместе с верхней полуплоскостью от горизонтальной прямой y = -5 (включая её). Это правый верхний квадрант, ограниченный прямыми x = 5 и y = -5.
  A0 = { (x, y) | x ∈ [5; +∞), y ∈ [-5; +∞) }

- **1**: всё, что не попало в 0, но лежит левее оси Y (x < 0) или ниже прямой y = -5 (y < 0). Это объединение двух полуплоскостей за вычетом области A0.
  A1 = { (x, y) | (x < 0 ∨ y < 0) ∧ (x, y) ∉ A0}
  В более явном виде: A1 = { (x, y) | x < 0, y < -5 } ∪ { (x, y) | x < 0, y ≥ -5, x < 5 } ∪ { (x, y) | x ≥ 0, y < 0, ... }.
  Или ваашпе: A1 = ( {x < 0} ∪ {y < 0} ) \ A0.

- **2**: оставшаяся область — там, где x ≥ 0, y ≥ 0, но не выполнено (x ≥ 5 и y ≥ -5). Поскольку y ≥ 0 уже даёт y ≥ -5, остаётся x ≥ 0, y ≥ 0 и x < 5. То есть полоса 0 ≤ x < 5, y ≥ 0.
  A2 = { (x, y) | x ∈ [0; 5), y ∈ [0; +∞) }

### Задание 9

```python
def t(i):
    return i >= 1000


left = -1
right = 10**18

while right - left > 1:
    mid = (left + right) // 2

    if t(mid):
        right = mid
    else:
        left = mid

print(right)
```

### Дополнительное задание 1

```cpp
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
```

### Дополнительное задание 2

#### 2.1. Ветвление в полной форме (if-else), ARM64

```cpp
int classify(int x) {
    if (x > 0) {
        return 1;
    } else {
        return -1;
    }
}
```

Ассемблер (ARM64, macOS, `g++ -O0 -S`):

```asm
__Z8classifyi:
    sub     sp, sp, #16
    str     w0, [sp, #8]        ; сохранить x на стек
    ldr     w8, [sp, #8]        ; загрузить x
    subs    w8, w8, #0          ; сравнить x с 0, выставить флаги
    b.le    LBB0_2              ; если x <= 0 — на else
    b       LBB0_1              ; иначе — на then
LBB0_1:                         ; then: x > 0
    mov     w8, #1
    str     w8, [sp, #12]       ; результат = 1
    b       LBB0_3              ; на выход
LBB0_2:                         ; else: x <= 0
    mov     w8, #-1
    str     w8, [sp, #12]       ; результат = -1
    b       LBB0_3              ; на выход
LBB0_3:                         ; выход
    ldr     w0, [sp, #12]       ; вернуть результат через w0
    add     sp, sp, #16
    ret
```

#### 2.2. Ветвление в краткой форме (if без else), ARM64

```cpp
int abs_val(int x) {
    int r = x;
    if (x < 0) {
        r = -x;
    }
    return r;
}
```

Ассемблер (ARM64, macOS, `g++ -O0 -S`):

```asm
__Z7abs_vali:
    sub     sp, sp, #16
    str     w0, [sp, #12]       ; сохранить x на стек
    ldr     w8, [sp, #12]
    str     w8, [sp, #8]        ; r = x
    ldr     w8, [sp, #12]       ; загрузить x
    tbz     w8, #31, LBB0_2     ; если бит 31 (знак) равен 0, т.е. x >= 0 — пропустить тело
    b       LBB0_1
LBB0_1:                         ; тело if: x < 0
    ldr     w9, [sp, #12]       ; загрузить x
    mov     w8, #0
    subs    w8, w8, w9          ; r = 0 - x = -x
    str     w8, [sp, #8]
    b       LBB0_2              ; на выход
LBB0_2:                         ; выход
    ldr     w0, [sp, #8]        ; вернуть r через w0
    add     sp, sp, #16
    ret
```

#### 2.3. Цикл с предусловием (while), ARM64

```cpp
int sum_while(int n) {
    int s = 0, i = 1;
    while (i <= n) {
        s += i;
        i++;
    }
    return s;
}
```

Ассемблер (ARM64, macOS, `g++ -O0 -S`):

```asm
__Z9sum_whilei:
    sub     sp, sp, #16
    str     w0, [sp, #12]       ; сохранить n на стек
    str     wzr, [sp, #8]       ; s = 0 (wzr — регистр нуля)
    mov     w8, #1
    str     w8, [sp, #4]        ; i = 1
    b       LBB0_1              ; безусловный переход к проверке условия
LBB0_1:                         ; проверка условия (начало итерации)
    ldr     w8, [sp, #4]        ; загрузить i
    ldr     w9, [sp, #12]       ; загрузить n
    subs    w8, w8, w9          ; сравнить i и n (i - n)
    b.gt    LBB0_3              ; если i > n — выход из цикла
    b       LBB0_2              ; иначе — тело цикла
LBB0_2:                         ; тело цикла
    ldr     w9, [sp, #4]        ; загрузить i
    ldr     w8, [sp, #8]        ; загрузить s
    add     w8, w8, w9          ; s = s + i
    str     w8, [sp, #8]
    ldr     w8, [sp, #4]        ; загрузить i
    add     w8, w8, #1          ; i = i + 1
    str     w8, [sp, #4]
    b       LBB0_1              ; безусловный переход к проверке
LBB0_3:                         ; выход
    ldr     w0, [sp, #8]        ; вернуть s через w0
    add     sp, sp, #16
    ret
```

#### 2.4. Цикл с постусловием (do-while), ARM64

```cpp
int sum_do(int n) {
    int s = 0, i = 1;
    do {
        s += i;
        i++;
    } while (i <= n);
    return s;
}
```

Ассемблер (ARM64, macOS, `g++ -O0 -S`):

```asm
__Z6sum_doi:
    sub     sp, sp, #16
    str     w0, [sp, #12]       ; сохранить n на стек
    str     wzr, [sp, #8]       ; s = 0
    mov     w8, #1
    str     w8, [sp, #4]        ; i = 1
    b       LBB0_1              ; безусловный переход на тело (do)
LBB0_1:                         ; тело цикла (начало итерации)
    ldr     w9, [sp, #4]        ; загрузить i
    ldr     w8, [sp, #8]        ; загрузить s
    add     w8, w8, w9          ; s = s + i
    str     w8, [sp, #8]
    ldr     w8, [sp, #4]        ; загрузить i
    add     w8, w8, #1          ; i = i + 1
    str     w8, [sp, #4]
    b       LBB0_2              ; переход к проверке условия
LBB0_2:                         ; проверка условия (while)
    ldr     w8, [sp, #4]        ; загрузить i
    ldr     w9, [sp, #12]       ; загрузить n
    subs    w8, w8, w9          ; сравнить i и n
    b.le    LBB0_1              ; если i <= n — обратно на тело
    b       LBB0_3              ; иначе — выход
LBB0_3:                         ; выход
    ldr     w0, [sp, #8]        ; вернуть s через w0
    add     sp, sp, #16
    ret
```

#### 2.5. Цикл со счётчиком (for), ARM64

```cpp
int sum_for(int n) {
    int s = 0;
    for (int i = 1; i <= n; i++) {
        s += i;
    }
    return s;
}
```

Ассемблер (ARM64, macOS, `g++ -O0 -S`):

```asm
__Z7sum_fori:
    sub     sp, sp, #16
    str     w0, [sp, #12]       ; сохранить n на стек
    str     wzr, [sp, #8]       ; s = 0 (wzr — регистр нуля)
    mov     w8, #1
    str     w8, [sp, #4]        ; i = 1 (инициализация цикла)
    b       LBB0_1              ; безусловный переход к проверке условия
LBB0_1:                         ; проверка условия (начало итерации)
    ldr     w8, [sp, #4]        ; загрузить i
    ldr     w9, [sp, #12]       ; загрузить n
    subs    w8, w8, w9          ; сравнить i и n (i - n)
    b.gt    LBB0_4              ; если i > n — выход из цикла
    b       LBB0_2              ; иначе — тело
LBB0_2:                         ; тело цикла
    ldr     w9, [sp, #4]        ; загрузить i
    ldr     w8, [sp, #8]        ; загрузить s
    add     w8, w8, w9          ; s = s + i
    str     w8, [sp, #8]
    b       LBB0_3              ; переход к шагу
LBB0_3:                         ; шаг цикла (инкремент)
    ldr     w8, [sp, #4]        ; загрузить i
    add     w8, w8, #1          ; i = i + 1
    str     w8, [sp, #4]
    b       LBB0_1              ; обратно к проверке
LBB0_4:                         ; выход
    ldr     w0, [sp, #8]        ; вернуть s через w0
    add     sp, sp, #16
    ret
```

#### 2.6. Цикл по коллекции (range-based for), ARM64

```cpp
#include <vector>

int sum_range(const int* begin, const int* end) {
    int s = 0;
    for (int x : std::vector<int>(begin, end)) {
        s += x;
    }
    return s;
}
```

Ассемблер (ARM64, macOS, `g++ -O0 -S`). Основная функция и ключевые вспомогательные:

```asm
__Z9sum_rangePKiS0_:                    ; sum_range(begin, end)
    sub     sp, sp, #112
    stp     x29, x30, [sp, #96]
    add     x29, sp, #96
    stur    x0, [x29, #-8]              ; begin
    stur    x1, [x29, #-16]             ; end
    stur    wzr, [x29, #-20]            ; s = 0
    ldur    x1, [x29, #-8]              ; begin
    ldur    x2, [x29, #-16]             ; end
    add     x0, sp, #40                 ; временный vector на стеке
    bl      vector<int>::vector(const int*, const int*)   ; создать вектор из диапазона
    ldur    x0, [x29, #-32]             ; указатель на вектор
    bl      vector<int>::begin()
    str     x0, [sp, #32]               ; __begin = begin()
    ldur    x0, [x29, #-32]
    bl      vector<int>::end()
    str     x0, [sp, #24]               ; __end = end()
    b       LBB0_1
LBB0_1:                                 ; проверка условия цикла
    add     x0, sp, #32
    add     x1, sp, #24
    bl      operator!=(__wrap_iter<int>, __wrap_iter<int>)   ; __begin != __end
    tbnz    w0, #0, LBB0_3              ; если не равны — в тело
    b       LBB0_2
LBB0_2:                                 ; выход из цикла
    add     x0, sp, #40
    bl      vector<int>::~vector()      ; разрушить временный вектор
    b       LBB0_5
LBB0_3:                                 ; тело цикла
    add     x0, sp, #32
    bl      __wrap_iter<int>::operator*()   ; разыменовать итератор
    ldr     w8, [x0]                    ; x = *it
    str     w8, [sp, #20]
    ldr     w9, [sp, #20]
    ldur    w8, [x29, #-20]
    add     w8, w8, w9                  ; s += x
    stur    w8, [x29, #-20]
    b       LBB0_4
LBB0_4:                                 ; шаг цикла
    add     x0, sp, #32
    bl      __wrap_iter<int>::operator++()  ; ++it
    b       LBB0_1
LBB0_5:                                 ; выход
    ldur    w0, [x29, #-20]             ; вернуть s
    ldp     x29, x30, [sp, #96]
    add     sp, sp, #112
    ret
```

Вспомогательные функции:

```asm
__wrap_iter<int>::operator*():          ; разыменование
    ldr     x8, [sp, #8]
    ldr     x0, [x8]                    ; вернуть указатель, лежащий в итераторе
    ret

__wrap_iter<int>::operator++():         ; инкремент итератора
    ldr     x0, [sp, #8]
    ldr     x8, [x0]
    add     x8, x8, #4                  ; сдвиг на 4 байта (sizeof(int))
    str     x8, [x0]
    ret

operator!=(__wrap_iter<int>, __wrap_iter<int>):   ; сравнение итераторов
    ; ... загрузить указатели из двух итераторов ...
    subs    x8, x0, x8                  ; вычесть указатели
    cset    w0, ne                      ; w0 = (x0 != x8)
    ret
```
