import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 16
        self._listBox1.Location = System.Drawing.Point(12, 18)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(436, 340)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.RosyBrown
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(463, 18)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(134, 112)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.RosyBrown
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(463, 136)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(134, 112)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.RosyBrown
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(463, 254)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(134, 112)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MistyRose
        self.ClientSize = System.Drawing.Size(599, 372)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog122h"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "Number\tSquare\tSquare Root\tCube\t4th Root"
        self._listBox1.Items.Add(heading)
        for num in range(1, 16+1):
            nsqrd = num**2
            nsqrt = math.sqrt(num)
            line  = str(num) + "\t\t" + str(nsqrd) +\
                               "\t\t" + str(round(nsqrd,4))
            self._listBox1.Items.Add(line)

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()