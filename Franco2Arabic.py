# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Franco2Arabic.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
txt=""
regex=[("th|TH|Th|tH","ث"),("^EL|^el|^El|^eL","ال"),("a|A","ا"),("B|b|p|P","ب") 
,("ya","يا"),("sh","ش"),("doctor","دكتور")
, ("c|C|k|K","ك")
,("2","ء"),
(" "," ") ,("ah|AH|Ah|aH","اه"),("eh","يه")
,("f|F","ف"),("s|S","س"),("r|R","ر"),("d|D","د"),("g|G","ج"),
("h|H","ه"),("j|J","چ"),("l|L","ل"),("m|M","م"),("n|N","ن"),
("O|o|OU|ou|oU|w|W|ow|WO|UO|uo|Uo|wo|Wo|OW","و")
,("q|Q","ق"),("^e|^E","إ"),("t|T","ت"),("u|U","ا"),("v|V","ڨ"),("x","إكس")
,("z|Z","ز"),("e|E|i|I|y|Y","ي"),("9","ص"),("6","ط"),("7","ح"),("8|'3","غ"),("5","خ"),
("sh|SH|Sh|sH|4","ش")
,("3","ع")]
FLM=""
LargestMatch=""
word=""
from PyQt5 import QtCore, QtGui, QtWidgets
import re

def is_start(Ch):
    flag=False
    idx = Ch
    global txt
    if(idx==0 or txt[idx-1]==' ' ):
        flag = True
    return flag
def is_last(index):
    f=False
    global txt
    if(index+1==len(txt)):
        f = True
    elif(txt[index+1]==" "):
        f = True
    ''' spaceidx= txt.find(" ",index,len(txt))
    if(spaceidx-index==1):
        f=True'''
    return f       
def Optimize (Eflag,Sflag):
    global FLM 
    global LargestMatch
    if(FLM.lower()=="el" and  not (Sflag)):
        LargestMatch="يل"
    elif( not (Sflag) and FLM.lower()=='e'):
        LargestMatch='ي'
    elif(Sflag  and FLM.lower()=='o'):
        LargestMatch='ا'
    elif(Sflag and not(Eflag) and FLM.lower()=="eh"):
        LargestMatch="إه"
    elif(Eflag and Sflag and (FLM.lower()=='a' or FLM.lower() == "ah" or  FLM.lower()=="eh")):
        LargestMatch="ايه"
    elif(Eflag and FLM.lower()=='a'):
        LargestMatch='ه'
def LCS(i):
    global stri
    stri=""
    global LargestMatch
    LargestMatch=" "
    global FLM
    FLM=" "
    Sflag=is_start(i)
    for c in range(i,len(txt)):
        if txt[c] == " ":
            break
        stri+=txt[c]
        global regex
        for a,b in regex:
            if(re.match(a,stri)):
                if(LargestMatch != b):
                    FLM=stri
                LargestMatch=b
                
                break
    Eflag=is_last(i+len(LargestMatch)-1)
    
    Optimize(Eflag,Sflag)
    return LargestMatch




def trans():
    global txt
    try:
        txt=str(ui.textEdit_2.toPlainText())
    except Exception as e: print(e)
    txt=txt.lower()
    word=""    
    stri=""
    c=0
    while(c<len(txt)):
        global FLM
        stri=LCS(c)
        count=len(FLM)
        word+=stri
        c+=count    
    ui.textEdit.setText(str(word))

class Ui_FrancoArab(object):
    def setupUi(self, FrancoArab):
        FrancoArab.setObjectName("FrancoArab")
        FrancoArab.resize(800, 465)
        self.centralwidget = QtWidgets.QWidget(FrancoArab)
        self.centralwidget.setObjectName("centralwidget")
        self.bgb = QtWidgets.QPushButton(self.centralwidget)
        self.bgb.setGeometry(QtCore.QRect(350, 330, 121, 61))
        self.bgb.setObjectName("bgb")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(422, 110, 261, 141))
        
        self.textEdit_2.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 110, 281, 141))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 80, 181, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 131, 16))
        self.label_2.setObjectName("label_2")
        FrancoArab.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrancoArab)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        FrancoArab.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrancoArab)
        self.statusbar.setObjectName("statusbar")
        FrancoArab.setStatusBar(self.statusbar)
        self.bgb.clicked.connect(trans)
        self.retranslateUi(FrancoArab)
        QtCore.QMetaObject.connectSlotsByName(FrancoArab)

    def retranslateUi(self, FrancoArab):
        _translate = QtCore.QCoreApplication.translate
        FrancoArab.setWindowTitle(_translate("FrancoArab", "Franco-Arab"))
        self.bgb.setText(_translate("FrancoArab", "Translate"))
        self.textEdit_2.setHtml(_translate("FrancoArab", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setHtml(_translate("FrancoArab", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("FrancoArab", "Type Franco - Arab here"))
        self.label_2.setText(_translate("FrancoArab", "Translation appears here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrancoArab = QtWidgets.QMainWindow()
    ui = Ui_FrancoArab()
    ui.setupUi(FrancoArab)
    FrancoArab.show()
    sys.exit(app.exec_())
