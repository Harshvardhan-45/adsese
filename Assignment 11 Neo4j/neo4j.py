from neo4j import GraphDatabase


class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self._uri = uri
        self._user = user
        self._pwd = pwd
        self._conn = None
        try:
            self._conn = GraphDatabase.driver(self._uri, auth=(self._user, self._pwd))
        except Exception as e:
            print("Failed to create the connection:", e)

    def close(self):
        if self._conn is not None:
            self._conn.close()

    def query(self, query, db=None):
        assert self._conn is not None, "Connection not initialized!"
        session = None
        response = None
        try:
            session = self._conn.session(database=db) if db is not None else self._conn.session()
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response


conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", pwd="password")
