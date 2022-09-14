import os
import click
from darkweb_tokenizers.src.tokenizers import BPETokenizer
from darkweb_tokenizers.utils.parameters import FILE_TEXT_PATH


@click.command()
@click.option("-vs", "--vocabulary_size", nargs=1, type=int, default=5000, help="5000, 10000, 25000, 50000 or 100000", required=True)
@click.option("-t", "--text", nargs=1, type=str, required=True)
def cli(
    vocabulary_size: str,
    text: str
) -> None:
    model_path = os.path.join(FILE_TEXT_PATH, f"{vocabulary_size}.model")
    model = BPETokenizer(model=model_path)
    print(model(text))


if __name__ == "__main__":
    cli()
