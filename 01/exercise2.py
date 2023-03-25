from typing import List, Union, TextIO, Optional


def reader(file_name: Union[str, TextIO], word_list: List[str]) -> Optional[str]:
    with open(file_name, encoding="utf-8") if isinstance(
        file_name, str
    ) else file_name as file:
        for row in file:
            for word in word_list:
                if word.lower() in row.lower().split():
                    yield row
                    break
