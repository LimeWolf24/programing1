import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Font = System.Drawing.Font("MingLiU_HKSCS-ExtB", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Blue
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(824, 192)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Font = System.Drawing.Font("MingLiU_HKSCS-ExtB", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Blue
        self._button1.Location = System.Drawing.Point(276, 224)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(161, 63)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Font = System.Drawing.Font("MingLiU_HKSCS-ExtB", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Blue
        self._button2.Location = System.Drawing.Point(443, 224)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(169, 63)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.HotTrack
        self.ClientSize = System.Drawing.Size(848, 308)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Craig Rules"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Craig Rules!!"

    def Button2Click(self, sender, e):
        self._label.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()