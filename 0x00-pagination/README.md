# Pagination

> This project was an introduction to Pagination.

## Summary

I learnt about how to paginate a dataset with simple page and page_size parameters, how to paginate a dataset with hypermedia metadata, and how to paginate in a deletion-resilient manner.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-simple_helper_function.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x00-pagination/0-simple_helper_function.py): A function named `index_range` that takes two integer arguments `page` and `page_size`.
- [ ] [1-simple_pagination.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x00-pagination/1-simple_pagination.py): A method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.
    - First, copy `index_range` from the previous task and add to the code below:
```py
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass
```
- [ ] [2-hypermedia_pagination.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x00-pagination/2-hypermedia_pagination.py): A `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:
    - `page_size`: the length of the returned dataset page
    - `page`: the current page number
    - `data`: the dataset page (equivalent to return from previous task)
    - `next_page`: number of the next page, `None` if no next page
    - `prev_page`: number of the previous page, `None` if no previous page
    - `total_pages`: the total number of pages in the dataset as an integer
- [ ] [3-hypermedia_del_pagination.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x00-pagination/3-hypermedia_del_pagination.py): A `get_hyper_index` method with two integer arguments: `index` with a `None` default value and `page_size` with default value of 10.

> [test_files](): A folder of test files. Provided by Alx.
