from odd_list_sorter import *
from even_list_sorter import *

class ListSorterFactory():

    @staticmethod
    def sorter_for(list):
        if(ListSorterFactory.even_amount_of_elements_in(list)):
            return EvenListSorter()
        else:
            return OddListSorter()

    @staticmethod
    def even_amount_of_elements_in(list):
        return len(list) % 2 == 0
