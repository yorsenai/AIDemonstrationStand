import json
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import  QTreeWidgetItem, QHBoxLayout
import main_window_design  # Это наш конвертированный файл дизайна
import demonstration_window_design
import frame_menu_design
import frame_demonstration_design
import os


class FrameDemo(QtWidgets.QFrame, frame_demonstration_design.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна



class FrameMenu(QtWidgets.QFrame, frame_menu_design.Ui_Frame):
    def __init__(self, startFunc):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.currentModule = None
        self.modules = []

        self.pushButtonStart.clicked.connect(startFunc)

        self.startup()

    def onClick(self):
        self.frameMenu.hide()
        l = QtWidgets.QLabel()
        l.show()

    def startup(self):
        self.load_modules()

    def load_modules(self):
        cwd = os.getcwd()
        if "modules" not in os.listdir(cwd):
            print("Папка с модулями не найдена")
            return False
        
        modulesDir = os.path.join(cwd, "modules")
        
        categories = dict()
        for module in os.listdir(modulesDir):
            moduleDir = os.path.join(modulesDir, module)
            with open(os.path.join(moduleDir, "module.conf"), "r", encoding="utf-8") as file:
                confData = json.load(file)
                self.modules.append(confData)
                if confData["moduleCategory"] not in categories.keys():
                    categories[confData["moduleCategory"]] = []
                categories[confData["moduleCategory"]].append(confData)

        
        
        for category in categories.items():
            twCategory = QTreeWidgetItem([category[0]])
            for module in category[1]:
                twCategory.addChild(QTreeWidgetItem([module["moduleName"]]))

            self.treeWidgetModules.addTopLevelItem(twCategory)

        self.treeWidgetModules.expandAll()
        self.treeWidgetModules.itemClicked.connect(self.select_module)
           
    @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
    def select_module(self, item, column):
        module = self.getModuleByName(item.text(column))
        if module is None:
            return
        self.labelModuleName.setText(module["moduleName"])
        self.labelModuleDescription.setText(module["description"])
        self.currentModule = module
        
    def getModuleByName(self, name):
        for module in self.modules:
            if module["moduleName"] == name:
                return module




class DemonstrationApp(QtWidgets.QMainWindow, main_window_design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        self.frameDemo = FrameDemo()
        self.frameMenu = FrameMenu(self.openDemo)

        #self.openDemo()
        self.openMenu()

    def openMenu(self):
        self.setCentralWidget(self.frameMenu) 

    def openDemo(self):
        self.setCentralWidget(self.frameDemo)
        
        

    

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = DemonstrationApp()  # Создаём объект класса DemonstrationApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение



if __name__ == "__main__":
    main()