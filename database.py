from sqlmodel import Field, Session, SQLModel, create_engine, select

postgres_url = "postgresql+psycopg://postgres:postgres@localhost:5433/tasks"
engine = create_engine(postgres_url, connect_args={})


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session