# darkweb-tokenizers

Flare research team is releasing the first tokenizer adapted to DarkWeb contents. This tokenizer is suited to NLP tasks applied on content coming from illicit sources, like Dark Web forums, markets, and chatters between malicious actors. The tokenizer is available is five versions: 5,000; 10,000; 25,000; 50,000, and 100,000 tokens. 

Behind the scenes, the dark web-tokenizers have been trained on years of content of illicit sources from Flare's database using bype-pair encoding. 

Feel free to try [Flare's auto-extractor](https://auto-extractor.flare.systems/), which is able to extract the titles, publications date and authors of a variety of illicit forums, without the need of human assistance (Xpath or CSSSelector). Behind the scenes, the DarkWeb tokenizer is in action, combined with a sequence labeling model and algorithms. See the [associated research](https://espace.etsmtl.ca/id/eprint/2993/).
## Installation

```bash
git clone https://github.com/Flared/darkweb-tokenizers.git
cd darkweb-tokenizers
python -m venv env
source env/bin/activate
pip install Cython # Mandatory
pip install .
```

### Help

```
python main.py --help 
```

### Exemples

```
python main.py -vs 100000 --text="CREDIT CARD/CVV +7,000 $ + PREMIUM CARDING "
>> ['▁CREDIT', '▁CARD', '/CVV', '▁+7', ',000', '▁$', '▁+', '▁PREMIUM', '▁CARDING']
```