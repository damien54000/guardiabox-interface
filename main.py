from ui.menu import menu
from db.db import init_db
from ui.login import login_menu
init_db()

user_id = None
while user_id is None:
    user_id = login_menu()

menu(user_id)