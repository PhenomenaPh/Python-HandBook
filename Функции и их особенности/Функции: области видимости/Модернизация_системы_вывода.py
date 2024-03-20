def modern_print(sentence: str, input_values: list = []) -> str:

    if sentence not in input_values:
        print(sentence)
        input_values.append(sentence)
