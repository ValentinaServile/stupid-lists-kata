import math

class ListSorter():

    def sort_list_with_even_amount_of_elements(self, list):
        list = sorted(list)
        first_half, second_half = self.split_in_two(list)
        result = self.zip(first_half, second_half)
        return result

    def can_sort(self, list):
        return self.is_lenght_sufficient_for_sorting(list) and self.less_than_max_duplicate_elements_in(list)

    def is_lenght_sufficient_for_sorting(self, list):
        return len(list) > 2

    def less_than_max_duplicate_elements_in(self, list):
        return list.count(self.most_common_element_in(list)) <= self.max_duplicate_elements_for(list)

    def most_common_element_in(self, list):
        return max(set(list), key=list.count)

    def split_in_two(self, list):
        slice_point = int(math.floor(len(list) / 2))
        first_half = list[0 : slice_point]
        second_half = list[slice_point : len(list)]
        return [first_half, second_half]

    def zip(self, first_list, second_list):
        list_zipped_as_touples = zip(first_list, second_list)
        list_zipped_as_lists = [list(item) for item in list_zipped_as_touples]
        return self.flatten(list_zipped_as_lists)

    def flatten(self, nested_list):
        return sum(nested_list, [])
