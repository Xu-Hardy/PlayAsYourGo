# import goslate
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import *
from PySide2.QtMultimediaWidgets import QVideoWidget
import sys
import os

os.environ['QT_MAC_WANTS_LAYER'] = '1'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = QMediaPlayer()
    vw=QVideoWidget()                       # 定义视频显示的widget
    vw.show()
    player.setVideoOutput(vw)                 # 视频播放输出的widget，就是上面定义的
    player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件
    print((QFileDialog.getOpenFileUrl()[0]))
    player.play()                               # 播放视频
    sys.exit(app.exec_())

# import PySide2