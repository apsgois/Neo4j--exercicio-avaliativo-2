from db.database import Graph


class EscolaDB():
    def __init__(self):
        self.db = Graph(uri='bolt://3.93.36.199:7687',
                        user='neo4j', password='finishes-piers-alerts')
