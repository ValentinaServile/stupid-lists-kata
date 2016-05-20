from list_sorter_factory import *

class StupidLists():

    LIST_NOT_SORTABLE_ERROR_MESSAGE = "Stupid list not sortable you dumb ass."

    def sort(self, stupid_list):
        sorter = ListSorterFactory.sorter_for(stupid_list)
        if(not sorter.can_sort(stupid_list)):
            raise StupidListNotSortableException(self.LIST_NOT_SORTABLE_ERROR_MESSAGE)
        else:
            return sorter.sort(stupid_list)

class StupidListNotSortableException(Exception):
    pass
