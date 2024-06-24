import configparser
import sys
from datetime import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QTimer, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

from untitled import Ui_Form

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')


class WindowNotify(QWidget, Ui_Form):
    # 定义弹窗关闭信号
    SignalClosed = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(WindowNotify, self).__init__(*args, **kwargs)
        self.setupUi(self)  # 设置 UI
        self.label_name.setText(config.get('TITLE', '弹窗标题'))  # 从配置文件读取标题
        self._timeout = int(config.get('DEFAULT', '浮窗默认停留时间')) * 1000  # 从配置文件读取超时时间
        self.animation_duration = int(config.get('DEFAULT', '上浮动画持续时间')) * 1000  # 从配置文件读取上浮动画持续时间
        self._init()  # 初始化其他属性和事件
        self.setPresetText()  # 设置预设文本

    def format_timedelta(self):
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        return f"{int(hours)}小时{int(minutes)}分钟"

    def setPresetText(self):
        current_time = datetime.now()  # 获取当前时间

        start_time_am = datetime.strptime(config.get('TIMES', '第一次上班时间'), "%H:%M:%S")
        end_time_am = datetime.strptime(config.get('TIMES', '第一次下班时间'), "%H:%M:%S")

        start_time_pm = datetime.strptime(config.get('TIMES', '第二次上班时间'), "%H:%M:%S")
        end_time_pm = datetime.strptime(config.get('TIMES', '第二次下班时间'), "%H:%M:%S")

        period_am = config.get('PERIOD', '第一段上班期间名称')
        period_pm = config.get('PERIOD', '第二段上班期间名称')

        time_thresholds_am = []
        N = int(config.get('THRESHOLDS_AM', '数量'))  # 将获取的值转换为整数类型
        for i in range(1, N + 1):
            time_key = f'分钟{str(i)}'
            text_key = f'文本{str(i)}'
            time_parameter = config['THRESHOLDS_AM'].get(time_key)
            text_value = config['THRESHOLDS_AM'].get(text_key)
            time_value = int(time_parameter) * 60
            event = (time_value, text_value)
            time_thresholds_am.append(event)

        time_thresholds_break_am = config.get('THRESHOLDS_BREAK', '中途休息时间文本')
        time_thresholds_break_pm = config.get('THRESHOLDS_BREAK', '最终休息时间文本')

        time_thresholds_pm = []
        N = int(config.get('THRESHOLDS_PM', '数量'))  # 将获取的值转换为整数类型
        for i in range(1, N + 1):
            time_key = f'分钟{str(i)}'
            text_key = f'文本{str(i)}'
            time_parameter = config['THRESHOLDS_PM'].get(time_key)
            text_value = config['THRESHOLDS_PM'].get(text_key)
            time_value = int(time_parameter) * 60
            event = (time_value, text_value)
            time_thresholds_pm.append(event)

        def format_timedelta(delta):
            hours = delta.seconds // 3600
            minutes = (delta.seconds % 3600) // 60
            return f"{int(hours)}小时{int(minutes)}分钟"

        if (start_time_am.hour < current_time.hour < end_time_am.hour or
                (current_time.hour == start_time_am.hour and
                 current_time.minute >= start_time_am.minute) or
                (current_time.hour == end_time_am.hour and
                 current_time.minute < end_time_am.minute)):
            period1 = period_am
            period2 = period1
            start_time = start_time_am
            process_time = current_time - start_time
            remaining_time = end_time_am - current_time
            total_remaining_time = end_time_pm - start_time_pm + remaining_time
            text1 = ""
            text2 = ""
            for time_value, text_value in time_thresholds_am:
                if remaining_time.seconds > time_value:
                    othertext = text_value
                    break
        elif (start_time_pm.hour < current_time.hour < end_time_pm.hour or
              (current_time.hour == start_time_pm.hour and
               current_time.minute >= start_time_pm.minute) or
              (current_time.hour == end_time_pm.hour and
               current_time.minute < end_time_pm.minute)):
            period1 = period_pm
            period2 = period1
            start_time = start_time_pm
            process_time = current_time - start_time + end_time_am - start_time_am
            remaining_time = end_time_pm - current_time
            total_remaining_time = remaining_time
            text1 = ""
            text2 = ""
            for time_value, text_value in time_thresholds_pm:
                if remaining_time.seconds > time_value:
                    othertext = text_value
                    break
        elif (end_time_am.hour < current_time.hour < start_time_pm.hour or
              (current_time.hour == end_time_am.hour and
               current_time.minute >= end_time_am.minute) or
              (current_time.hour == start_time_pm.hour and
               current_time.minute < start_time_pm.minute)):
            period1 = period_pm
            period2 = period1
            start_time = start_time_pm
            process_time = end_time_am - start_time
            remaining_time = end_time_pm - start_time_pm
            total_remaining_time = remaining_time
            text1 = "将"
            text2 = ""
            othertext = time_thresholds_break_am
        elif (0 < current_time.hour < start_time_am.hour or
              (current_time.hour == start_time_am.hour and
               current_time.minute < start_time_am.minute)):
            period1 = period_am
            period2 = period1
            start_time = start_time_am
            process_time = start_time - start_time
            remaining_time = end_time_am - start_time_am + end_time_pm - start_time_pm
            total_remaining_time = remaining_time
            text1 = "将"
            text2 = ""
            othertext = time_thresholds_break_pm
        elif ((end_time_pm.hour < current_time.hour < 24) or
              (current_time.hour == end_time_pm.hour and
               current_time.minute >= end_time_pm.minute)):
            period1 = period_am
            period2 = "今日"
            start_time = start_time_am
            process_time = end_time_am - start_time_am + end_time_pm - start_time_pm
            remaining_time = end_time_pm - end_time_pm
            total_remaining_time = remaining_time
            text1 = "将"
            text2 = "明日"
            othertext = time_thresholds_break_pm
        else:
            period1 = ""
            period2 = ""
            start_time = ""
            process_time = ""
            remaining_time = ""
            total_remaining_time = ""
            text1 = ""
            text2 = ""
            othertext = "未能识别当前的时间段\n请稍后再试或联系作者。"

        process_time_str = format_timedelta(process_time)
        remaining_time_str = format_timedelta(remaining_time)
        total_remaining_time_str = format_timedelta(total_remaining_time)

        message = f"您{text1}从{text2}{period1}{start_time.strftime('%H:%M:%S')}开始上班\n" \
                  f"今日已经持续工作：{process_time_str}\n" \
                  f"{period2}上班剩余时间：{remaining_time_str}\n" \
                  f"当日总剩余工作时间：{total_remaining_time_str}\n\n" \
                  f"{othertext}"

        self.textEdit.setText(message)  # 设置textEdit的文本内容

    # 设置超时时间的方法
    def setTimeout(self, timeout):
        if isinstance(timeout, int):
            self._timeout = timeout
        return self

    # 获取超时时间的方法
    def timeout(self):
        return self._timeout

    # 关闭按钮点击事件处理方法
    def onClose(self):
        # 点击关闭按钮时，启动关闭动画
        self.isShow = False
        QTimer.singleShot(100, self.closeAnimation)  # 启动关闭动画

    # 初始化方法，设置窗口属性和事件
    def _init(self):
        # 设置窗口属性，如隐藏任务栏、无边框、顶层显示等
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint |
                            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗体透明
        # 窗口阴影
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 4)  # 偏移
        self.shadow.setBlurRadius(10)  # 阴影半径
        self.shadow.setColor(QColor(0, 0, 0, 100))  # 阴影颜色
        self.setGraphicsEffect(self.shadow)  # 将阴影效果应用到窗口
        # 连接关闭按钮的点击事件
        self.Button_close.clicked.connect(self.onClose)
        # 设置是否在显示的标志
        self.isShow = True
        # 设置超时标志
        self._timeouted = False
        # 获取当前桌面对象
        self._desktop = QApplication.instance().desktop()
        # 设置窗口初始开始位置
        self._startPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.screenGeometry().height()
        )
        # 设置窗口弹出结束位置
        self._endPos = QPoint(
            self._desktop.screenGeometry().width() - self.width() - 5,
            self._desktop.availableGeometry().height() - self.height() - 5
        )
        # 将窗口移动到初始位置
        self.move(self._startPos)

        # 初始化动画
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.finished.connect(self.onAnimationEnd)
        self.animation.setDuration(self.animation_duration)  # 设置动画持续时间为 1 秒

        # 初始化关闭定时器
        self._timer = QTimer(self, timeout=self.closeAnimation)

    # 显示弹窗的方法
    def show(self):
        # 停止定时器，隐藏窗口，设置标题和内容，设置超时时间，并显示窗口
        self._timer.stop()
        self.hide()
        self.move(self._startPos)
        super(WindowNotify, self).show()
        return self

    # 显示动画的方法
    def showAnimation(self):
        # 停止之前的动画，设置动画的起始和结束值，并启动动画
        self.isShow = True
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._endPos)
        self.animation.start()
        # 设置弹出 5 秒后如果没有焦点则关闭
        self._timer.start(self._timeout)

    # 关闭动画的方法
    def closeAnimation(self):
        # 判断是否有焦点，如果没有焦点则启动关闭动画
        if self.hasFocus():
            self._timeouted = True
            return
        self.isShow = False
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._startPos)
        self.animation.start()

    # 动画结束事件处理方法
    def onAnimationEnd(self):
        # 判断是否需要关闭窗口，并关闭窗口，停止定时器，发射关闭信号
        if not self.isShow:
            self.close()
            self._timer.stop()
            self.SignalClosed.emit()

    # # 鼠标进入窗口事件处理方法
    # def enterEvent(self, event):
    #     # 调用父类的 enterEvent 方法，设置焦点
    #     super(WindowNotify, self).enterEvent(event)
    #     self.setFocus(Qt.MouseFocusReason)
    #
    # # 鼠标离开窗口事件处理方法
    # def leaveEvent(self, event):
    #     # 调用父类的 leaveEvent 方法，取消焦点
    #     super(WindowNotify, self).leaveEvent(event)
    #     self.clearFocus()
    #     if self._timeouted:
    #         QTimer.singleShot(1000, self.closeAnimation)


if __name__ == "__main__":
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应分辨率
    app = QApplication(sys.argv)
    window = QWidget()
    notify = WindowNotify(parent=window)  # 创建 WindowNotify 实例作为通知弹窗
    notify.show().showAnimation()  # 直接显示通知弹窗并播放动画
    sys.exit(app.exec_())
