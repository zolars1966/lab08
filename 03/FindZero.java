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
