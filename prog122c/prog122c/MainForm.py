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
        self._listBox2 = System.Windows.Forms.ListBox()
        self._listBox3 = System.Windows.Forms.ListBox()
        self._listBox4 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.DimGray
        self._listBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 21
        self._listBox1.Location = System.Drawing.Point(23, 15)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(91, 256)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.OliveDrab
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(23, 294)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(116, 82)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.OliveDrab
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(184, 294)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(116, 82)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.OliveDrab
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(349, 294)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(116, 82)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # listBox2
        # 
        self._listBox2.BackColor = System.Drawing.Color.DimGray
        self._listBox2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox2.FormattingEnabled = True
        self._listBox2.ItemHeight = 21
        self._listBox2.Location = System.Drawing.Point(149, 15)
        self._listBox2.Name = "listBox2"
        self._listBox2.Size = System.Drawing.Size(91, 256)
        self._listBox2.TabIndex = 4
        # 
        # listBox3
        # 
        self._listBox3.BackColor = System.Drawing.Color.DimGray
        self._listBox3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox3.FormattingEnabled = True
        self._listBox3.ItemHeight = 21
        self._listBox3.Location = System.Drawing.Point(277, 15)
        self._listBox3.Name = "listBox3"
        self._listBox3.Size = System.Drawing.Size(91, 256)
        self._listBox3.TabIndex = 5
        # 
        # listBox4
        # 
        self._listBox4.BackColor = System.Drawing.Color.DimGray
        self._listBox4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox4.FormattingEnabled = True
        self._listBox4.ItemHeight = 21
        self._listBox4.Location = System.Drawing.Point(399, 15)
        self._listBox4.Name = "listBox4"
        self._listBox4.Size = System.Drawing.Size(91, 256)
        self._listBox4.TabIndex = 6
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkOliveGreen
        self.ClientSize = System.Drawing.Size(511, 388)
        self.Controls.Add(self._listBox4)
        self.Controls.Add(self._listBox3)
        self.Controls.Add(self._listBox2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122c"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "2"
        self._listBox1.Items.Add(heading)
        heading = "3"
        self._listBox2.Items.Add(heading)
        heading = "4"
        self._listBox3.Items.Add(heading)
        heading = "4"
        self._listBox4.Items.Add(heading)
        

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()
        self._listBox2.Items.Clear()
        self._listBox3.Items.Clear()
        self._listBox4.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()