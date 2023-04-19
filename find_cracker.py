def find_hack(arr):
    grade_of_b = ('A', 'B')
    scores_dict = {
        "A": 30,
        "B": 20,
        "C": 10,
        "D": 5
    }

    hack_list = []
    for i in arr:
        total_sum = 0
        count = 0
        if i[1] > 200:
            hack_list.append(i[0])
            continue

        for j in i[2]:
            asw = scores_dict[j]
            total_sum += asw
            if j in grade_of_b:
                count += 1
            else:
                count = 0
        if count >= 5:
            total_sum += 20

        if total_sum != i[1]:
            hack_list.append(i[0])

    return hack_list


def main():
    array = [
        ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
        ["name2", 120, ["B", "A", "A", "A"]],
        ["name3", 160, ["B", "A", "A", "A", "A"]],
        ["name4", 140, ["B", "A", "A", "C", "A"]]
    ]

    print(find_hack(arr=array))


if __name__ == '__main__':
    main()
