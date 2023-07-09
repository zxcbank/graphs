def ms_init():
    '''
    вводится матрица смежностей
    :return: матрица смежностей
    '''
    v = int(input())
    k = v
    ms = []
    while k > 0:
        ms.append(list(map(int, input().split())))
        k -= 1
    return ms, v


def sr_init():
    """
    в каждой строчке через пробел два числа = ребро
    :return: список ребер
    """
    v, e = list(map(int, input().split()))
    sr = []
    while e > 0:
        sr.append(list(map(int, input().split())))
        e -= 1
    return sr, v


def ss_init():
    '''
    в i-й строчке вводятся номера смежных вершин через пробел
    :return: список смежностей
    '''
    v = int(input())
    ss = []
    k = v
    while k > 0:
        ss.append(list(map(int, input().split())))
        k -= 1
    return ss, v


def ms_is_dir_1(ms, v):
    '''
    :param ms: матрциа смежностей
    :param v: количество вершин
    :return: ориентированность графа
    '''
    for i in range(v):
        for j in range(v):
            if ms[i][j] != ms[j][i] or (i == j and ms[i][j] == 1):
                return False
    return True


def ms_is_loop_2(ms, v):
    '''
    :param ms: матрица смежностей
    :param v: количество вершин
    :return: наличие петель
    '''
    flag = False
    for i in range(v):
        if ms[i][i] == 1:
            flag = True
    return flag


def ms_count_edges_3(ms, v):
    '''
    :param ms: матрица смежностей
    :param v: количество вершин
    :return: количество ребер
    '''
    cnt = 0
    for i in range(v):
        for j in range(v):
            if ms[i][j] == 1:
                cnt += 1
    return int(cnt / 2)


def ms_dir_count_edges_4(ms, v):
    '''
    :param ms: матрица смежностей
    :param v: количество вершин
    :return: количество ребер
    '''
    cnt = 0
    for i in range(v):
        for j in range(v):
            if ms[i][j] == 1:
                cnt += 1
    return int(cnt)


def ms_to_sr_5(ms, v):
    '''
    :param ms: матрица смежностей
    :param v: количество вершин
    :return: список ребер
    '''
    edges_list = []
    for i in range(v):
        for j in range(i + 1, v):
            if ms[i][j] == 1:
                edges_list.append((i + 1, j + 1))
    return edges_list


def sr_to_ms_6(sr, v):
    '''
    :param sr: список ребер
    :param v: количество вершин
    :return: матрица смежностей
    '''
    e = len(sr)
    ms = [[0 for i in range(v)] for j in range(v)]
    for i in range(e):
        ms[sr[i][1] - 1][sr[i][0] - 1] = 1
        ms[sr[i][0] - 1][sr[i][1] - 1] = 1
    return ms


def ms_dir_to_sr_7(ms, v):
    '''
    :param ms: матрица смежностей
    :param v: количество вершин
    :return: список ребер
    '''
    sr = []
    for i in range(v):
        for j in range(v):
            if ms[i][j] == 1:
                sr.append([i + 1, j + 1])
    return sr


def sr_dir_to_ms_8(sr, v):
    '''
    :param sr: список смежностей
    :param v: количество вершин
    :return: матрица смежностей
    '''
    e = len(sr)
    ms = [[0 for i in range(v)] for j in range(v)]
    for i in range(e):
        ms[sr[i][0] - 1][sr[i][1] - 1] +=1
    #     95 пиздец важная строчка там вместо += может просто = стоять (раньше стояло)
    return ms


def ss_dir_reverse_9(ss, v):
    '''
    :param ss: список смежностей
    :param v: количество вершин
    :return: развернутый список смежностей
    '''
    ans = [[] for i in range(v)]
    for i in range(v):
        for j in range(len(ss[i])):
            ans[ss[i][j] - 1].append(i + 1)
    return ans


def sr_is_parallel_edges_10(sr, v):
    '''
    :param sr:
    :param v:
    :return: параллельность ребер графа
    '''
    e = len(sr)
    for i in range(e):
        for j in range(i + 1, e):
            if sr[i] == sr[j][::-1]:
                return True
    return False


def sr_dir_is_parallel_edges_11(sr, v):
    '''
    :param sr: список ребер
    :param v: количество вершин
    :return: паралелльность ребер орграфа
    '''
    e = len(sr)
    for i in range(e):
        for j in range(i + 1, e):
            if sr[i] == sr[j]:
                return True
    return False


def ms_powers_12(ms, v):
    '''
    :param ms: матрица смежности
    :param v: количество вершин
    :return: степени всех вершин неориентированного графа
    '''
    e = len(ms)
    powers = []
    for i in range(e):
        cnt = 0
        for j in range(e):
            if ms[i][j] == 1:
                cnt += 1
        powers.append(cnt)
    return powers


