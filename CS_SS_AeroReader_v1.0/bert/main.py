import time

from bert.bert_search import BertSearch


def main():
    init_start = time.perf_counter()
    bert = BertSearch(max_seq=100)
    init_end = time.perf_counter()
    init_total = init_end - init_start
    print(f"BERT init time: {init_total}\n")

    search_start = time.perf_counter()
    result = bert.search("fish")
    search_end = time.perf_counter()
    search_total = search_end - search_start
    print(result)
    print(f"Search time: {search_total}\n")

    search_start = time.perf_counter()
    result = bert.search("clothes")
    search_end = time.perf_counter()
    search_total = search_end - search_start
    print(result)
    print(len(result))
    print(f"Search time: {search_total}\n")

    search_start = time.perf_counter()
    result = bert.search("fish")
    search_end = time.perf_counter()
    search_total = search_end - search_start
    print(result)
    print(f"Search time: {search_total}\n")

    return 0


if __name__ == "__main__":
    main()
