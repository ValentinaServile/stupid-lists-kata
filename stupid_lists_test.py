import unittest
from stupid_lists import *

class StupidListsTest(unittest.TestCase):

    sut = StupidLists()

    def test_cannot_sort_empty_list(self):
        self.assertRaises(StupidListNotSortableException, self.sut.sort, [])

    def test_cannot_sort_list_of_one(self):
        self.assertRaises(StupidListNotSortableException, self.sut.sort, [1])

    def test_cannot_sort_list_of_two(self):
        self.assertRaises(StupidListNotSortableException, self.sut.sort, [1,2])


    def test_sorts_list_with_even_amount_of_elements_alternating_less_and_greater_signs_between_elements(self):
        self.assertEquals([1, 3, 2, 4], self.sut.sort([1, 3, 2, 4]))

    def test_sorts_list_with_odd_amount_of_elements_alternating_less_and_greater_signs_between_elements(self):
        self.assertEquals([5, 1, 3, 2, 4], self.sut.sort([1, 2, 3, 4, 5]))

    def test_can_also_sort_list_when_elements_are_in_randomized_order(self):
        self.assertEquals([1, 3, 2, 4], self.sut.sort([4, 1, 2, 3]))


    def test_can_sort_list_with_even_amount_of_elements_that_has_up_to_fifty_percent_duplicate_elements_with_minimum_value(self):
        self.assertEquals([1, 2, 1, 3, 1, 4, 1, 5], self.sut.sort([1, 1, 1, 1, 2, 3, 4, 5]))

    def test_can_sort_list_with_even_amount_of_elements_that_has_up_to_fifty_percent_duplicate_elements_with_maximum_value(self):
        self.assertEquals([1, 5, 2, 5, 3, 5, 4, 5], self.sut.sort([1, 2, 3, 4, 5, 5, 5, 5]))

    def test_cannot_sort_list_with_even_amount_of_elements_that_has_more_than_fifty_percent_duplicate_elements(self):
        self.assertRaises(StupidListNotSortableException, self.sut.sort, [1, 1, 1, 1, 1, 1, 2, 3, 4, 5])


    def test_can_sort_list_with_odd_amount_of_elements_that_has_up_to_fifty_percent_plus_one_duplicate_elements_with_minimum_value(self):
        self.assertEquals([1, 2, 1, 3, 1, 4, 1, 5, 1], self.sut.sort([1, 1, 1, 1, 1, 2, 3, 4, 5]))

    def test_can_sort_list_with_odd_amount_of_elements_that_has_up_to_fifty_percent_plus_one_duplicate_elements_with_maximum_value(self):
        self.assertEquals( [5, 1, 5, 2, 5, 3, 5, 4, 5], self.sut.sort([1, 2, 3, 4, 5, 5, 5, 5, 5]))

    def test_cannot_sort_list_with_odd_amount_of_elements_that_has_more_than_fifty_percent_plus_one_duplicate_elements(self):
        self.assertRaises(StupidListNotSortableException, self.sut.sort, [1, 1, 1, 1, 1, 1, 2, 3, 4])


    def test_can_sort_list_with_even_amount_of_elements_consisting_of_only_two_values_repeating_themeselves(self):
        self.assertEquals([1, 2, 1, 2, 1, 2], self.sut.sort([1, 1, 1, 2, 2, 2]))

    def test_can_sort_list_with_odd_amount_of_elements_consisting_of_only_two_values_repeating_themeselves(self):
        self.assertEquals([1, 2, 1, 2, 1, 2, 1], self.sut.sort([1, 1, 1, 1, 2, 2, 2]))


    def test_can_sort_list_with_even_amount_of_elements_and_50_percent_of_duplicates_in_the_middle(self):
        self.assertEquals([1,2,3,2], self.sut.sort([1,2,2,3]))

if __name__ == '__main__':
	unittest.main()
