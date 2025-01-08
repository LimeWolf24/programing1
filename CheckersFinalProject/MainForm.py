import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        resources = System.Resources.ResourceManager("CheckersFinalProject.MainForm", System.Reflection.Assembly.GetEntryAssembly())
        self._Red1 = System.Windows.Forms.Label()
        self._Red2 = System.Windows.Forms.Label()
        self._Red3 = System.Windows.Forms.Label()
        self._Red4 = System.Windows.Forms.Label()
        self._Red5 = System.Windows.Forms.Label()
        self._Red6 = System.Windows.Forms.Label()
        self._Black1 = System.Windows.Forms.Label()
        self._Black2 = System.Windows.Forms.Label()
        self._Black3 = System.Windows.Forms.Label()
        self._Black4 = System.Windows.Forms.Label()
        self._Black5 = System.Windows.Forms.Label()
        self._Black6 = System.Windows.Forms.Label()
        self._RedPoints = System.Windows.Forms.Label()
        self._BlackPoints = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # Red1
        # 
        self._Red1.BackColor = System.Drawing.Color.Red
        self._Red1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Red1.Image = resources.GetObject("Red1.Image")
        self._Red1.Location = System.Drawing.Point(12, 108)
        self._Red1.Name = "Red1"
        self._Red1.Size = System.Drawing.Size(89, 98)
        self._Red1.TabIndex = 0
        self._Red1.Text = "1"
        self._Red1.Click += self.Red1Click
        # 
        # Red2
        # 
        self._Red2.BackColor = System.Drawing.Color.Red
        self._Red2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Red2.Image = resources.GetObject("Red2.Image")
        self._Red2.Location = System.Drawing.Point(109, 9)
        self._Red2.Name = "Red2"
        self._Red2.Size = System.Drawing.Size(89, 93)
        self._Red2.TabIndex = 1
        self._Red2.Text = "2"
        self._Red2.Click += self.Red2Click
        # 
        # Red3
        # 
        self._Red3.BackColor = System.Drawing.Color.Red
        self._Red3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Red3.Image = resources.GetObject("Red3.Image")
        self._Red3.Location = System.Drawing.Point(215, 107)
        self._Red3.Name = "Red3"
        self._Red3.Size = System.Drawing.Size(89, 98)
        self._Red3.TabIndex = 2
        self._Red3.Text = "3"
        self._Red3.Click += self.Red3Click
        # 
        # Red4
        # 
        self._Red4.BackColor = System.Drawing.Color.Red
        self._Red4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Red4.Image = resources.GetObject("Red4.Image")
        self._Red4.Location = System.Drawing.Point(310, 9)
        self._Red4.Name = "Red4"
        self._Red4.Size = System.Drawing.Size(89, 93)
        self._Red4.TabIndex = 3
        self._Red4.Text = "4"
        self._Red4.Click += self.Red4Click
        # 
        # Red5
        # 
        self._Red5.BackColor = System.Drawing.Color.Red
        self._Red5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Red5.Image = resources.GetObject("Red5.Image")
        self._Red5.Location = System.Drawing.Point(410, 108)
        self._Red5.Name = "Red5"
        self._Red5.Size = System.Drawing.Size(89, 98)
        self._Red5.TabIndex = 4
        self._Red5.Text = "5"
        self._Red5.Click += self.Red5Click
        # 
        # Red6
        # 
        self._Red6.BackColor = System.Drawing.Color.Red
        self._Red6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Red6.Image = resources.GetObject("Red6.Image")
        self._Red6.Location = System.Drawing.Point(506, 9)
        self._Red6.Name = "Red6"
        self._Red6.Size = System.Drawing.Size(89, 93)
        self._Red6.TabIndex = 5
        self._Red6.Text = "6"
        self._Red6.Click += self.Red6Click
        # 
        # Black1
        # 
        self._Black1.BackColor = System.Drawing.Color.Black
        self._Black1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Black1.Image = resources.GetObject("Black1.Image")
        self._Black1.Location = System.Drawing.Point(12, 304)
        self._Black1.Name = "Black1"
        self._Black1.Size = System.Drawing.Size(89, 87)
        self._Black1.TabIndex = 6
        self._Black1.Text = "1"
        self._Black1.Click += self.Black1Click
        # 
        # Black2
        # 
        self._Black2.BackColor = System.Drawing.Color.Black
        self._Black2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Black2.Image = resources.GetObject("Black2.Image")
        self._Black2.Location = System.Drawing.Point(109, 399)
        self._Black2.Name = "Black2"
        self._Black2.Size = System.Drawing.Size(89, 98)
        self._Black2.TabIndex = 7
        self._Black2.Text = "2"
        self._Black2.Click += self.Black2Click
        # 
        # Black3
        # 
        self._Black3.BackColor = System.Drawing.Color.Black
        self._Black3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Black3.Image = resources.GetObject("Black3.Image")
        self._Black3.Location = System.Drawing.Point(204, 304)
        self._Black3.Name = "Black3"
        self._Black3.Size = System.Drawing.Size(89, 94)
        self._Black3.TabIndex = 8
        self._Black3.Text = "3"
        self._Black3.Click += self.Black3Click
        # 
        # Black4
        # 
        self._Black4.BackColor = System.Drawing.Color.Black
        self._Black4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Black4.Image = resources.GetObject("Black4.Image")
        self._Black4.Location = System.Drawing.Point(310, 399)
        self._Black4.Name = "Black4"
        self._Black4.Size = System.Drawing.Size(89, 98)
        self._Black4.TabIndex = 9
        self._Black4.Text = "4"
        self._Black4.Click += self.Black4Click
        # 
        # Black5
        # 
        self._Black5.BackColor = System.Drawing.Color.Black
        self._Black5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Black5.Image = resources.GetObject("Black5.Image")
        self._Black5.Location = System.Drawing.Point(410, 304)
        self._Black5.Name = "Black5"
        self._Black5.Size = System.Drawing.Size(89, 87)
        self._Black5.TabIndex = 10
        self._Black5.Text = "5"
        self._Black5.Click += self.Black5Click
        # 
        # Black6
        # 
        self._Black6.BackColor = System.Drawing.Color.Black
        self._Black6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._Black6.Image = resources.GetObject("Black6.Image")
        self._Black6.Location = System.Drawing.Point(506, 399)
        self._Black6.Name = "Black6"
        self._Black6.Size = System.Drawing.Size(89, 98)
        self._Black6.TabIndex = 11
        self._Black6.Text = "6"
        self._Black6.Click += self.Black6Click
        # 
        # RedPoints
        # 
        self._RedPoints.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._RedPoints.ForeColor = System.Drawing.Color.Red
        self._RedPoints.Location = System.Drawing.Point(12, 9)
        self._RedPoints.Name = "RedPoints"
        self._RedPoints.Size = System.Drawing.Size(91, 93)
        self._RedPoints.TabIndex = 12
        self._RedPoints.Text = "0"
        self._RedPoints.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._RedPoints.Click += self.Label1Click
        # 
        # BlackPoints
        # 
        self._BlackPoints.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._BlackPoints.Location = System.Drawing.Point(10, 399)
        self._BlackPoints.Name = "BlackPoints"
        self._BlackPoints.Size = System.Drawing.Size(91, 88)
        self._BlackPoints.TabIndex = 13
        self._BlackPoints.Text = "0"
        self._BlackPoints.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._BlackPoints.Click += self.Label2Click
        # 
        # MainForm
        # 
        self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
        self.ClientSize = System.Drawing.Size(597, 496)
        self.Controls.Add(self._BlackPoints)
        self.Controls.Add(self._RedPoints)
        self.Controls.Add(self._Black6)
        self.Controls.Add(self._Black5)
        self.Controls.Add(self._Black4)
        self.Controls.Add(self._Black3)
        self.Controls.Add(self._Black2)
        self.Controls.Add(self._Black1)
        self.Controls.Add(self._Red6)
        self.Controls.Add(self._Red5)
        self.Controls.Add(self._Red4)
        self.Controls.Add(self._Red3)
        self.Controls.Add(self._Red2)
        self.Controls.Add(self._Red1)
        self.Name = "MainForm"
        self.Text = "CheckersFinalProject"
        self.Load += self.MainFormLoad
        self.MouseClick += self.MainFormMouseClick
        self.ResumeLayout(False)
            
    """TODO: I want to make it so the pieces don't show up until player clicks start
     I want the pieces to not be visable when they have been jumped by the other player"""
     
    """TODO: make the code for the pieces to move, and disapear when taken over"""

    def MainFormLoad(self, sender, e):
        pass
    
    

    def RedPointsClick(self, sender, e):
        pass 

    def BlackPointsClick(self, sender, e):
        pass

    def Red1Click(self, sender, e):
        if DragDrop Red1 over Black1:
             Black1.Visible = False
        if DragDrop Red1 over Black2:
             Black2.Visible = False
        if DragDrop Red1 over Black3:
             Black3.Visible = False
        if DragDrop Red1 over Black4:
             Black4.Visible = False
        if DragDrop Red1 over Black5:
             Black5.Visible = False
        if DragDrop Red1 over Black6:
             Black6.Visible = False
        
    def Red2Click(self, sender, e):
        if DragDrop Red2 over Black1:
             Black1.Visible = False
        if DragDrop Red2 over Black2:
             Black2.Visible = False
        if DragDrop Red2 over Black3:
             Black3.Visible = False
        if DragDrop Red2 over Black4:
             Black4.Visible = False
        if DragDrop Red2 over Black5:
             Black5.Visible = False
        if DragDrop Red2 over Black6:
             Black6.Visible = False

    def Red3Click(self, sender, e):
        if DragDrop Red3 over Black1:
             Black1.Visible = False
        if DragDrop Red3 over Black2:
             Black2.Visible = False
        if DragDrop Red3 over Black3:
             Black3.Visible = False
        if DragDrop Red3 over Black4:
             Black4.Visible = False
        if DragDrop Red3 over Black5:
             Black5.Visible = False
        if DragDrop Red3 over Black6:
             Black6.Visible = False

    def Red4Click(self, sender, e):
        if DragDrop Red4 over Black1:
             Black1.Visible = False
        if DragDrop Red4 over Black2:
             Black2.Visible = False
        if DragDrop Red4 over Black3:
             Black3.Visible = False
        if DragDrop Red4 over Black4:
             Black4.Visible = False
        if DragDrop Red4 over Black5:
             Black5.Visible = False
        if DragDrop Red4 over Black6:
             Black6.Visible = False

    def Red5Click(self, sender, e):
        if DragDrop Red5 over Black1:
             Black1.Visible = False
        if DragDrop Red5 over Black2:
             Black2.Visible = False
        if DragDrop Red5 over Black3:
             Black3.Visible = False
        if DragDrop Red5 over Black4:
             Black4.Visible = False
        if DragDrop Red5 over Black5:
             Black5.Visible = False
        if DragDrop Red5 over Black6:
             Black6.Visible = False

    def Red6Click(self, sender, e):
        if DragDrop Red6 over Black1:
             Black1.Visible = False
        if DragDrop Red6 over Black2:
             Black2.Visible = False
        if DragDrop Red6 over Black3:
             Black3.Visible = False
        if DragDrop Red6 over Black4:
             Black4.Visible = False
        if DragDrop Red6 over Black5:
             Black5.Visible = False
        if DragDrop Red6 over Black6:
             Black6.Visible = False

    def Black1Click(self, sender, e):
        if DragDrop Black1 over Red1:
             Red1.Visible = False
        if DragDrop Black1 over Red2:
             Red2.Visible = False
        if DragDrop Black1 over Red3:
             Red3.Visible = False
        if DragDrop Black1 over Red4:
             Red4.Visible = False
        if DragDrop Black1 over Red5:
             Red5.Visible = False
        if DragDrop Black1 over Red6:
             Red6.Visible = False

    def Black2Click(self, sender, e):
        if DragDrop Black2 over Red1:
             Red1.Visible = False
        if DragDrop Black2 over Red2:
             Red2.Visible = False
        if DragDrop Black2 over Red3:
             Red3.Visible = False
        if DragDrop Black2 over Red4:
             Red4.Visible = False
        if DragDrop Black2 over Red5:
             Red5.Visible = False
        if DragDrop Black2 over Red6:
             Red6.Visible = False

    def Black3Click(self, sender, e):
        if DragDrop Black3 over Red1:
             Red1.Visible = False
        if DragDrop Black3 over Red2:
             Red2.Visible = False
        if DragDrop Black3 over Red3:
             Red3.Visible = False
        if DragDrop Black3 over Red4:
             Red4.Visible = False
        if DragDrop Black3 over Red5:
             Red5.Visible = False
        if DragDrop Black3 over Red6:
             Red6.Visible = False

    def Black4Click(self, sender, e):
        if DragDrop Black4 over Red1:
             Red1.Visible = False
        if DragDrop Black4 over Red2:
             Red2.Visible = False
        if DragDrop Black4 over Red3:
             Red3.Visible = False
        if DragDrop Black4 over Red4:
             Red4.Visible = False
        if DragDrop Black4 over Red5:
             Red5.Visible = False
        if DragDrop Black4 over Red6:
             Red6.Visible = False

    def Black5Click(self, sender, e):
        if DragDrop Black5 over Red1:
             Red1.Visible = False
        if DragDrop Black5 over Red2:
             Red2.Visible = False
        if DragDrop Black5 over Red3:
             Red3.Visible = False
        if DragDrop Black5 over Red4:
             Red4.Visible = False
        if DragDrop Black5 over Red5:
             Red5.Visible = False
        if DragDrop Black5 over Red6:
             Red6.Visible = False

    def Black6Click(self, sender, e):
        if DragDrop Black6 over Red1:
             Red1.Visible = False
        if DragDrop Black6 over Red2:
             Red2.Visible = False
        if DragDrop Black6 over Red3:
             Red3.Visible = False
        if DragDrop Black6 over Red4:
             Red4.Visible = False
        if DragDrop Black6 over Red5:
             Red5.Visible = False
        if DragDrop Black6 over Red6:
             Red6.Visible = False