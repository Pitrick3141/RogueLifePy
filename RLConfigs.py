from PySide6.QtWidgets import QMessageBox

import RLDebug
import global_var


class Configs:
    # 配置项字典
    _configs = {}

    def __init__(self):
        RLDebug.debug("配置项模块初始化完成", type='success', who=self.__class__.__name__)

    def apply_config(self, config_file):
        # 应用配置文件

        # 检测配置文件是否启用
        if not config_file.get('enabled') is True:
            RLDebug.debug("配置文件未被启用或格式错误，跳过本次解析", type='error', who=self.__class__.__name__)
            return

        # 检测配置文件版本是否符合
        from global_var import current_version
        if not config_file.get('version') in [current_version, '*', 'all']:
            RLDebug.debug(
                "配置文件版本不符或格式错误，跳过本次解析<br>当前版本: {}<br>配置文件版本: {}".format(
                    current_version,
                    config_file.get('version')),
                type='error', who=self.__class__.__name__)
            return

        # 可用配置项
        valid_keys = ['ignored_version', 'allow_command', 'discovered_eggs', 'enable_debug', 'enable_editor']

        # 配置项计数
        cnt = 0

        # 应用配置项
        for key in valid_keys:

            # 读取配置文件中的配置项
            if key in config_file.keys():
                RLDebug.debug("发现配置项: {} = {}".format(key, config_file.get(key)), who=self.__class__.__name__)

                # 检测配置项是否已经存在
                if key in self.config_keys():

                    # 若重复添加相同的配置项
                    if self.get_config(key) == config_file.get(key):
                        RLDebug.debug("已存在完全相同的配置项: {}, 配置项值为{}, 跳过本次应用配置项值".format(
                            key,
                            self.get_config(key)),
                            type='warn', who=self.__class__.__name__)
                        continue

                    RLDebug.debug("已存在的配置项: {}"
                                  "<br>原配置项值: {}"
                                  "<br>新配置项值: {}, 已弹窗询问".format(key, self._configs.get(key), config_file.get(key)),
                                  type='warn', who=self.__class__.__name__)

                    # 弹窗询问处理方法
                    msgbox = QMessageBox()
                    msgbox.setWindowTitle("重复的配置项")
                    msgbox.setText("你要添加的配置项已存在")
                    msgbox.setInformativeText("你想要覆盖原本的配置项值吗？")
                    msgbox.setDetailedText(
                        "已存在的配置项: {}\n原配置项值: {}\n新配置项值: {}".format(
                            key,
                            self._configs.get(key),
                            config_file.get(key)))
                    msgbox.setIcon(QMessageBox.StandardButton.Question)
                    msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                    msgbox.setDefaultButton(QMessageBox.StandardButton.Yes)
                    msgbox.setButtonText(QMessageBox.StandardButton.Yes, "使用新配置项值")
                    msgbox.setButtonText(QMessageBox.StandardButton.No, "保留原配置项值")
                    ret = msgbox.exec_()

                    # 处理弹窗结果
                    if ret == QMessageBox.StandardButton.Yes:
                        # 覆盖为新配置项值
                        self._configs[key] = config_file.get(key)
                        cnt += 1
                        RLDebug.debug("配置项{}已被覆盖为新配置项值: {}".format(key, config_file.get(key)),
                                      type='success', who=self.__class__.__name__)
                    else:
                        # 保留原配置项值
                        RLDebug.debug("配置项{}仍保留为原配置项值: {}".format(key, self._configs.get(key)),
                                      type='success', who=self.__class__.__name__)
                        return

                else:

                    # 应用配置项
                    self._configs[key] = config_file.get(key)
                    cnt += 1
                    RLDebug.debug("配置项{}已设为: {}".format(key, config_file.get(key)), type='success',
                                  who=self.__class__.__name__)

        RLDebug.debug("配置文件解析完成，共应用了{}个配置项".format(cnt), type='success', who=self.__class__.__name__)

    def set_config(self, key, value):

        # 设置配置项
        self._configs[key] = value
        return

    def get_config(self, key):

        # 获取配置项
        return self._configs.get(key)

    def config_keys(self):

        # 取得配置项键表
        return self._configs.keys()


def init():
    global_var.configs = Configs()
