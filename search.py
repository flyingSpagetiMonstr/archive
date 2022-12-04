from math import inf


def zero(*args): return 0
def f(x, end, h): return g(x)+h(x, end)


def g(x: object):
    ptr = x
    count = 0
    while ptr != None:
        ptr = ptr.parent
        count += 1
    return count


def A_star(start: object, end: object, h=zero, G=None, f=f, cost: list = None) -> list[object]:

    # cost=============
    if cost != None:
        cost.append(0)

    open_list = [start]
    close_list = [start]

    para = (G,) if G else ()

    while open_list:
        min_cost = inf
        index = -1
        for i in range(len(open_list)):
            estimate = f(open_list[i], end, h)
            if estimate < min_cost:
                min_cost = estimate
                index = i
        to_extend = open_list[index]

        for next in to_extend.adjacencies(*para):
            if next in close_list:
                continue
            close_list.append(next)

            # cost=============
            if cost != None:
                cost[-1] += 1

            if next == end:
                ptr = next
                solution = []
                while ptr != None:
                    solution.insert(0, ptr)
                    ptr = ptr.parent
                return solution

            try:
                i = open_list.index(next)
            except ValueError:
                open_list.append(next)
            else:
                if g(open_list[i]) > g(next):
                    open_list.pop(i)
                    open_list.append(next)

        open_list.pop(index)
    return "Failed"


def BFS__based_on_A_star(start, end, G=None):
    return A_star(start, end, zero, G)


def DFS__based_on_A_star(start, end, G=None):
    return A_star(start, end, G=G, f=lambda x, end, h: -g(x))
