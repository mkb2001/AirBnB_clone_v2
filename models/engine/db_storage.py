# models/engine/db_storage.py

class DBStorage:
    """Database Storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the engine and session"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}', pool_pre_ping=True)
        
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a class, or all objects if cls is None"""
        from models.state import State
        from models.city import City
        # Import other models here if needed
        
        objects = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f'{obj.__class__.__name__}.{obj.id}'
                objects[key] = obj
        else:
            for model in [State, City]: # Add other models to this list
                query_result = self.__session.query(model).all()
                for obj in query_result:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database"""
        from models.state import State
        from models.city import City
        # Import other models here if needed
        
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
