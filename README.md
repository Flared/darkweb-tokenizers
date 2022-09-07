# darkweb-tokenizers
Byte-Pair-Encoding of the tokenizers and lexical from darweb doc


## Installation

```bash
pip install youtokentome
```
## Python interface 

### Example
Let's start with a self-contained example. 

```python
import random

```

 

&nbsp;

vocab_size-1]. Id of subword or,
 if there is no such subword in the vocabulary, `unk_id` will be 
returned.

&nbsp;
#### id_to_subword 

```python
id_to_subword(self, id)
```
**Args:**
* `id`: int, must be in the range [0, vocab_size-1]

**Returns:** string. Subword from vocabulary by id.
  
&nbsp;
#### decode 
```python
decode(self, ids, ignore_ids=None)
```  
Convert each id to subword and concatenate with space symbol.

**Args:**

  * `ids`: list of lists of integers. All integers must be in the range [0, vocab_size-1]
  * `ignore_ids`: collection of integers. These indices would be ignored during the decoding. All integers must be in the range [0, vocab_size-1] [default: None]

  
**Returns:** List of strings.  
 
## Command line interface

### Example 

```bash
$ yttm bpe --data TRAINING_DATA_FILE --model OUTPUT_MODEL_FILE --vocab_size 2000
$ yttm encode --model OUTPUT_MODEL_FILE --output_type subword < TEST_DATA_FILE > ENCODED_DATA 
```


### Supported commands

`YouTokenToMe` supports the following commands:

```
$ yttm --help

Usage: yttm [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  bpe     Train BPE model.
  decode  Decode ids to text.
  encode  Encode text to ids or subwords.
  vocab   Print list of learned subwords.
```