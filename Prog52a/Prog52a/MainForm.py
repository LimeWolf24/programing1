import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.IndianRed
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(376, 131)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(163, 35)
        self._label5.TabIndex = 4
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Crimson
        self.ClientSize = System.Drawing.Size(645, 310)
        self.Name = "MainForm"
        self.Text = "Prog52a"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)

    def Button1Click(self, sender, e):
        length = int(self._textBox1.Text)
        width  = int(self._textBox1.Text)
        area   = length * width
        perim  = 2 * length +2* width
        self._label5.Text = str(area)
        self._label6.Text = str(perim)
        # + - * / %      **pow     // divide & round downn
        #int (Intiger): a whole number pos/neg
        #float (Floating-Point-Number): any number w/ a decim
        #str (String): a string of text

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox5.Text = ""
        self._textBox6.Text = ""

    def Label8Click(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        pass