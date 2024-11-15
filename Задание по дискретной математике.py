from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)


def dfs1(v, g, used, order):
    used[v] = True
    for to in g[v]:
        if not used[to]:
            dfs1(to, g, used, order)
    order.append(v)


def dfs2(v, gt, comp, cl):
    comp[v] = cl
    for to in gt[v]:
        if comp[to] == -1:
            dfs2(to, gt, comp, cl)


def main():
    n = int(input())
    clauses = []
    for _ in range(n):
        line = list(map(int, input().split()))
        clauses.append(tuple(line))

    num_vars = max(abs(x) for clause in clauses for x in clause)
    g = defaultdict(list)
    gt = defaultdict(list)

    for clause in clauses:
        if len(clause) == 1:
            x = clause[0]
            g[-x].append(x)
            gt[x].append(-x)
        elif len(clause) == 2:
            x, y = clause
            g[-x].append(y)
            g[-y].append(x)
            gt[y].append(-x)
            gt[x].append(-y)

    used = [False] * (2 * num_vars + 1)
    order = []
    for i in range(-num_vars, num_vars + 1):
        if i != 0 and not used[i]:
            dfs1(i, g, used, order)

    comp = [-1] * (2 * num_vars + 1)
    j = 0
    while order:
        v = order.pop()
        if comp[v] == -1:
            dfs2(v, gt, comp, j)
            j += 1

    for i in range(1, num_vars + 1):
        if comp[i] == comp[-i]:
            print("Impossible")
            return

    print("Possible")


if __name__ == "__main__":
    main()
