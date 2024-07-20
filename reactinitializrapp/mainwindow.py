from reactinitializrapp.ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog
import markdown


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect signals and slots
        self.ui.directory_button.clicked.connect(self.getDirectory)

    def renderMarkdown(self, markdown_string):
        # Create a Markdown instance
        md = markdown.Markdown()

        # Convert the Markdown string to HTML
        html = md.convert(markdown_string)

        # Set the HTML content to the text browser
        self.ui.text_browser.setHtml(html)

    def getDirectory(self):
        # Get the directory path using QFileDialog
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')

        # Print the directory path
        if directory:
            print(directory)

        # Test markdown render
        self.renderMarkdown("<p>Follow the instructions to run the project:</p>\n  <ol>\n    <li>Download the zip project</li>\n    <li>Unzip the project in the desired folder</li>\n    <li>Open the terminal (<strong>Command Prompt on Windows</strong> or <strong>Terminal on macOS/Linux</strong>) in the project folder</li>\n    <li>Install the dependencies <code>npm install</code></li>\n    <li>Run the command <code>npm run dev</code></li>\n    <li>Modify the files for TailwindCSS following the steps from step 3: <a href=\"https://tailwindcss.com/docs/guides/vite#react\" target=\"_blank\">TailwindCSS Guide</a></li>\n  </ol>")
