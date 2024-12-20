import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(365, 30)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(163, 60)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Maroon
        self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._textBox1.Location = System.Drawing.Point(143, 48)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(209, 29)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Maroon
        self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._textBox2.Location = System.Drawing.Point(143, 123)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(209, 29)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.Maroon
        self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._textBox3.Location = System.Drawing.Point(143, 202)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(209, 29)
        self._textBox3.TabIndex = 7
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(365, 105)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(163, 60)
        self._label2.TabIndex = 8
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(365, 184)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(163, 60)
        self._label3.TabIndex = 9
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Crimson
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(21, 309)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(141, 66)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Crimson
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(211, 309)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(141, 66)
        self._button2.TabIndex = 11
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Crimson
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(410, 309)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(141, 66)
        self._button3.TabIndex = 12
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(-1, 30)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(138, 60)
        self._label4.TabIndex = 13
        self._label4.Text = "Radius"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label5.Location = System.Drawing.Point(-1, 105)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(138, 60)
        self._label5.TabIndex = 14
        self._label5.Text = "Area"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label6.Location = System.Drawing.Point(-1, 184)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(138, 60)
        self._label6.TabIndex = 15
        self._label6.Text = "circumference"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MediumAquamarine
        self.ClientSize = System.Drawing.Size(563, 389)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        self._label1.Text = ""
        Radius == Diamiter/2
        self._label2.Text = ""
        Area == 3.14159*Radius
        self._label3.Text = ""
        Circumference == 2*3.14159*Radius

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Appliication.Exit()