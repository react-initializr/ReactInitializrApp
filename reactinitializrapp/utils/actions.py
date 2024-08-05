SET_CURRENT_PROJECT = "SET_CURRENT_PROJECT"
ADD_PROJECT = "ADD_PROJECT"
ARCHIVE_PROJECT = "ARCHIVE_PROJECT"


def set_current_project(project):
    return {"type": SET_CURRENT_PROJECT, "project": project}


def add_project(project):
    return {"type": ADD_PROJECT, "project": project}


def archive_project(project):
    return {"type": ARCHIVE_PROJECT, "project": project}
