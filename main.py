class WordLengthIterator:
    def __init__(self, sentence):
        self.words = sentence.split()  
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):  
            raise StopIteration

        word_length = len(self.words[self.index])
        self.index += 1
        return word_length

sentence = "Hello, how are you doing today?"
word_length_iterator = WordLengthIterator(sentence)

for word_length in word_length_iterator:
    print(word_length)
