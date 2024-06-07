# Analyzing Redundancy in English Language

This is a research project source code repository for analyzing redundancy in English language. The project is based on the paper "[Exploiting Redundancy in English Language for Hiding Secret Data in Innocent News Articles](https://ieeexplore.ieee.org/document/10180519)". The project analyze new data set which were scrapped from famous news-articles websites `results/scrapped` and a pre-collected datasets `results/datasets` (all the links at `results/datasets/data set links`).

## Installation
To install the project, you need to have Python 3.6 or higher installed on your system. You can install the project by running the following command:
```bash
git clone https://github.com/kashorafof/Analyzing-Redundancy-in-English-Language.git
cd Analyzing-Redundancy-in-English-Language
pip install -r requirements.txt
```
or by running the following jupyter notebook:
```python
package installer.ipynb
```

## Usage
The project use Spacy NLP library to analyze the redundancy in English language and calculate the redudancy of the following grammer rules / 100 words:
- Coordinating Conjunctions
- Phrasal Verbs
- Abbreviations
- Subordinating Conjunctions
- Noun and its identifier

The project provide the necessary functions to calculate the redundancy of the above mentioned grammer rules which can be found in the `code/text_processing.py` file.

The project also provide the necessary functions to analyze the text and calculate the redundancy of the above mentioned grammer rules in the given text. The functions can be found in the `code/functions.py` file.

## Example
The following code will calculate the redundancy of the Coordinating Conjunctions in the given text.
```python
import text_proccessing
import functions
texts = ["This is a sample text", "This is another sample text"]
doc = functions.analyze_txts(texts)
redundancy = text_proccessing.CoordinaryConjunction(text)
print(redundancy)
```
The above code will calculate the redundancy of the Coordinating Conjunctions in the given text.

## Results 
The results can be found in the `graphs` as a bar graph and in the `results` as a csv file.




