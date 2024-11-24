def make_parsing_table(
    terminals: set[str],
    non_terminals: set[str],
    rule_set: dict[str, set[str]],
    first: dict[str, set[str]],
    follow: dict[str, set[str]],
    epsilon_symbol: str,
) -> dict[tuple[str, str], dict[str, str]]:
    parsing_table = {}
    for non_term in non_terminals:
        for term in terminals:
            parsing_table[(non_term, term)] = None

    for non_term in non_terminals:
        for expand_str in rule_set[non_term]:
            rule_to_add = {non_term: expand_str}
            term_pool = first[expand_str[0]]

            if epsilon_symbol in term_pool:
                term_pool.remove(epsilon_symbol)
                term_pool = term_pool | follow[non_term]

            for term in term_pool:
                if parsing_table[(non_term, term)] is None:
                    parsing_table[(non_term, term)] = rule_to_add
                else:
                    raise ValueError(
                        f"Conflicting rules for {non_term} and\
                        {term}:{parsing_table[(term, non_term)]}\
                        and {rule_to_add}"
                    )

    return parsing_table