from typing import List

class MettaLexerError(Exception):
    def __init__(self, error_message: str):
        super().__init__(error_message)

class MettaSyntaxError(Exception):
    def __init__(self, error_message: str):
        super().__init__(error_message)

class UndefinedSymbolError(Exception):
    def __init__(self, symbols: List[str]):
        super().__init__(str(symbols))
        self.missing_symbols = [symbol for symbol in symbols]

class UnknownSymbolOrdering(Exception):
    def __init__(self, symbols: str):
        super().__init__(str(symbol))
        self.symbol = symbol
