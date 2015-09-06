__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import pickle
import math

# ---------------------------------------------------------------
# Class - Book
# ---------------------------------------------------------------


class Book:
    """Represents an "electronic book" - one can add pages, save/load to file and search for phrases"""
    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self):
        self._pages = []

        self.can_do_tfidf = False
        self._word2number_of_pages_having_it = None
        self._page2word_frequency = None
        self._page2max_word_frequency = None

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def add_page(self, page):
        """Adds a new page to the book"""
        self._pages.append(page)
        self.can_do_tfidf = False

    def make_pages_from_textfile(self, fname, lines_per_page=20):
        """Opens given text file, and makes pages out of it"""
        with open(fname, 'r') as f:
            lines = f.readlines()
            buffer = []
            for line in lines:
                buffer.append(line)
                if len(buffer) == lines_per_page:
                    self.add_page("\n".join(buffer))
                    buffer.clear()
            if len(buffer) != 0:
                self.add_page("\n".join(buffer))
        self.can_do_tfidf = False

    def search_for(self, text):
        """Searches for the text in all the pages, then sorts the results by TF.IDF importance of the search phrase
        in the page
        """
        # find pages containing the text
        found_pages = [i for i in range(len(self._pages)) if text in self._pages[i]]

        # split the search string to words
        words = [word for word in self.__split_to_words(text)]

        # get the importance-score for each found page
        pages_and_scores = []
        for i in found_pages:
            score = 0
            for word in words:
                score += self.__tf_idf(word, i)
            pages_and_scores.append((i, score))

        # sort by importance score
        pages_and_scores.sort(key=lambda x: x[1], reverse=True)

        print("Search phrase \"" + text + "\" located in following pages (sorted by importance): ")
        for pas in pages_and_scores:
            print("\tPage " + str(pas[0]) + " (importance = " + str(pas[1]) + ")")

    def save_to_file(self, fname):
        """Saves the book to a specified file"""
        with open(fname, 'wb') as f:
            pickle.dump(self._pages, f)

    def load_from_file(self, fname):
        """Loads the book from specified file"""
        with open(fname, 'rb') as f:
            self._pages = pickle.load(f)
        self.can_do_tfidf = False

    def print_page(self, page_number, width=120):
        """Prints the specified page of the book, to the console

        One may specify the maximum width of the page
        """
        print('-'*width)
        print("| Page " + str(page_number + 1))
        print('-'*width)
        line = ""
        for c in self._pages[page_number]:
            line += c
            if len(line) == width:
                print(line)
                line = ""
        print(line)
        print('-'*width)
        print()

    def print_all(self, width=120):
        """Prints all the pages of the book, one by one, to the console"""
        for i in range(len(self._pages)):
            self.print_page(i, width)

    def print_important_words(self, page_number, k=10):
        """Gets the top k important words for given page"""
        words_and_importances = []
        for word in self.__get_words_for_page(page_number):
            words_and_importances.append((word, self.__tf_idf(word, page_number)))

        words_and_importances.sort(key=lambda x: x[1], reverse=True)

        print("Most important words on page " + str(page_number + 1))
        for wai in words_and_importances[:k]:
            print("\t" + wai[0] + " (importance = " + str(wai[1]) + ")")

    # ---------------------------------------------------------------
    # Implementation
    # ---------------------------------------------------------------

    def __tf_idf(self, word, page_index):
        """Computes the TF.IDF for given word on given page"""
        if not self.can_do_tfidf:
            self.__compute_stats_for_tfidf()
        return self.__tf(word, page_index)*self.__idf(word)

    def __tf(self, word, page_index):
        """Computes the TF for given word"""
        if not self.can_do_tfidf:
            self.__compute_stats_for_tfidf()

        f = 0 if word not in self._page2word_frequency[page_index] else self._page2word_frequency[page_index][word]
        return f/self._page2max_word_frequency[page_index]

    def __idf(self, word):
        """Computes the IDF for given word"""
        if not self.can_do_tfidf:
            self.__compute_stats_for_tfidf()
        n_word = 0 if word not in self._word2number_of_pages_having_it else self._word2number_of_pages_having_it[word]
        return math.log(len(self._pages)/(1 + n_word))

    def __get_words_for_page(self, page_index):
        """Gets the set of words found in the given page"""
        if not self.can_do_tfidf:
            self.__compute_stats_for_tfidf()
        return self._page2word_frequency[page_index].keys()

    @staticmethod
    def __filter_to_letters(word):
        """Returns the word filtered to contain letters only"""
        filtered = ""
        for c in word:
            if not c.isalpha():
                continue
            filtered += c
        return filtered

    def __split_to_words(self, s):
        """Splits the string s to words (in a simplistic manner used in this class) and iterates through them"""
        for word in s.split(' '):
            # skip empty words
            word = self.__filter_to_letters(word)
            word = word.lower()
            if len(word.strip()) == 0:
                continue

            yield word

    def __compute_stats_for_tfidf(self):
        """Computes stats necessary for computation of TF.IDF"""
        # get the necessary stats on the words
        word2number_of_pages_having_it = {}  # e.g. 'word' -> '15'
        page2word_frequency = {}  # e.g. 47 -> ('word' -> 2)
        for i in range(len(self._pages)):
            page = self._pages[i]
            page2word_frequency[i] = {}

            for word in self.__split_to_words(page):
                # mark the occurence of the word for this page
                first_occurence = False
                if word not in page2word_frequency[i]:
                    page2word_frequency[i][word] = 0
                    first_occurence = True
                page2word_frequency[i][word] += 1

                # if this is the first time we see this word for this page, we also increase the # of pages having it
                if first_occurence:
                    if word not in word2number_of_pages_having_it:
                        word2number_of_pages_having_it[word] = 0
                    word2number_of_pages_having_it[word] += 1

        # get max-word frequency for each page
        page2max_word_frequency = {}  # e.g. 47 -> 17
        for i in page2word_frequency:
            page2max_word_frequency[i] = max(page2word_frequency[i].values())

        self._word2number_of_pages_having_it = word2number_of_pages_having_it
        self._page2word_frequency = page2word_frequency
        self._page2max_word_frequency = page2max_word_frequency
        self.can_do_tfidf = True

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    b = Book()
    b.make_pages_from_textfile('animal_farm.txt')
    b.print_page(0)
    b.print_important_words(0)
    b.search_for("pig")
    b.print_important_words(38)
    b.search_for("point of view")
    b.print_page(10)

if __name__ == '__main__':
    main()