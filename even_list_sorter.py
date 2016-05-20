from list_sorter import *

class EvenListSorter(ListSorter):

    def sort(self, list):
        return self.sort_list_with_even_amount_of_elements(list)

    def max_duplicate_elements_for(self, list):
        return len(list) / 2
