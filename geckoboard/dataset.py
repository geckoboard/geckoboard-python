class Dataset():
    def __init__(self, dataset_id, connection):
        self.__id = dataset_id
        self.__connection = connection

    def put(self, items):
        body = {
            'data': items,
        }

        self.__connection.put('/datasets/' + self.__id + '/data', body)

        return True

    def post(self, items, delete_by=None):
        body = {
            'data': items,
        }

        if delete_by is not None:
            body['delete_by'] = delete_by

        self.__connection.post('/datasets/' + self.__id + '/data', body)

        return True

    def delete(self):
        self.__connection.delete('/datasets/' + self.__id)

        return True
