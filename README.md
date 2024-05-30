# PDF to Summarized PDF Converter

This Python program allows you to convert a regular PDF document into a summarized PDF using language processing techniques. It leverages the [LangChain](https://python.langchain.com/docs/use_cases/summarization) library and [PyPDF2](https://pypi.org/project/PyPDF2) for text extraction and manipulation. With this tool, you can condense lengthy PDFs into shorter, more digestible versions.


## Prerequisites

Before you can use this program,you have the appropriate Python version specified in the `runtime.txt` file. Make sure you have the required dependencies installed. You can find them listed in the `requirements.txt` file. To install them, run:
```bash
pip install -r requirements.txt
```
Make sure to add environment of 'OPEN_API_KEY' with your actual OpenAI API key.OR you can this in code:
```bash
import os
os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'
```
This approach allows you to securely store and use your API key without hardcoding it directly into your code. It's a best practice for managing sensitive information like API keys.

and don't forget to replace placeholders like `"your_pdf.pdf"` with actual file paths or relevant information.




## Usage
Place the PDF file you want to summarize in the same directory as app.py.

Modify the app.py file if necessary to customize the summarization process according to your preferences.

Run the app.py script:

```bash
python app.py
```
The program will extract text from the PDF, generate a summary, and create a new summarized PDF in the same directory.



## License
```
MIT License

Copyright (c) 2024 Muhammad Junaid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```



