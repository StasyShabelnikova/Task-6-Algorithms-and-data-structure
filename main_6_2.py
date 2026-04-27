# ======== Для красивой печати треугольника Паскаля ========


from task_6_2 import Pascal_triangle


def main():
    n = int(input("Введите кол-во строк в треугольнике паскаля: "))
    triangle = Pascal_triangle(n)
    width = len(" ".join(map(str, triangle[-1])))
    for i in range (0, n):
        beauty_tr = " ".join(map(str, triangle[i])).center(width)
        print (beauty_tr)


if __name__ == "__main__":
    main()