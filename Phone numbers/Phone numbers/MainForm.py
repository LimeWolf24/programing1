import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        resources = System.Resources.ResourceManager("Phone_numbers.MainForm", System.Reflection.Assembly.GetEntryAssembly())
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.RosyBrown
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(24, 7)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(377, 296)
        self._label1.TabIndex = 0
        self._label1.Click += self.Label1Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.IndianRed
        self._button1.Font = System.Drawing.Font("MingLiU-ExtB", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(407, 0)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(119, 101)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.IndianRed
        self._button2.Font = System.Drawing.Font("MingLiU-ExtB", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(407, 107)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(119, 101)
        self._button2.TabIndex = 2
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.IndianRed
        self._button3.Font = System.Drawing.Font("MingLiU-ExtB", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(407, 214)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(119, 101)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
        self.ClientSize = System.Drawing.Size(551, 312)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Phone numbers"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label1.Text = " Jefferson Elementery School: (608) 743-6600, Marshall Middle School: (608) 743-6200, Craig High School: (608) 743-5200. Walmart: (608) 754-7800, Books-A-Million: (608) 752-6071."

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()