import json
import sys  # sys нужен для передачи argv в QApplication
import importlib.util
import os
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QVBoxLayout, QHBoxLayout, QRadioButton, QComboBox




class FrameMenu(QtWidgets.QFrame):
    def __init__(self, startFunc):
        super().__init__()
        uic.loadUi(os.path.join('ui', 'frameMenu.ui'), self)

        self.currentModule = None
        self.modules = []

        self.parameters = {
            "demonstration_type" : "normal"
        }

        self.pushButtonStart.clicked.connect(startFunc)

        

        self.radioButtonStandard = QRadioButton("Обычный режим")
        self.radioButtonStandard.resize(150,20)
        self.radioButtonStandard.clicked.connect(self.radioClicked)
        self.radioButtonStandard.setChecked(True)

        self.radioButtonAttack = QRadioButton("Атака")
        self.radioButtonAttack.resize(150,20)
        self.radioButtonAttack.clicked.connect(self.radioClicked)

        self.radioButtonAttackDefense = QRadioButton("Атака + Защита")
        self.radioButtonAttackDefense.resize(150,20)
        self.radioButtonAttackDefense.clicked.connect(self.radioClicked)

        hbox = QHBoxLayout()
        self.groupBoxParameters.setLayout(hbox)

        vbox = QVBoxLayout()
        hbox.addLayout(vbox)
        self.extraParamsLayout = QVBoxLayout()
        hbox.addLayout(self.extraParamsLayout)
        
        vbox.addWidget(self.radioButtonStandard)
        vbox.addWidget(self.radioButtonAttack)
        vbox.addWidget(self.radioButtonAttackDefense)

        
        self.load_modules()

    def addParameter(self, parameter:QWidget):
        self.extraParamsLayout.addWidget(parameter)
        #self.groupBoxParameters.resize(self.groupBoxParameters.frameGeometry().width(), self.groupBoxParameters.frameGeometry().height() + 20 )
        

    def radioClicked(self):
        if self.radioButtonAttack.isChecked():
            self.parameters["demonstration_type"] = "attack"
        elif self.radioButtonAttackDefense.isChecked():
            self.parameters["demonstration_type"] = "protect"
        else:
            self.parameters["demonstration_type"] = "normal"

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
           
    @QtCore.pyqtSlot(QTreeWidgetItem, int)
    def select_module(self, item, column):
        module = self.getModuleByName(item.text(column))
        if module is None:
            return
        self.labelModuleName.setText(module["moduleName"])
        self.labelModuleDescription.setText(module["description"])
        self.currentModule = module
        self.pushButtonStart.setEnabled(True)



        current_module = self.currentModule
        modulePath = os.path.join(os.getcwd(), "modules", current_module["moduleName"], current_module["scriptPath"])

        spec = importlib.util.spec_from_file_location(current_module["moduleName"], modulePath)
        module = importlib.util.module_from_spec(spec)
        sys.modules[current_module["moduleName"]] = module
        spec.loader.exec_module(module)
        for param in module.addParams():
            self.addParameter(param)

                
    def getModule(self):
        return self.currentModule
    def getModuleByName(self, name):
        for module in self.modules:
            if module["moduleName"] == name:
                return module

    def getParameters(self):
        for i in range(self.extraParamsLayout.count()):
            param = self.extraParamsLayout.itemAt(i).widget()
            if  isinstance(param, QComboBox):
                self.parameters["param" + str(i)] = param.currentText()                
        return self.parameters



class DemonstrationApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Демонстрационный стенд \"Искусственный интеллект\"")
        self.resize(1000, 850)
        self.openMenu()

    def openMenu(self):
        self.frameMenu = FrameMenu(self.openDemo)
        self.setCentralWidget(self.frameMenu) 

    def openDemo(self):
        current_module = self.frameMenu.getModule()
        modulePath = os.path.join(os.getcwd(), "modules", current_module["moduleName"], current_module["scriptPath"])

        spec = importlib.util.spec_from_file_location(current_module["moduleName"], modulePath)
        module = importlib.util.module_from_spec(spec)
        sys.modules[current_module["moduleName"]] = module
        spec.loader.exec_module(module)

        self.frameMenu.getParameters()
        cm = module.Module(
                parent = self,
                demonstration_type = self.frameMenu.parameters["demonstration_type"], 
                slides = current_module["slides"]["normal"] + 1, 
                parameters = self.frameMenu.parameters
        )

        #ПОТОМ НАДО ВСЕ ЭТО В parameters ЗАПИХНУТЬ 
        # составляющие parameters свои для каждого preview класса
        self.setCentralWidget(cm.demoFrame)
        

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = DemonstrationApp()  # Создаём объект класса DemonstrationApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение



if __name__ == "__main__":
    main()