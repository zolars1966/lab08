int sum_do(int n) {
    int s = 0, i = 1;
    do {
        s += i;
        i++;
    } while (i <= n);
    return s;
}
