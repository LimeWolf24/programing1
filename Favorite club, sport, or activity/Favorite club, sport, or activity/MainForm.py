import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        resources = System.Resources.ResourceManager("Favorite_club__sport__or_activity.MainForm", System.Reflection.Assembly.GetEntryAssembly())
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # 
        self._label1.BackColor = System.Drawing.Color.Maroon
        self._label1.Font = System.Drawing.Font("Modern No. 20", 23.9999981, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(242, 28)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(584, 225)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Maroon
        self._button1.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(252, 265)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(135, 41)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Maroon
        self._button2.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(432, 265)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(140, 40)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Navy
        self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
        self.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self.ClientSize = System.Drawing.Size(843, 313)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "favorite activity"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "I enjoy reading books while listening to music."

    def Button2Click(self, sender, e):
        self._label1.Text = ""