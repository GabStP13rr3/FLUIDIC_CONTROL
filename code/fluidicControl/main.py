from PyQt5.QtWidgets import QApplication
## from ui.(file name containing response function) import (class name)
from ui.ON_OFF import ON_OFF_RESPONSES


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    
    ## (var name) = class_name()
    ui = ON_OFF_RESPONSES()
    ui.show()
   
    sys.exit(app.exec_())
