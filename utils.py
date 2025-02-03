from typing import List


def read_input(file_name: str) -> List[str] :
    with open(f"input_files/{file_name}.txt", "r") as file:
        text = file.read()
        lines = text.split("\n")
    return lines