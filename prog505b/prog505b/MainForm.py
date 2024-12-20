import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightCoral
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(6, 74)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(636, 58)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightCoral
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(6, 132)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(636, 58)
        self._label2.TabIndex = 1
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightCoral
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(6, 190)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(636, 58)
        self._label3.TabIndex = 2
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label3.Click += self.Label3Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Red
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(21, 266)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(107, 53)
        self._button1.TabIndex = 3
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Red
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(21, 319)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(107, 56)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Red
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(134, 266)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(126, 109)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightCoral
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(6, 9)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(636, 58)
        self._label4.TabIndex = 6
        self._label4.Text = "Student test grades, average test score and letter grade"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(654, 377)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog505b"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)


    def Label3Click(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label1.Text = "Sam Lilly: \t\t 80, \t\t 77, \t\t 82, \t\t 86, \t\t 90, \t\t\t\t 83 \t\t B"
        self._label2.Text = "Fred Biggie: \t\t 70, \t\t 72, \t\t 88, \t\t 90, \t\t 93, \t\t\t\t 82.6 \t\t B"
        self._label3.Text = "Sally Awsome: \t\t 92, \t\t 91, \t\t 86, \t\t 99, \t\t 93, \t\t\t\t 92 \t\t A"

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()