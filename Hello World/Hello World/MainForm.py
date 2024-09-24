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
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Crimson
        self._label1.Cursor = System.Windows.Forms.Cursors.No
        self._label1.Font = System.Drawing.Font("MS Gothic", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(60, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(760, 212)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Crimson
        self._button1.Font = System.Drawing.Font("MS Gothic", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(60, 253)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(108, 42)
        self._button1.TabIndex = 1
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Crimson
        self._button2.Font = System.Drawing.Font("MS Gothic", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlText
        self._button2.Location = System.Drawing.Point(325, 253)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(104, 42)
        self._button2.TabIndex = 2
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Crimson
        self._button3.Font = System.Drawing.Font("MS Gothic", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlText
        self._button3.Location = System.Drawing.Point(554, 253)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(112, 42)
        self._button3.TabIndex = 3
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(875, 318)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Cursor = System.Windows.Forms.Cursors.Default
        self.Name = "MainForm"
        self.Text = "Hello World"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Hello, world!"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()