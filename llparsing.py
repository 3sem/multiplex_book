def ll1_algorithm(
    input_string: str,
    parsing_table: dict[tuple[str, str], dict[str, str]],
    starting_symbol: str,
    end_symbol: str,
    epsilon_symbol: str,
):
    taken_len = 0
    stack = []
    stack.append(end_symbol)
    stack.append(starting_symbol)

    non_term_term_pairs = parsing_table.keys()
    non_terminals = {pair[0] for pair in non_term_term_pairs}
    terminals = {pair[1] for pair in non_term_term_pairs}

    current = input_string[taken_len]
    taken_len += 1

    while stack[-1] != end_symbol:
        stack_top = stack[-1]
        if stack_top == epsilon_symbol:
            stack.pop()
            continue
        if stack_top == current:
            stack.pop()
            current = input_string[taken_len]
            taken_len += 1
        elif stack_top in non_terminals:
            corresponding_rule = parsing_table[stack_top, current]
            if corresponding_rule is None:
                raise LookupError(
                    f"parsing table empty with non_term\
                    {stack_top} and term {current}, which is\
                    {taken_len} symbol from {input_string}"
                )
            stack.pop()
            stack.extend(corresponding_rule[stack_top][::-1])
        else:
            raise LookupError(
                f"terminal {current} #{taken_len} from\
                input {input_string} is not equal to\
                terminal{stack_top} from stack while parsing"
            )

    if current != end_symbol:
        raise LookupError(
            f"parsing of input {input_string} with\
            len{len(input_string)}
            ended on {taken_len} symbol"
        )