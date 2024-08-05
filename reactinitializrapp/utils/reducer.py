from reactinitializrapp.models.project import Project
from reactinitializrapp.utils.actions import (
    ADD_PROJECT,
    ARCHIVE_PROJECT,
    SET_CURRENT_PROJECT,
)
from reactinitializrapp.utils.database import Database


def reducer(state, action):
    new_state = state.copy()
    if action["type"] == SET_CURRENT_PROJECT:
        new_state["current_project"] = action["project"]
    elif action["type"] == ADD_PROJECT:
        add_project(action["project"])
    elif action["type"] == ARCHIVE_PROJECT:
        if "archived_projects" not in new_state:
            new_state["archived_projects"] = []
        if "projects" not in new_state:
            new_state["projects"] = []
        new_state["archived_projects"].append(action["project"])
        new_state["projects"].remove(action["project"])
    return new_state


def add_project(project: Project):
    database = Database.get_instance()
    session = database.get_session()
    try:
        session.add(project)
        session.commit()
        session.refresh(project)
    except Exception as e:
        session.rollback()
        print(f"Error adding project: {e}")
    finally:
        session.close()
