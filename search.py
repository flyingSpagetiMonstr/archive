# A-star algorithm, and BFS&DFS that are based on it.
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
    # requirements for the object:
    #   methods:
    #       1, __eq__()
    #       2, adjacencies()    [return adjacent nodes, and their parent nodes should be given]
    #   attributes:
    #       1, self.parent      [defaultly None]

    # cost=============
    if cost != None:
        cost.append(0)

    open_list = [start]
    close_list = [start]

    para = (G,) if G else ()

    while open_list:

        # sort out the node with a min f(x) in open list
        min_cost = inf
        to_extend = None
        for tmp in open_list:
            estimate = f(tmp, end, h)
            if estimate < min_cost:
                min_cost = estimate
                to_extend = tmp

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

        open_list.remove(to_extend)
    return "Failed"


def BFS_based_on_A_star(start, end, G=None, cost=None):
    return A_star(start, end, zero, G, cost=cost)


def DFS_based_on_A_star(start, end, G=None, cost=None):
    return A_star(start, end, G=G, f=lambda x, end, h: -g(x), cost=cost)
