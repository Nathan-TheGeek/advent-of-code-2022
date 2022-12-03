from pathlib import Path


class InputFile:
    def __init__(self, input_file):
        self.file = Path(input_file)

    def get_contents_by_line(self):
        return self.file.read_text().split("\n")