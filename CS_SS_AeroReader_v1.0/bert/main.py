import time

from bert_search import BertSearch


def main():
    clusters = [["angle", "hat", "body"], ["chair", "death", "life"]]
    init_start = time.perf_counter()
    bert = BertSearch(max_seq=200)
    init_end = time.perf_counter()
    init_total = init_end - init_start
    print(f"BERT init time: {init_total}\n")

    search_start = time.perf_counter()
    result = bert.search("fish", clusters)
    search_end = time.perf_counter()
    search_total = search_end - search_start
    print(result)
    print(f"Search time: {search_total}\n")

    # search_start = time.perf_counter()
    # result = bert.search("clothes", clusters)
    # search_end = time.perf_counter()
    # search_total = search_end - search_start
    # print(result)
    # print(len(result))
    # print(f"Search time: {search_total}\n")
    #
    # search_start = time.perf_counter()
    # result = bert.search("fish", clusters)
    # search_end = time.perf_counter()
    # search_total = search_end - search_start
    # print(result)
    # print(f"Search time: {search_total}\n")

    return 0


if __name__ == "__main__":
    main()
