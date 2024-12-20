import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self.SuspendLayout()
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Navy
        self.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self.ClientSize = System.Drawing.Size(843, 313)
        self.Name = "MainForm"
        self.Text = "favorite activity"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)