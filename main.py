matrix = [
    [" ", 1, 2, 3],
    [1, '-','-','-'],
    [2, '-','-','-'],
    [3, '-','-','-']
]

def draw_pf (matrix):
#функция рисующая игровое поле
    for i in matrix:
        print(*i)

def who_won(matrix):
#функция определяющая победителя
    winners = ((1,1,1,2,1,3),(2,1,2,2,2,3),(3,1,3,2,3,3),
               (1,1,2,1,3,1),(1,2,2,2,3,2),(1,3,2,3,3,3),
               (1,1,2,2,3,3),(1,3,2,2,3,1))
    for i1,i2,i3,i4,i5,i6 in winners:
        if matrix[i1][i2] == matrix[i3][i4] == matrix[i5][i6] and matrix[i1][i2] != "-":
            return matrix[i1][i2]

def pl_move(matrix,pl_sign):
#функция запрашивающая ход игрока
    print ("Игрок "+pl_sign+" Ваш ход!")
    while True:
        while True:
            try:
                x = int(input("Введите номер строки: "))
                y = int(input("Введите номер столбца: "))
                break
            except:
                print ("Вводите цифры!")
        if 1<=x<=3 and 1<=y<=3:
                if matrix[x][y] == "-":
                    matrix[x][y] = pl_sign
                    break
                else:
                    print("Такой ход уже был. Ячейка занята. Повторите ход.")
        else:
            print("""Введенные данные вне диапазона игрового поля! 
Введите данные снова.""")

def get_pl_sign():
        sign = input("""Введите знак каким будите играть "X" или "O"= """).strip(" ").upper()
        while sign != "X" and sign !="O":
            print("Введите правильные знаки!")
            sign = input("""Введите знак каким будите играть "X" или "O"= """).strip(" ").upper()
        return sign

def main(matrix):
    pl_sign = get_pl_sign()
    count = 0
    while True:
        draw_pf (matrix)
        pl_move(matrix,pl_sign)
        count +=1

        if count >4:
            pl_win = who_won(matrix)

            if pl_win=="X" or pl_win=="O":
                draw_pf(matrix)
                print("Поздравляем! Выиграл игрок "+pl_win)
                break

        if count == 9:
            draw_pf(matrix)
            print ("Ничья")
            break
        pl_sign = "X" if pl_sign == "O" else "O"

main(matrix)


