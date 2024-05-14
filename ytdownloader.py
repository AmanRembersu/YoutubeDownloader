import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from pytube import YouTube

class YoutubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('YouTube Video Downloader')
        self.setGeometry(100, 100, 400, 150)

        self.url_label = QLabel('Enter YouTube URL:', self)
        self.url_label.move(10, 10)

        self.url_entry = QLineEdit(self)
        self.url_entry.setGeometry(150, 10, 240, 20)

        self.download_button = QPushButton('Download', self)
        self.download_button.setGeometry(150, 40, 80, 25)
        self.download_button.clicked.connect(self.download_video)

        self.show()

    def download_video(self):
        url = self.url_entry.text()
        try:
            yt = YouTube(url)
            stream = yt.streams.first()
            stream.download()
            QMessageBox.information(self, 'Success', 'Video downloaded successfully!')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YoutubeDownloader()
    sys.exit(app.exec_())
