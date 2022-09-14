# darkweb-tokenizers

Flare research team is releasing the first tokenizer adapted to DarkWeb contents. This tokenizer is suit to NLP taks applied on content coming from illicit sources, like Dark Web forums, markets, and chatters between malicous actors. The tokenizer is available is five versions: 5,000' 10,000; 25,000; 50,000 and 100,000 tokens. 

Behind the scene, the dark web-tokenizers had been trained on years of content of illicit souces from the Flare's databse using bype-pair encoding. 

Feel free to try the [Flare's auto-extractor](https://auto-extractor.flare.systems/), which is able to extract the titles, publications date and authors of a variery of illicit forums, without the need of human assistance (Xpath or CSSSelector). Behind the scene, the DarkWeb tokenizer is in action, combined with a sequence labliing model and algorithms. See the [assiciated research](https://espace.etsmtl.ca/id/eprint/2993/).

## Installation

```bash
git clone https://github.com/Flared/darkweb-tokenizers.git
cd darkweb-tokenizers
python -m venv env
source env/bin/activate
pip install Cython # Mandatory
python -m venv env
source env/bin/activate
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