def sr_powers_13(sr, v):
    '''
    :param sr: список ребер
    :param v: количество вершин
    :return: степени вершин
    '''
    ms = sr_to_ms_6(sr, v)
    return ms_powers_12(ms, v)

def ms_dir_count_in_out_14(ms, v):
    '''
    :param ms: матрица смежности
    :param v: количество вершин
    :return: полустепени входа и выхода для каждой вершины
    '''
    ans = [[0, 0] for k in range(v)]
    for i in range(v):
        for j in range(v):
            if ms[i][j] == 1:
                ans[i][1] += 1
                ans[j][0] += 1
    return ans

def sr_dir_powers_15(sr, v):
    '''
    :param sr: список ребер
    :param v: количество вершин
    :return: степени орграфа
    '''
    ans = [[0, 0] for k in range(v)]
    ms = sr_dir_to_ms_8(sr, v)
    for i in range(v):
        out_cnt = 0
        in_cnt = 0
        for j in range(v):
            if ms[i][j]:
                out_cnt += 1
            if ms[j][i]:
                in_cnt += 1
        ans[i][1] = out_cnt
        ans[i][0] = in_cnt
    return ans


def ms_in_out_only_16(ms , v):
    '''
    :param ms: матрица смежности
    :param v: количество вершин
    :return: число, истоки, число стоки
    '''
    _in = []
    _out = []
    for i in range(v):
        in_flag = True
        out_flag = True
        for j in range(v):
            if ms[i][j] == 1:
                in_flag = False
            if ms[j][i] == 1:
                out_flag = False
        if in_flag:
            _in.append(i+1)
        if out_flag:
            _out.append(i+1)
    return (len(_out), _out), (len(_in), _in)

def sr_is_regular_17(sr, v):
    '''
    :param sr: список ребер графа (строки по 2 числа)
    :param v:  число вершын
    :return: регулярность неориентированного графа
    '''
    ms = sr_to_ms_6(sr, v)
    powers = ms_powers_12(ms, v)
    if len(set(powers)) == 1:
        return True
    else:
        return False

def sr_is_full_18(sr, v):
    '''
    :param sr: список ребер
    :param v: количество вершин
    :return: полнота неориентированного графа
    '''
    ms = sr_to_ms_6(sr, v)
    for i in range(v):
        cnt = 0
        for j in range(v):
            if ms[i][j] == 1:
                cnt += 1
        if cnt != v - 1:
            return False
    return True

def sr_dir_is_full_19(sr, v):
    '''
    :param sr: список ребер
    :param v: количество вершин
    :return: полуполнота ориентированного графа
    '''
    ms = sr_dir_to_ms_8(sr, v)
    for i in range(v):
        cnt = 0
        for j in range(v):
            if ms[i][j] >= 1 or ms[j][i] >= 1:
                cnt += (ms[i][j] + ms[j][i])
        if cnt == 0:
            return False
    return True

def sr_dir_is_tur_20(sr, v):
    '''
    :param sr: список ребер
    :param v: количество вершин
    :return: турнирность ориентированного графа
    '''
    ms = sr_dir_to_ms_8(sr, v)
    for i in range(v):
        cnt = 0
        for j in range(v):
            if ms[i][j] == 1 or ms[j][i] == 1:
                cnt += (ms[i][j] + ms[j][i])
        if cnt != v - 1:
            return False
    return True

def uncommon_1_number(a, b):
    '''
    :param a: два числа
    :param b: два числа
    :return: общее число этих пар, если оно одного - ничего в противном случае
    '''
    for i in [0, 1]:
        for j in [0, 1]:
            if a[i] == b[j]:
                return [a[i-1], b[j-1]]

def sr_is_trans_21(sr, v):
    '''
    :param sr: список ребер
    :param v: количество вершин
    :return: транзитивность неориентированного графа
    '''
    e = len(sr)
    for i in range(e):
        for j in range(i +1, e):
            pair = uncommon_1_number(sr[i], sr[j])
            if  pair not in sr and pair[::-1] not in sr:
                return False
    return True

def ms_dir_is_trans_22(ms, v):
    '''
    :param ms: матрица смежности
    :param v: количество вершин
    :return: тринзитивность оринтированного графа
    '''
    sr = ms_dir_to_sr_7(ms, v)
    e = len(sr)
    for i in range(e):
        for j in range(i + 1, e):
            pair = [sr[i][0], sr[j][1]]
            if pair not in sr and pair[::-1] not in sr:
                return False
    return True