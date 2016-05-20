import math
from list_sorter import *

class OddListSorter(ListSorter):

    def sort(self, stupid_list):
        stupid_list = sorted(stupid_list)
        original_list = stupid_list[:]

        if(self.duplicates_at_beginning_are_half_plus_one(stupid_list)):
            extra_element = stupid_list.pop(0)
        else:
            extra_element = stupid_list.pop()

        result = self.sort_list_with_even_amount_of_elements(stupid_list)

        if(self.duplicates_at_beginning_are_half_plus_one(original_list)):
            self.add_at_end(result, extra_element)
        else:
            self.add_at_beginning(result, extra_element)

        return result

    def max_duplicate_elements_for(self, list):
        return len(list) / 2 + 1

    def duplicates_at_beginning_are_half_plus_one(self, list):
        return list.count(list[0]) == len(list) / 2 + 1

    def last_element_of(self, list):
        return list[-1]

    def add_at_end(self, list, element):
        list.append(element)

    def add_at_beginning(self, list, element):
        list.insert(0, element)
