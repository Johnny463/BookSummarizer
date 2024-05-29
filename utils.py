import re


def clean_text(text):
    # if new line if followed by - join the lines
    text = text.replace("-\n\n", "")
    # if new line if followed by - join the lines
    text = text.replace("-\n", "")
    # replace double new lines with a whitespace
    text = text.replace("\n\n", " ")
    # # remove new lines
    text = text.replace("\n", "")
    # clean for 'Crime and Punishment'
    text = text.replace("Crime and Punishment", "")
    # clean 'Download free eBooks of classic literature, books and novels at Planet eBook.' 
    text = text.replace("Download free eBooks of classic literature, books and novels at Planet eBook.", "")
    # clean Subscribe to our free eBooks blog and email newsletter.
    text = text.replace("Subscribe to our free eBooks blog and email newsletter.", "")
    # check if there is any number on the right of 'Free eBooks at Planet eBook.com' if so remove it
    text = re.sub(r'Free eBooks at Planet eBook.com\s+\d+', '', text)
    # clean Free eBooks at Planet eBook.com
    text = text.replace("Free eBooks at Planet eBook.com", "")
    # remove all characters like \x181
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
    # remove double or more spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()