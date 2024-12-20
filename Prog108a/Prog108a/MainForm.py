import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Silver
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label1.Location = System.Drawing.Point(21, 22)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(143, 57)
        self._label1.TabIndex = 0
        self._label1.Text = "Sconds"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Silver
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label2.Location = System.Drawing.Point(21, 110)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(143, 63)
        self._label2.TabIndex = 1
        self._label2.Text = "Minutes and Sconds"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(192, 22)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(184, 35)
        self._textBox1.TabIndex = 2
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Gainsboro
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(49, 252)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(115, 36)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Gainsboro
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(170, 252)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(115, 36)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Gainsboro
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(112, 294)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(115, 36)
        self._button3.TabIndex = 6
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label3.Location = System.Drawing.Point(192, 110)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(184, 63)
        self._label3.TabIndex = 7
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DimGray
        self.ClientSize = System.Drawing.Size(396, 332)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog108a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        strMinutesSeconds = ""
        # Combine minutes and seconds
        if strMinutesSeconds >= 60:
            return 60 or below
        else: 
            return 60 or higher
        self._label3.Text = strMinutesSeconds

    def Button2Click(self, sender, e):
        self._textBox1.Clear()
        self._label3.Text = ""
        
        self._textBox1.Focus()

    def Button3Click(self, sender, e):
       Application.Exit()