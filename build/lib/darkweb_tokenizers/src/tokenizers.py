from typing import List
from typing import Protocol

import os

from youtokentome import BPE
from youtokentome import OutputType


class Tokenizer(Protocol):
    def __call__(self, text: str) -> Tokens:
        pass

    def revert(self, tokens: Tokens) -> str:
        pass

    def tokens(self) -> List[str]:
        pass


class BPETokenizer:
    def __init__(self, model: str) -> None:
        self.model_path = model
        self.tokenize = BPE(model=model)

    def __call__(self, text: str) -> List[str]:
        tokens = self.tokenize.encode(
            sentences=[text],
            output_type=OutputType.SUBWORD,
        )[0]

        # We know it's a List of str because of OutputType.SUBWORD
        return tokens

    def revert(self, tokens: Tokens) -> str:
        ids = [self.tokenize.subword_to_id(token) for token in tokens]
        return self.tokenize.decode(ids)[0]

    def tokens(self) -> List[str]:
        return self.tokenize.vocab()

    @classmethod
    def load_from_disk(cls, directory_path: str) -> "BPETokenizer":
        return cls(model=os.path.join(directory_path, FILE_TEXT_TOKENIZER))