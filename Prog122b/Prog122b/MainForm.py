import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.RosyBrown
        self._button1.Location = System.Drawing.Point(384, 61)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(85, 73)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.RosyBrown
        self._button2.Location = System.Drawing.Point(384, 171)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(85, 73)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.RosyBrown
        self._button3.Location = System.Drawing.Point(384, 291)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(85, 73)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Silver
        self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(28, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(344, 46)
        self._label1.TabIndex = 4
        self._label1.Text = "With four dollars per hour"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MistyRose
        self._label2.Location = System.Drawing.Point(29, 94)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(184, 270)
        self._label2.TabIndex = 5
        self._label2.Text = "label2"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MistyRose
        self._label3.Location = System.Drawing.Point(210, 94)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(162, 270)
        self._label3.TabIndex = 6
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.IndianRed
        self._label4.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(28, 55)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(344, 33)
        self._label4.TabIndex = 7
        self._label4.Text = "Hours                     Pay"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightCoral
        self.ClientSize = System.Drawing.Size(481, 379)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog122b"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
       pass
   

    def Button2Click(self, sender, e):
       pass
    def Button3Click(self, sender, e):
        Application.Exit()