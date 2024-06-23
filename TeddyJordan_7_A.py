import re

def extract_sentences(text):
    # define the regular expression pattern.
    pattern = r'[^.!?]*[0-9]*[^.!?]*[.!?]'

    # use re.findall to find all sentences matching the pattern
    sentences = re.findall(pattern, text)

    # filter out any empty strings from the results
    sentences = [s.strip() for s in sentences if s.strip()]

    return sentences

def main():
    # sample text with sentences
    text = "1. This is a test sentence. 2. 4 test, sentence! does it work? normal sentence."

    # extract sentences
    sentences = extract_sentences(text)

    # display each sentence and the count
    print("Extracted Sentences:")
    for sentence in sentences:
        print(sentence)

    print(f"\nTotal number of sentences: {len(sentences)}")

if __name__ == "__main__":
    main()