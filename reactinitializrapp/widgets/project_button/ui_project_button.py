from reactinitializrapp.models.project import Project


class UIProjectButton:
    def __init__(self, project_button, project: Project):
        self.project = project
        self.project_button = project_button
        self.project_button.setText(self.project.name)
        self.setup_styles()

    def setup_styles(self):
        self.project_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent; color: white; border: none; border-bottom: 1px solid #fff; padding: 10px 0; border-radius: 0;
            }
            QPushButton:hover {
                background-color: #292929;
                border-radius: 5px;
            }
            """
        )