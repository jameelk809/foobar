def main():
    temp_memo = ['0'] * 101
    start_end_dict = {'Start': 1, 'End': 100}
    game_board = []
    current_pos = output1 = output2 = 0

    for i in range(10):
        if i % 2 == 1:
            game_board = input().split() + game_board
        else:
            game_board = input().split()[::-1] + game_board
    game_board = ['0'] + game_board

    for p, q in enumerate(game_board):
        if (q[0] == 'S' or q[0] == 'L') and q[1] == '(':
            if q[2].isdigit():
                temp_memo[p] = int(q[2:-1])
            else:
                temp_memo[p] = start_end_dict[q[2:-1]]
        else:
            temp_memo[p] = start_end_dict.get(q[2:-1], p)

    dice_user_inputs = list(map(int, input().split()))

    for q in dice_user_inputs:
        if current_pos + q < 101:
            current_pos += q
        while temp_memo[current_pos] != current_pos:
            if current_pos > temp_memo[current_pos]:
                output1 += 1
            else:
                output2 += 1
            current_pos = temp_memo[current_pos]

    if current_pos == 100:
        print(f'Possible {output1} {output2}')
    else:
        print(f'Not possible {output1} {output2} {"Start" if current_pos == 1 else current_pos}')


if __name__ == '__main__':
    main()
