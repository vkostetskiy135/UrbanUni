def get_password(initial_number):
    result = []
    for x in range(1, round(initial_number / 2) + 1):
        for y in range(1, initial_number):
            if x == y:
                continue
            elif initial_number % (x + y) == 0:
                unique = True
                for pair in result:
                    if x in pair and y in pair:
                        unique = False
                if unique:
                    result.append([x, y])
    return ''.join(map(lambda x: ''.join([str(y) for y in x]), result))

answers = ['12', '13', '1423', '121524', '162534', '13172635', '1218273645', '141923283746', '11029384756',
           '12131511124210394857', '112211310495867', '1611325212343114105968', '1214114232133124115106978',
           '1317115262143531341251161079', '11621531441351261171089', '12151811724272163631545414513612711810',
           '118217316415514613712811910', '13141911923282183731746416515614713812911']
for input in range(3, 21):
    if get_password(input) in answers:
        print('success')
        continue
    print(f'Wrong!')

