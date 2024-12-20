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
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkRed
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Transparent
        self._label1.Location = System.Drawing.Point(12, 66)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(321, 76)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightCoral
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(342, 18)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(86, 48)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightCoral
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(434, 18)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(98, 48)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Maroon
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Transparent
        self._button3.Location = System.Drawing.Point(458, 72)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(74, 287)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkRed
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Transparent
        self._label2.Location = System.Drawing.Point(12, 283)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(321, 76)
        self._label2.TabIndex = 4
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkRed
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Transparent
        self._label3.Location = System.Drawing.Point(12, 18)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(321, 48)
        self._label3.TabIndex = 5
        self._label3.Text = "American"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DarkRed
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Transparent
        self._label4.Location = System.Drawing.Point(12, 236)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(321, 47)
        self._label4.TabIndex = 6
        self._label4.Text = "European"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Brown
        self.ClientSize = System.Drawing.Size(544, 387)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog65a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "12/24/24"
        self._label2.Text = "24/12/24"

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()