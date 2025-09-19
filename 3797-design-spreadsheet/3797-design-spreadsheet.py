class Spreadsheet:
    def __init__(self, rows: int):
        # rows is given but we may or may not need to use it explicitly
        self.d = {}  # dictionary to store only set cells

    def setCell(self, cell: str, value: int) -> None:
        self.d[cell] = value

    def resetCell(self, cell: str) -> None:
        # either remove or set to 0
        # removing is better to save memory
        if cell in self.d:
            del self.d[cell]

    def getValue(self, formula: str) -> int:
        # formula has format "=X+Y"
        assert formula.startswith("=")
        expr = formula[1:]
        a, b = expr.split("+")
        total = 0

        for part in (a, b):
            part = part.strip()
            if part == "":
                continue
            if part[0].isdigit():
                total += int(part)
            else:
                total += self.d.get(part, 0)
        return total
