import falcon


class HTTP301Status (falcon.HTTPStatus):
    def __init__(self, location, headers=None):
        if headers is None:
            headers = {}

        headers.setdefault("location", location)

        super().__init__(falcon.HTTP_301, headers)
