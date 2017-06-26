class DatasetsClient():
  def __init__(self, connection):
    self.__connection = connection

  def find_or_create(self, dataset_id, fields, unique_by=None):
    body = {
      'fields': fields,
    }

    if unique_by is not None:
      body['unique_by'] = unique_by

    return self.__connection.put('/datasets/' + dataset_id, body)

  def delete(self, dataset_id):
    self.__connection.delete('/datasets/' + dataset_id)

    return True