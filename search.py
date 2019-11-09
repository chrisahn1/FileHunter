import os
from datetime import datetime
from os import walk

import pickle
import main

class FileHunter:
    def __init__(self):
        # a list that store the directory index
        self.file_index = []
        # store the results of each search
        self.results = []
        # record the count of matched file
        self.matches = 0
        # record the number of file that has been searched
        self.records = 0

    def create_new_index(self, root_path):
        """creat a new index and save to file"""
        self.file_index = [(root, files) for root, dirs, files in walk(root_path) if files]

        # save to file
        with open('file_index.pkl', 'wb') as f:
            pickle.dump(self.file_index, f)

    def load_existing_index(self):
        """load existing index"""
        try:
            with open('file_index.pkl', 'rb') as f:
                self.file_index = pickle.load(f)
        except:
            self.file_index = []

    def search(self, term, search_type = 'endswith'):
        """search for term based on the search type"""
        # reset variables
        self.results.clear()
        self.matches = 0
        self.records = 0

        # perform search
        for path, files in self.file_index:
            for file in files:
                self.records += 1
                if (search_type == 'contains' and term.lower() in file.lower() or
                    search_type == 'startswith' and file.lower().startswith(term.lower()) or
                    search_type == 'endswith' and file.lower().endswith(term.lower())):

                    result = path.replace('\\', '/') + '/' + file
                    self.results.append(result)
                    self.matches += 1
                else:
                    continue

        # save the results
        with open('search_results.txt', 'w') as f:
            for row in self.results:
                f.write(row + '\n')

def test1(words):
    t1 = datetime.now()
    s = FileHunter()
    s.create_new_index('C:/')
    #s.search('.txt')
    s.search(words)

    print()
    print(">> There were {:,d} matches out of {:,d} records searched.".format(s.matches, s.records))
    print()
    print(">> This query produced the following matches: \n")
    # for match in s.results:
    #     print(match)

    t2 = datetime.now()

    print(t2-t1)

    return s.results
