# A toy acronym tool for pre-module assignment of AIPI510 Fall 2024

This toy tool can read a text file and convert each line of text to acronym and then write those acronym line by line to other text file.


## install dependencies

using a virtual environment is suggested.

```bash
pip install -r requirements.txt
```

## How to use it?

for example, if we want convert each line in the `test_main/text_file_for_demo.txt` to acronym and write it to `result_file_for_demo.txt`, we can use the tool like this:

```bash
python ./acronym.py test_cases/input_file_for_test.txt result_file_for_demo.txt
```

## How to test the code?

```bash
pytest
```