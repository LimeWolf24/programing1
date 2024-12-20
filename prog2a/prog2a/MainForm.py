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
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Black
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Red
        self._label1.Location = System.Drawing.Point(14, 8)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(273, 47)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DimGray
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Gainsboro
        self._button1.Location = System.Drawing.Point(327, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(122, 165)
        self._button1.TabIndex = 6
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DimGray
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Gainsboro
        self._button2.Location = System.Drawing.Point(327, 202)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(122, 174)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DimGray
        self._button3.Font = System.Drawing.Font("Microsoft YaHei UI", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Gainsboro
        self._button3.Location = System.Drawing.Point(468, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(89, 370)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Black
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Red
        self._label2.Location = System.Drawing.Point(14, 55)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(273, 47)
        self._label2.TabIndex = 9
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Black
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Red
        self._label3.Location = System.Drawing.Point(14, 102)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(273, 47)
        self._label3.TabIndex = 10
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Black
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Red
        self._label4.Location = System.Drawing.Point(14, 149)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(273, 47)
        self._label4.TabIndex = 11
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Black
        self._label5.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.Red
        self._label5.Location = System.Drawing.Point(14, 196)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(273, 47)
        self._label5.TabIndex = 12
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Black
        self._label6.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.Red
        self._label6.Location = System.Drawing.Point(14, 243)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(273, 47)
        self._label6.TabIndex = 13
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Black
        self._label7.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.Red
        self._label7.Location = System.Drawing.Point(14, 290)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(273, 47)
        self._label7.TabIndex = 14
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(569, 384)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog2a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "The program you"
        self._label2.Text = "are using is"
        self._label3.Text = "called Pascal. It"
        self._label4.Text = "Will soon be your friend."
        self._label5.Text = "Oops! A mistake was"
        self._label6.Text = "just made. Please"
        self._label7.Text = "correct me."

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()