"""
Demo example

shows how to use the api(s) to create index and to make query
"""

import sys
from src.feed import Feeder
from src.peragro import PeragroClient


if __name__ == '__main__':
    f = Feeder()
    client = PeragroClient()

    dir_path = sys.argv[1]

    # feed data to elasticsearch for index creation
    f.feedAll(dir_path, iname="example_index", doc_type="ex_audio")
    print "index created"

    client.set_index("example_index")

    while True:
        print "[1] search by id"
        print "[2] search by text"
        print "[3] quit"

        choice = raw_input("Enter your choice: ")

        if choice == '1':
            id_ = raw_input("Enter id: ")
            res = client.get_sound(id_)

            if res:
                print res['_id'], "found"
            else:
                print id_, "not found"

        elif choice == '2':
            q = raw_input("Enter query: ")
            res = client.text_search(q)

        elif choice == '3':
            break

    # clear the indexes
    f.es.indices.delete(index="example_index")
