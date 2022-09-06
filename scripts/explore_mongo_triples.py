from pymongo import MongoClient

def main():
    client = MongoClient()
    triple_coll = client.roslog.triples
    graphs = {}
    for doc in triple_coll.find():
        if doc["graph"] not in graphs.keys():
            graphs[doc["graph"]] = 1
        else:
            graphs[doc["graph"]] += 1
    for graph_name, graph_count in graphs.items():
        print(f"{graph_name}: {graph_count}")


if __name__ == "__main__":
    main()