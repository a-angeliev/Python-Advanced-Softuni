from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if not category in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if not topic in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if not document in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for cat in self.categories:
            if cat.id == category_id:
                cat.name = new_name
                break

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for top in self.topics:
            if top.id == topic_id:
                top.topic = new_topic
                top.storage_folder = new_storage_folder
                break

    def edit_document(self, document_id, new_file_name):
        for doc in self.documents:
            if doc.id == document_id:
                doc.file_name = new_file_name
                break

    def delete_category(self, category_id):
        for cat in self.categories:
            if cat.id == category_id:
                self.categories.remove(cat)
                break

    def delete_topic(self, topic_id):
        for top in self.topics:
            if top.id == topic_id:
                self.topics.remove(top)
                break

    def delete_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                self.documents.remove(doc)
                break

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc

    def __repr__(self):
        string = ""
        for doc in self.documents:
            string += f"{doc}\n"
        return string

