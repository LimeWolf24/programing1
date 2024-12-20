import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label9 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(102, 67)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(113, 20)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(102, 16)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(114, 20)
        self._textBox2.TabIndex = 1
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkGreen
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(222, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(64, 43)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkGreen
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(292, 13)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(57, 43)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkGreen
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(355, 13)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(55, 43)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.DarkOliveGreen
        self._label9.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label9.Location = System.Drawing.Point(136, 127)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(268, 31)
        self._label9.TabIndex = 13
        self._label9.Click += self.Label9Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.SeaGreen
        self._label1.Font = System.Drawing.Font("Microsoft Yi Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(22, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(73, 31)
        self._label1.TabIndex = 28
        self._label1.Text = "Num 1:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.SeaGreen
        self._label2.Font = System.Drawing.Font("Microsoft Yi Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(22, 63)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(73, 31)
        self._label2.TabIndex = 29
        self._label2.Text = "Num 2:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.YellowGreen
        self._label3.Font = System.Drawing.Font("Microsoft Yi Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(22, 127)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(92, 31)
        self._label3.TabIndex = 30
        self._label3.Text = "Sum:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.YellowGreen
        self._label4.Font = System.Drawing.Font("Microsoft Yi Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(22, 171)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(92, 31)
        self._label4.TabIndex = 31
        self._label4.Text = "Difference:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.YellowGreen
        self._label5.Font = System.Drawing.Font("Microsoft Yi Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(22, 216)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(92, 31)
        self._label5.TabIndex = 32
        self._label5.Text = "Product:"
        self._label5.Click += self.Label5Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.YellowGreen
        self._label6.Font = System.Drawing.Font("Microsoft Yi Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(22, 258)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(92, 31)
        self._label6.TabIndex = 33
        self._label6.Text = "Average:"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.YellowGreen
        self._label8.Font = System.Drawing.Font("Microsoft Yi Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(22, 301)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(92, 31)
        self._label8.TabIndex = 34
        self._label8.Text = "Max:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.YellowGreen
        self._label7.Font = System.Drawing.Font("Microsoft Yi Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(22, 345)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(92, 31)
        self._label7.TabIndex = 35
        self._label7.Text = "Min:"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.DarkOliveGreen
        self._label10.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label10.Location = System.Drawing.Point(136, 174)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(268, 31)
        self._label10.TabIndex = 36
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.DarkOliveGreen
        self._label11.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label11.Location = System.Drawing.Point(136, 216)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(268, 31)
        self._label11.TabIndex = 37
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.DarkOliveGreen
        self._label12.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label12.Location = System.Drawing.Point(136, 258)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(268, 31)
        self._label12.TabIndex = 38
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.DarkOliveGreen
        self._label13.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label13.Location = System.Drawing.Point(136, 304)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(268, 31)
        self._label13.TabIndex = 39
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.DarkOliveGreen
        self._label14.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label14.Location = System.Drawing.Point(136, 345)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(268, 31)
        self._label14.TabIndex = 40
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(416, 414)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "prog88a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label8Click(self, sender, e):
        pass

    def Label9Click(self, sender, e):
        pass

    def Label13Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        Sum = num1 + num2
        Dif = num1 + num2
        self._label5.Text = str(perim)
        self._label6.Text = str(average)
        # TODO: finish product and average
        Abs = abs(Dif)
        Max = 0
        Min = 0
        if num1  >= num2:
            Max = Num1
        else:  # otherwise...
             Max = Num2
        
        if Max == num1: # If Max has the same value as num1 (==)
            Min = Num2
        else:
            Min = num1
        #TODO: put the rest of the nums in the labels and finish clear btn
        self._label13.Text = str(Max)
        self._label14.Text = str(Min)

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label5Click(self, sender, e):
        pass