import os
import sys
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(app_path)

from conf.db_session import create_table


if __name__ == "__main__":
    create_table()

