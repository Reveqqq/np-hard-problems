def get_reverse(literal):
    """Returns the negated version of the literal."""
    return -literal


def is_satisfiable(clauses):
    """Determines if the given clauses are satisfiable."""
    my_sets = []

    first_clause = clauses[0]
    for c in first_clause:
        this = set()
        this.add(c)
        my_sets.append(this)

    for current_clause in clauses[1:]:
        temp_sets = []
        for s in my_sets:
            for literal in current_clause:
                if get_reverse(literal) not in s:
                    new_set = s.copy()
                    new_set.add(literal)
                    temp_sets.append(new_set)
        my_sets = temp_sets

    if my_sets:
        print("Possible")
    else:
        print("Impossible")


def main():
    m = int(input())
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        clauses.append(clause)

    is_satisfiable(clauses)


if __name__ == "__main__":
    main()
