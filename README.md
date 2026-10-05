# Text Analyzer & Next-Word Predictor

A Python command-line tool that analyzes text and predicts the next word.

## Features
- Two input modes: type text directly or load it from a file path
- Text preprocessing: lowercasing and punctuation removal
- Statistics dashboard: total words, unique words, and more
- Next-word prediction based on the analyzed text

## Requirements
- Python 3.8+
- Uses only the standard library (`os`, `string`)

## How to Run
```bash
python smart_analyzer.py
```
1. Choose `1` to enter text directly (type `$$END_TEXT$$` on a new line to finish) or `2` to enter a file path.
2. The tool preprocesses the text and shows the dashboard.

## Project Structure
- `smart_analyzer.py`: main script (input, preprocessing, dashboard, prediction)

## Author
um240712-code
