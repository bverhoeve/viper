import os

import pytest
from viper.app import app

@pytest.fixture
def client():
  # Configure webapp in testing mode
  app.config['TESTING'] = True

  with app.test_client() as client:
    with app.app_context():
      pass
    yield client