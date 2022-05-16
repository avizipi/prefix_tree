import json
import random
import string
from prefix_tree import PrefixTree, PrefixTree2
import time
from inspect import currentframe, getframeinfo


english_word_path = "words_dictionary.json"
with open(english_word_path) as f:
    english_words = json.load(f)


def random_string(n : int) -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(n))


def random_english_word() -> str:
    return random.choice(list(english_words.keys()))


def basic_test():
    '''
    >>> basic_test()
    {
        "a": {
            "b": {
                "c": {
                    "__end_of_word__": null
                }
            }
        }
    }
    {
        "a": {
            "b": {
                "c": {
                    "__end_of_word__": null
                }
            }
        },
        "b": {
            "a": {
                "r": {
                    "__end_of_word__": null,
                    "z": {
                        "__end_of_word__": null
                    }
                },
                "z": {
                    "__end_of_word__": null
                }
            }
        }
    }
    4
    True
    False
    True
    {
        "a": {
            "b": {
                "c": {
                    "__end_of_word__": null
                }
            },
            "s": {
                "s": {
                    "a": {
                        "f": {
                            "__end_of_word__": null
                        }
                    }
                }
            }
        },
        "b": {
            "a": {
                "r": {
                    "__end_of_word__": null,
                    "z": {
                        "__end_of_word__": null
                    }
                },
                "z": {
                    "__end_of_word__": null
                }
            }
        }
    }
    5
    '''
    pt = PrefixTree()
    pt.insert('abc')
    print(pt)
    pt.insert('bar')
    pt.insert('baz')
    pt.insert('barz')
    print(pt)
    print(len(pt))
    print(pt.contains('baz'))
    print(pt.contains('assaf'))
    pt.insert("assaf")
    print(pt.contains('assaf'))
    print(pt)
    print(len(pt))


def testing_times_of_inserting_random_strings(N=10000, number_of_chars=15):
    pt = PrefixTree()
    cnt = 0
    average_time = 0.0
    for _ in range(N):
        random_str = random_string(number_of_chars)
        start_time = time.perf_counter()
        res = pt.insert(random_str)
        end_time = time.perf_counter()
        average_time = average_time + end_time - start_time
        cnt = cnt + res
    average_time = average_time / N
    if cnt != pt.num_of_words:
        frame_info = getframeinfo(currentframe())
        print(" something went wrong in file: {}, line number: {}".format(frame_info.filename, frame_info.lineno+1))
    return average_time, pt


def testing_times_of_contains_random_strings(N=10000, number_of_values_in_the_tree=10000, number_of_chars=15):
    _, pt = testing_times_of_inserting_random_strings(number_of_values_in_the_tree, number_of_chars)
    contain_str = []
    for _ in range(N):
        contain_str.append(pt.get_random_value())

    start_time = time.perf_counter()
    for i in range(N):  # does contains this values

        res = pt.contains(contain_str[i])
        if not res:
            frame_info = getframeinfo(currentframe())
            print(
                " something went wrong in file: {}, line number: {}".format(frame_info.filename, frame_info.lineno + 1))
    end_time = time.perf_counter()

    average_time_finding = (end_time - start_time) / N

    contain_str = []
    for _ in range(N):
        contain_str.append(random_string(random.choice(range(number_of_chars))))

    start_time = time.perf_counter()
    for i in range(N):  # does contains this values

        res = pt.contains(contain_str[i])
        if res:
            frame_info = getframeinfo(currentframe())
            print(
                " something went wrong in file: {}, line number: {}".format(frame_info.filename, frame_info.lineno + 1))
    end_time = time.perf_counter()

    average_time_not_finding = (end_time - start_time) / N

    return average_time_finding, average_time_not_finding


def basic_test2():
    """
    >>> basic_test2()
    {
        "ab": {
            "c": {
                "__end_of_word__": null
            }
        }
    }
    {
        "ab": {
            "c": {
                "__end_of_word__": null
            }
        },
        "ba": {
            "r": {
                "__end_of_word__": null
            },
            "z": {
                "__end_of_word__": null
            },
            "rz": {
                "__end_of_word__": null
            }
        }
    }
    4
    True
    False
    True
    {
        "ab": {
            "c": {
                "__end_of_word__": null
            }
        },
        "ba": {
            "r": {
                "__end_of_word__": null
            },
            "z": {
                "__end_of_word__": null
            },
            "rz": {
                "__end_of_word__": null
            }
        },
        "as": {
            "sa": {
                "f": {
                    "__end_of_word__": null
                }
            }
        }
    }
    5
    """
    pt = PrefixTree2()
    pt.insert('abc')
    print(pt)
    pt.insert('bar')
    pt.insert('baz')
    pt.insert('barz')
    print(pt)
    print(len(pt))
    print(pt.contains('baz'))
    print(pt.contains('assaf'))
    pt.insert("assaf")
    print(pt.contains('assaf'))
    print(pt)
    print(len(pt))


def testing_times_of_inserting_random_strings2(N=10000, number_of_chars=15):
    pt = PrefixTree2()
    cnt = 0
    average_time = 0.0
    for _ in range(N):
        random_str = random_string(number_of_chars)
        start_time = time.perf_counter()
        res = pt.insert(random_str)
        end_time = time.perf_counter()
        average_time = average_time + end_time - start_time
        cnt = cnt + res
    average_time = average_time / N
    if cnt != pt.num_of_words:
        frame_info = getframeinfo(currentframe())
        print(" something went wrong in file: {}, line number: {}".format(frame_info.filename, frame_info.lineno+1))
    return average_time, pt


def testing_times_of_contains_random_strings2(N=10000, number_of_values_in_the_tree=10000, number_of_chars=15):
    _, pt = testing_times_of_inserting_random_strings2(number_of_values_in_the_tree, number_of_chars)
    contain_str = []
    for _ in range(N):
        contain_str.append(pt.get_random_value())

    start_time = time.perf_counter()
    for i in range(N):  # does contains this values

        res = pt.contains(contain_str[i])
        if not res:
            frame_info = getframeinfo(currentframe())
            print(
                " something went wrong in file: {}, line number: {}".format(frame_info.filename, frame_info.lineno + 1))
    end_time = time.perf_counter()

    average_time_finding = (end_time - start_time) / N

    contain_str = []
    for _ in range(N):
        contain_str.append(random_string(random.choice(range(number_of_chars))))

    start_time = time.perf_counter()
    for i in range(N):  # does contains this values

        res = pt.contains(contain_str[i])
        if res:
            frame_info = getframeinfo(currentframe())
            print(
                " something went wrong in file: {}, line number: {}".format(frame_info.filename, frame_info.lineno + 1))
    end_time = time.perf_counter()

    average_time_not_finding = (end_time - start_time) / N

    return average_time_finding, average_time_not_finding
