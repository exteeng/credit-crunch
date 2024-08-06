def utils_example():
    """A simple example of a utility function.

        :return: _description_
    """
    import json
    from pathlib import Path
    
    data_path = Path('data/example_data.json')

    if data_path.exists():
        with data_path.open() as transactions_file:
            all_transactions_total = json.load(transactions_file)


    return (len(all_transactions_total), all_transactions_total,)


