from email.policy import default
import os
import click
from darkweb_tokenizers.src.tokenizers import BPETokenizer
from darkweb_tokenizers.utils.parameters import FILE_TEXT_PATH
from darkweb_tokenizers.utils.parameters import FILE_TEXT_TOKENIZER


@click.command()
@click.option("-mp", "--model_path", nargs=1, default=os.path.join(FILE_TEXT_PATH, FILE_TEXT_TOKENIZER), type=str)
def cli(
    model_path: str,
) -> None:
    model = BPETokenizer(model=model_path)
    print('First 100 tokens : ')
    print(model.tokens()[:100])


if __name__ == "__main__":
    cli()