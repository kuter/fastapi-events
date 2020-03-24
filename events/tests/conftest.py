import sys

from alembic.command import downgrade, upgrade
from alembic.config import Config as AlembicConfig
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_DB_URL = "sqlite:///./test.db"
ALEMBIC_INI = "/home/kuter/workspace/github/fastapi-events/alembic.ini"


@pytest.fixture(scope="session")
def db(request):
    engine = create_engine(TEST_DB_URL, echo=True)
    Session = sessionmaker(bind=engine)

    alembic_config = AlembicConfig(ALEMBIC_INI)
    alembic_config.set_main_option("sqlalchemy.url", TEST_DB_URL)
    upgrade(alembic_config, "head")

    yield Session()

    downgrade(alembic_config, "base")
    engine.dispose()