from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        return self.__add_obj(category, self.categories)

    def add_topic(self, topic: Topic) -> None:
        return self.__add_obj(topic, self.topics)

    def add_document(self, document: Document) -> None:
        return self.__add_obj(document, self.documents)

    def edit_category(self, category_id: int, new_name: str) -> None:
        return self.__edit_obj(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        return self.__edit_obj(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        return self.__edit_obj(document_id, self.documents, new_file_name)

    def delete_category(self, category_id) -> None:
        return self.__delete_obj(category_id, self.categories)

    def delete_topic(self, topic_id) -> None:
        return self.__delete_obj(topic_id, self.topics)

    def delete_document(self, document_id) -> None:
        return self.__delete_obj(document_id, self.documents)

    def get_document(self, document_id):
        return self.__find_obj(document_id, self.documents)

    def __repr__(self):
        return '\n'.join([doc.__repr__() for doc in self.documents])

    @staticmethod
    def __add_obj(obj: Category | Topic | Document, collection: list[Document | Category | Topic]):
        if obj not in collection:
            collection.append(obj)

    @classmethod
    def __edit_obj(cls, obj_id: int, collection: list[Document | Category | Topic], *args):
        obj = cls.__find_obj(obj_id, collection)
        if obj:
            obj.edit(*args)

    @classmethod
    def __delete_obj(cls, obj_id: int, collection: list[Document | Category | Topic]):
        obj = cls.__find_obj(obj_id, collection)
        if obj:
            collection.remove(obj)

    @staticmethod
    def __find_obj(obj_id: int, collection: list[Document | Category | Topic]) -> Document | Category | Topic | None:
        obj = next((obj for obj in collection if obj.id == obj_id), None)
        return obj
