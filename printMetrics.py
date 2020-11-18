from utils import getMetrics

search_total, sols_total, no_sols, cost, exec_time = getMetrics()

print("Total lines searched: {}".format(search_total))
print("Total solution lines: {}".format(sols_total))
print("Total no solutions: {}".format(no_sols))
print("Total cost: {}".format(cost))
print("Total execution time: {}".format(exec_time))
print("\nNote: puzzles with no solution are not included in the metrics")