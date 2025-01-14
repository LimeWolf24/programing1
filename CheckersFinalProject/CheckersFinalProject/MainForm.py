import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        resources = System.Resources.ResourceManager("CheckersFinalProject.MainForm", System.Reflection.Assembly.GetEntryAssembly())
        self._RedPlayer1 = System.Windows.Forms.Label()
        self._RedPlayer2 = System.Windows.Forms.Label()
        self._RedPlayer3 = System.Windows.Forms.Label()
        self._RedPlayer4 = System.Windows.Forms.Label()
        self._RedPlayer5 = System.Windows.Forms.Label()
        self._RedPlayer6 = System.Windows.Forms.Label()
        self._BlackPlayer1 = System.Windows.Forms.Label()
        self._BlackPlayer2 = System.Windows.Forms.Label()
        self._BlackPlayer3 = System.Windows.Forms.Label()
        self._BlackPlayer4 = System.Windows.Forms.Label()
        self._BlackPlayer5 = System.Windows.Forms.Label()
        self._BlackPlayer6 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # RedPlayer1
        # 
        self._RedPlayer1.BackColor = System.Drawing.Color.Red
        self._RedPlayer1.Location = System.Drawing.Point(111, 9)
        self._RedPlayer1.Name = "RedPlayer1"
        self._RedPlayer1.Size = System.Drawing.Size(92, 93)
        self._RedPlayer1.TabIndex = 0
        self._RedPlayer1.Text = "1"
        self._RedPlayer1.Click += self.RedPlayer1Click
        # 
        # RedPlayer2
        # 
        self._RedPlayer2.BackColor = System.Drawing.Color.Red
        self._RedPlayer2.Location = System.Drawing.Point(12, 107)
        self._RedPlayer2.Name = "RedPlayer2"
        self._RedPlayer2.Size = System.Drawing.Size(95, 96)
        self._RedPlayer2.TabIndex = 1
        self._RedPlayer2.Text = "2"
        self._RedPlayer2.Click += self.RedPlayer2Click
        # 
        # RedPlayer3
        # 
        self._RedPlayer3.BackColor = System.Drawing.Color.Red
        self._RedPlayer3.Location = System.Drawing.Point(308, 9)
        self._RedPlayer3.Name = "RedPlayer3"
        self._RedPlayer3.Size = System.Drawing.Size(98, 93)
        self._RedPlayer3.TabIndex = 2
        self._RedPlayer3.Text = "3"
        self._RedPlayer3.Click += self.RedPlayer3Click
        # 
        # RedPlayer4
        # 
        self._RedPlayer4.BackColor = System.Drawing.Color.Red
        self._RedPlayer4.Location = System.Drawing.Point(213, 107)
        self._RedPlayer4.Name = "RedPlayer4"
        self._RedPlayer4.Size = System.Drawing.Size(95, 96)
        self._RedPlayer4.TabIndex = 3
        self._RedPlayer4.Text = "4"
        self._RedPlayer4.Click += self.RedPlayer4Click
        # 
        # RedPlayer5
        # 
        self._RedPlayer5.BackColor = System.Drawing.Color.Red
        self._RedPlayer5.Location = System.Drawing.Point(508, 9)
        self._RedPlayer5.Name = "RedPlayer5"
        self._RedPlayer5.Size = System.Drawing.Size(94, 93)
        self._RedPlayer5.TabIndex = 4
        self._RedPlayer5.Text = "5"
        self._RedPlayer5.Click += self.RedPlayer5Click
        # 
        # RedPlayer6
        # 
        self._RedPlayer6.BackColor = System.Drawing.Color.Red
        self._RedPlayer6.Location = System.Drawing.Point(410, 107)
        self._RedPlayer6.Name = "RedPlayer6"
        self._RedPlayer6.Size = System.Drawing.Size(97, 96)
        self._RedPlayer6.TabIndex = 5
        self._RedPlayer6.Text = "6"
        self._RedPlayer6.Click += self.RedPlayer6Click
        # 
        # BlackPlayer1
        # 
        self._BlackPlayer1.BackColor = System.Drawing.Color.Black
        self._BlackPlayer1.ForeColor = System.Drawing.Color.White
        self._BlackPlayer1.Location = System.Drawing.Point(111, 401)
        self._BlackPlayer1.Name = "BlackPlayer1"
        self._BlackPlayer1.Size = System.Drawing.Size(92, 97)
        self._BlackPlayer1.TabIndex = 6
        self._BlackPlayer1.Text = "1"
        self._BlackPlayer1.Click += self.BlackPlayer1Click
        # 
        # BlackPlayer2
        # 
        self._BlackPlayer2.BackColor = System.Drawing.Color.Black
        self._BlackPlayer2.ForeColor = System.Drawing.Color.White
        self._BlackPlayer2.Location = System.Drawing.Point(12, 305)
        self._BlackPlayer2.Name = "BlackPlayer2"
        self._BlackPlayer2.Size = System.Drawing.Size(95, 89)
        self._BlackPlayer2.TabIndex = 7
        self._BlackPlayer2.Text = "2"
        self._BlackPlayer2.Click += self.BlackPlayer2Click
        # 
        # BlackPlayer3
        # 
        self._BlackPlayer3.BackColor = System.Drawing.Color.Black
        self._BlackPlayer3.ForeColor = System.Drawing.Color.White
        self._BlackPlayer3.Location = System.Drawing.Point(308, 401)
        self._BlackPlayer3.Name = "BlackPlayer3"
        self._BlackPlayer3.Size = System.Drawing.Size(98, 97)
        self._BlackPlayer3.TabIndex = 8
        self._BlackPlayer3.Text = "3"
        self._BlackPlayer3.Click += self.BlackPlayer3Click
        # 
        # BlackPlayer4
        # 
        self._BlackPlayer4.BackColor = System.Drawing.Color.Black
        self._BlackPlayer4.ForeColor = System.Drawing.Color.White
        self._BlackPlayer4.Location = System.Drawing.Point(204, 305)
        self._BlackPlayer4.Name = "BlackPlayer4"
        self._BlackPlayer4.Size = System.Drawing.Size(95, 89)
        self._BlackPlayer4.TabIndex = 9
        self._BlackPlayer4.Text = "4"
        self._BlackPlayer4.Click += self.BlackPlayer4Click
        # 
        # BlackPlayer5
        # 
        self._BlackPlayer5.BackColor = System.Drawing.Color.Black
        self._BlackPlayer5.ForeColor = System.Drawing.Color.White
        self._BlackPlayer5.Location = System.Drawing.Point(508, 395)
        self._BlackPlayer5.Name = "BlackPlayer5"
        self._BlackPlayer5.Size = System.Drawing.Size(94, 97)
        self._BlackPlayer5.TabIndex = 10
        self._BlackPlayer5.Text = "5"
        # 
        # BlackPlayer6
        # 
        self._BlackPlayer6.BackColor = System.Drawing.Color.Black
        self._BlackPlayer6.ForeColor = System.Drawing.Color.White
        self._BlackPlayer6.Location = System.Drawing.Point(410, 305)
        self._BlackPlayer6.Name = "BlackPlayer6"
        self._BlackPlayer6.Size = System.Drawing.Size(88, 89)
        self._BlackPlayer6.TabIndex = 11
        self._BlackPlayer6.Text = "6"
        # 
        # label1
        # 
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(620, 167)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(305, 176)
        self._label1.TabIndex = 12
        self._label1.Text = resources.GetString("label1.Text")
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Red
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Cursor = System.Windows.Forms.Cursors.Default
        self._label2.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(620, 23)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(124, 95)
        self._label2.TabIndex = 13
        self._label2.Text = "0"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Black
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(620, 389)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(124, 95)
        self._label3.TabIndex = 14
        self._label3.Text = "0"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(761, 23)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(164, 38)
        self._label4.TabIndex = 15
        self._label4.Text = "Red Player points"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(750, 395)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(164, 38)
        self._label5.TabIndex = 16
        self._label5.Text = "Black Player points"
        # 
        # MainForm
        # 
        self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
        self.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self.ClientSize = System.Drawing.Size(937, 493)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._BlackPlayer6)
        self.Controls.Add(self._BlackPlayer5)
        self.Controls.Add(self._BlackPlayer4)
        self.Controls.Add(self._BlackPlayer3)
        self.Controls.Add(self._BlackPlayer2)
        self.Controls.Add(self._BlackPlayer1)
        self.Controls.Add(self._RedPlayer6)
        self.Controls.Add(self._RedPlayer5)
        self.Controls.Add(self._RedPlayer4)
        self.Controls.Add(self._RedPlayer3)
        self.Controls.Add(self._RedPlayer2)
        self.Controls.Add(self._RedPlayer1)
        self.Name = "MainForm"
        self.Text = "CheckersFinalProject"
        self.LocationChanged += self.MainFormLocationChanged
        self.ResumeLayout(False)


    def RedPlayer2LocationChanged(self, sender, e):
        if self._RedPlayer2.Location():
            Location == 108, 209
        if self._RedPlayer4.Location():
            Location == 108, 209 or Locaion == 308, 202
        if self._RedPlayer6.Location():
            Location == 308, 202 or Location == 505, 202
        if self._BlackPlayer2.Location():
            Location == 108, 209
        if self._BlackPlayer4.Location():
            Location == 108, 209 or Locaion == 308, 202
        if self._BlackPlayer6.Location():
            Location == 308, 202 or Location == 505, 202