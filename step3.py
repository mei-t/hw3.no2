# coding:utf-8
def readNumber(line, index):
    number = 0
    flag = 0
    keta = 1
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):   #小数点と数字の間。記号が出てくるまで繰り返す。
        if line[index] == '.':
            flag = 1
        else:
            number = number * 10 + int(line[index])
            if flag == 1:                   #小数点が出てきたら位は上がらない
                keta *= 0.1
        index += 1              #while文のループが繰り返されるごとにindexは増えていく
    token = {'type': 'NUMBER', 'number': number * keta}    #tokenはディクショナリ
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():              #index番目の文字列が数字だったら isdisit()
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMultiply(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)               #プログラム終了
        tokens.append(token)      #tokensにtokenを追加
    return tokens


def evaluate(tokens):   #掛け算の処理
    answer = 0
    tokens2 = []
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token. insert(n, a):n番目の要素の前にaを新しい要素として追加
    index = 1  #index初期化
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index + 1]['type'] == 'MULTIPLY':
                answer += tokens[index]['number'] * tokens[index+2]['number']
                print "answer = %f\n" % answer
                tokens2.append =  {'type': 'NUMBER', 'number':'answer'}
                index += 2
            else:
                tokens2.append(tokens[index])
        else:
            tokens2.append(tokens[index])
        index += 1
    return tokens2


def evaluate2(tokens2):    #足し算引き算の処理
    index = 1
    answer = 0
    while index < len(tokens2):
        if tokens2[index]['type'] == 'NUMBER':
            if tokens2[index - 1]['type'] == 'PLUS':
                answer += tokens2[index]['number']    #ダミーの+を入れたことによって最初の数字もこのif文に入る
            elif tokens2[index - 1]['type'] == 'MINUS':
                answer -= tokens2[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
        print "answer = %f\n" % answer
    return answer


def test(line, expectedAnswer):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:  #absは絶対値
        print "PASS! (%s = %f)" % (line, expectedAnswer)
    else:
        print "FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer)


# Add more tests to this function :)
def runTest():
    print "==== Test started! ===="
    test("1+2", 3)
    test("1.0+2.1-3", 0.1)
    test("2*3", 6)
    test("2+3*4+1", 15)
    print "==== Test finished! ====\n"

runTest()

while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    tokens2 = evaluate(tokens)
    answer = evaluate2(tokens2)
    print "answer = %f\n" % answer
