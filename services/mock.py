from models.mock import Mock as MockModel


class MockService:
    def __init__(self, db) -> None:
        self.db = db

    def get_all(self):
        mocks = self.db.query(MockModel).all()
        return mocks

    def get(self, endpoint: str):
        mock = self.db.query(MockModel).filter(
            MockModel.endpoint == endpoint).first()
        return mock

    def create(self, mock, response):
        self.db.add(MockModel(
            endpoint=mock.endpoint,
            prompt=mock.prompt,
            response=response
        ))
        self.db.commit()
        return
