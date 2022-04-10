#递归下降
import ffp

tokens = []
token_path = './token.txt'

# 读取token序列
ft = open(token_path, 'r')
for line in ft.readlines():
    for token in line.strip('\n').strip('').split(' '):
        tokens.append(token)

index = 0

def Start(name):
    match_formula = ''
    for formula in ffp.dic[name].split(' | '):
        if tokens[index] in ffp.predictSet[name + ' = ' + formula]:
            match_formula = formula
            break
    print(name + ' = ' + match_formula)
    for v in match_formula.split(' '):
        if v == '$':
            break
        elif v in ffp.vt:
            Match(v)
        else:
            Start(v)
    return


def Match(v):
    global index
    index += 1
    return

