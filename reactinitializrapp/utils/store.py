from reactinitializrapp.models.project import Project
from reactinitializrapp.utils.reducer import reducer
from reactinitializrapp.utils.database import Database


# Store Singleton & Observer Pattern
class Store:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Store, cls).__new__(cls, *args, **kwargs)
            try:
                database = Database.get_instance()
                cls._instance.session = database.get_session()
                cls._instance.state = {
                    "current_project": None,
                    "projects": cls._instance.session.query(Project).all(),
                    "archived_projects": [],
                }
                cls._instance.subscribers = []
            except Exception as e:
                print(f"Error initializing Store: {e}")
                cls._instance = None
        return cls._instance

    def get_state(self):
        return self.state

    def dispatch(self, action):
        self.state = reducer(self.state, action)
        self.notify_subscribers()

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber()
