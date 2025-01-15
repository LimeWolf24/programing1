import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        resources = System.Resources.ResourceManager("Checkers.MainForm", System.Reflection.Assembly.GetEntryAssembly())
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Red
        self._label1.Location = System.Drawing.Point(12, 106)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 97)
        self._label1.TabIndex = 0
        self._label1.Text = "1"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Red
        self._label2.Location = System.Drawing.Point(102, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 97)
        self._label2.TabIndex = 1
        self._label2.Text = "2"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Red
        self._label3.Location = System.Drawing.Point(208, 106)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 97)
        self._label3.TabIndex = 2
        self._label3.Text = "3"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Red
        self._label4.Location = System.Drawing.Point(302, 9)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 97)
        self._label4.TabIndex = 3
        self._label4.Text = "4"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Red
        self._label5.Location = System.Drawing.Point(399, 106)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 97)
        self._label5.TabIndex = 4
        self._label5.Text = "5"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Red
        self._label6.Location = System.Drawing.Point(505, 9)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 97)
        self._label6.TabIndex = 5
        self._label6.Text = "6"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Black
        self._label7.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label7.Location = System.Drawing.Point(3, 498)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 97)
        self._label7.TabIndex = 6
        self._label7.Text = "1"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Black
        self._label8.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label8.Location = System.Drawing.Point(102, 397)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(100, 97)
        self._label8.TabIndex = 7
        self._label8.Text = "2"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.Black
        self._label9.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label9.Location = System.Drawing.Point(208, 498)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(100, 97)
        self._label9.TabIndex = 8
        self._label9.Text = "3"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.Black
        self._label10.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label10.Location = System.Drawing.Point(302, 397)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(100, 97)
        self._label10.TabIndex = 9
        self._label10.Text = "4"
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.Black
        self._label11.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label11.Location = System.Drawing.Point(399, 498)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(100, 97)
        self._label11.TabIndex = 10
        self._label11.Text = "5"
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.Black
        self._label12.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label12.Location = System.Drawing.Point(505, 397)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(100, 97)
        self._label12.TabIndex = 11
        self._label12.Text = "6"
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.White
        self._label13.Font = System.Drawing.Font("Microsoft YaHei UI", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(626, 9)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(136, 97)
        self._label13.TabIndex = 12
        self._label13.Text = "0"
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.White
        self._label14.Font = System.Drawing.Font("Microsoft YaHei UI", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(626, 485)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(136, 97)
        self._label14.TabIndex = 13
        self._label14.Text = "0"
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.White
        self._label15.Font = System.Drawing.Font("Microsoft PhagsPa", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(611, 200)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(281, 197)
        self._label15.TabIndex = 14
        self._label15.Text = resources.GetString("label15.Text")
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkGray
        self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
        self.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self.ClientSize = System.Drawing.Size(907, 591)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Checkers"
        self.ResumeLayout(False)



    def RedPlayer2LocationChanged(self, sender, e):
        if self._RedPlayer2.Location():
            Location == 108, 209
        if self._RedPlayer4.Location():
            Location == 108, 209 or Locaion == 308, 202
        if self._RedPlayer6.Location():
            Location == 308, 202 or Location == 505, 202
        if self._BlackPlayer2.Location():
            Location == 3, 300 or Location == 208, 300
        if self._BlackPlayer4.Location():
            Location == 208, 300 or Locaion == 399, 300
        if self._BlackPlayer6.Location():
            Location == 399, 300