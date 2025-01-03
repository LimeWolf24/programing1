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
        self.SuspendLayout()
        # 
        # RedPlayer1
        # 
        self._RedPlayer1.BackColor = System.Drawing.Color.Red
        self._RedPlayer1.Location = System.Drawing.Point(27, 31)
        self._RedPlayer1.Name = "RedPlayer1"
        self._RedPlayer1.Size = System.Drawing.Size(55, 44)
        self._RedPlayer1.TabIndex = 0
        self._RedPlayer1.Text = "1"
        self._RedPlayer1.Click += self.RedPlayer1Click
        # 
        # RedPlayer2
        # 
        self._RedPlayer2.BackColor = System.Drawing.Color.Red
        self._RedPlayer2.Location = System.Drawing.Point(128, 135)
        self._RedPlayer2.Name = "RedPlayer2"
        self._RedPlayer2.Size = System.Drawing.Size(55, 44)
        self._RedPlayer2.TabIndex = 1
        self._RedPlayer2.Text = "2"
        self._RedPlayer2.Click += self.RedPlayer2Click
        # 
        # RedPlayer3
        # 
        self._RedPlayer3.BackColor = System.Drawing.Color.Red
        self._RedPlayer3.Location = System.Drawing.Point(226, 31)
        self._RedPlayer3.Name = "RedPlayer3"
        self._RedPlayer3.Size = System.Drawing.Size(55, 44)
        self._RedPlayer3.TabIndex = 2
        self._RedPlayer3.Text = "3"
        self._RedPlayer3.Click += self.RedPlayer3Click
        # 
        # RedPlayer4
        # 
        self._RedPlayer4.BackColor = System.Drawing.Color.Red
        self._RedPlayer4.Location = System.Drawing.Point(321, 135)
        self._RedPlayer4.Name = "RedPlayer4"
        self._RedPlayer4.Size = System.Drawing.Size(55, 44)
        self._RedPlayer4.TabIndex = 3
        self._RedPlayer4.Text = "4"
        self._RedPlayer4.Click += self.RedPlayer4Click
        # 
        # RedPlayer5
        # 
        self._RedPlayer5.BackColor = System.Drawing.Color.Red
        self._RedPlayer5.Location = System.Drawing.Point(424, 31)
        self._RedPlayer5.Name = "RedPlayer5"
        self._RedPlayer5.Size = System.Drawing.Size(55, 44)
        self._RedPlayer5.TabIndex = 4
        self._RedPlayer5.Text = "5"
        self._RedPlayer5.Click += self.RedPlayer5Click
        # 
        # RedPlayer6
        # 
        self._RedPlayer6.BackColor = System.Drawing.Color.Red
        self._RedPlayer6.Location = System.Drawing.Point(531, 135)
        self._RedPlayer6.Name = "RedPlayer6"
        self._RedPlayer6.Size = System.Drawing.Size(55, 44)
        self._RedPlayer6.TabIndex = 5
        self._RedPlayer6.Text = "6"
        self._RedPlayer6.Click += self.RedPlayer6Click
        # 
        # BlackPlayer1
        # 
        self._BlackPlayer1.BackColor = System.Drawing.Color.Black
        self._BlackPlayer1.ForeColor = System.Drawing.Color.White
        self._BlackPlayer1.Location = System.Drawing.Point(27, 427)
        self._BlackPlayer1.Name = "BlackPlayer1"
        self._BlackPlayer1.Size = System.Drawing.Size(55, 44)
        self._BlackPlayer1.TabIndex = 6
        self._BlackPlayer1.Text = "1"
        self._BlackPlayer1.Click += self.BlackPlayer1Click
        # 
        # BlackPlayer2
        # 
        self._BlackPlayer2.BackColor = System.Drawing.Color.Black
        self._BlackPlayer2.ForeColor = System.Drawing.Color.White
        self._BlackPlayer2.Location = System.Drawing.Point(128, 330)
        self._BlackPlayer2.Name = "BlackPlayer2"
        self._BlackPlayer2.Size = System.Drawing.Size(55, 44)
        self._BlackPlayer2.TabIndex = 7
        self._BlackPlayer2.Text = "2"
        self._BlackPlayer2.Click += self.BlackPlayer2Click
        # 
        # BlackPlayer3
        # 
        self._BlackPlayer3.BackColor = System.Drawing.Color.Black
        self._BlackPlayer3.ForeColor = System.Drawing.Color.White
        self._BlackPlayer3.Location = System.Drawing.Point(226, 427)
        self._BlackPlayer3.Name = "BlackPlayer3"
        self._BlackPlayer3.Size = System.Drawing.Size(55, 44)
        self._BlackPlayer3.TabIndex = 8
        self._BlackPlayer3.Text = "3"
        self._BlackPlayer3.Click += self.BlackPlayer3Click
        # 
        # BlackPlayer4
        # 
        self._BlackPlayer4.BackColor = System.Drawing.Color.Black
        self._BlackPlayer4.ForeColor = System.Drawing.Color.White
        self._BlackPlayer4.Location = System.Drawing.Point(321, 330)
        self._BlackPlayer4.Name = "BlackPlayer4"
        self._BlackPlayer4.Size = System.Drawing.Size(55, 44)
        self._BlackPlayer4.TabIndex = 9
        self._BlackPlayer4.Text = "4"
        self._BlackPlayer4.Click += self.BlackPlayer4Click
        # 
        # BlackPlayer5
        # 
        self._BlackPlayer5.BackColor = System.Drawing.Color.Black
        self._BlackPlayer5.ForeColor = System.Drawing.Color.White
        self._BlackPlayer5.Location = System.Drawing.Point(424, 427)
        self._BlackPlayer5.Name = "BlackPlayer5"
        self._BlackPlayer5.Size = System.Drawing.Size(55, 44)
        self._BlackPlayer5.TabIndex = 10
        self._BlackPlayer5.Text = "5"
        # 
        # BlackPlayer6
        # 
        self._BlackPlayer6.BackColor = System.Drawing.Color.Black
        self._BlackPlayer6.ForeColor = System.Drawing.Color.White
        self._BlackPlayer6.Location = System.Drawing.Point(531, 330)
        self._BlackPlayer6.Name = "BlackPlayer6"
        self._BlackPlayer6.Size = System.Drawing.Size(55, 44)
        self._BlackPlayer6.TabIndex = 11
        self._BlackPlayer6.Text = "6"
        # 
        # MainForm
        # 
        self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
        self.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self.ClientSize = System.Drawing.Size(603, 493)
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
        self.ResumeLayout(False)


    def RedPlayer1Click(self, sender, e):
        pass

    def RedPlayer2Click(self, sender, e):
        pass

    def RedPlayer3Click(self, sender, e):
        pass

    def RedPlayer4Click(self, sender, e):
        pass

    def RedPlayer5Click(self, sender, e):
        pass

    def RedPlayer6Click(self, sender, e):
        pass

    def BlackPlayer1Click(self, sender, e):
        pass

    def BlackPlayer2Click(self, sender, e):
        pass

    def BlackPlayer3Click(self, sender, e):
        pass

    def BlackPlayer4Click(self, sender, e):
        pass