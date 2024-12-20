import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Salmon
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(92, 11)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(229, 55)
        self._label1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Salmon
        self._button1.Location = System.Drawing.Point(703, 9)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(132, 72)
        self._button1.TabIndex = 8
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Salmon
        self._button2.Location = System.Drawing.Point(703, 112)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(132, 72)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Salmon
        self._button3.Location = System.Drawing.Point(703, 213)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(132, 72)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(14, 20)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(37, 32)
        self._label9.TabIndex = 11
        self._label9.Text = "1."
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(14, 84)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(37, 32)
        self._label10.TabIndex = 12
        self._label10.Text = "2."
        # 
        # label11
        # 
        self._label11.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(14, 152)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(37, 32)
        self._label11.TabIndex = 13
        self._label11.Text = "3."
        # 
        # label12
        # 
        self._label12.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(14, 225)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(37, 32)
        self._label12.TabIndex = 14
        self._label12.Text = "4."
        # 
        # label13
        # 
        self._label13.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(376, 20)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(37, 32)
        self._label13.TabIndex = 15
        self._label13.Text = "5."
        # 
        # label14
        # 
        self._label14.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(376, 84)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(37, 32)
        self._label14.TabIndex = 16
        self._label14.Text = "6."
        # 
        # label15
        # 
        self._label15.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(376, 152)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(37, 32)
        self._label15.TabIndex = 17
        self._label15.Text = "7."
        # 
        # label16
        # 
        self._label16.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.Location = System.Drawing.Point(376, 225)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(37, 32)
        self._label16.TabIndex = 18
        self._label16.Text = "8."
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Salmon
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(92, 75)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(229, 55)
        self._label2.TabIndex = 19
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Salmon
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(92, 141)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(229, 55)
        self._label3.TabIndex = 20
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Salmon
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(92, 213)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(229, 55)
        self._label4.TabIndex = 21
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Salmon
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(433, 9)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(229, 55)
        self._label5.TabIndex = 22
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Salmon
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(433, 75)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(229, 55)
        self._label6.TabIndex = 23
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Salmon
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label7.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(433, 141)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(229, 55)
        self._label7.TabIndex = 24
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Salmon
        self._label8.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label8.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(433, 213)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(229, 55)
        self._label8.TabIndex = 25
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Coral
        self.ClientSize = System.Drawing.Size(862, 369)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Schedule"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Construction and Woodworking 1"
        self._label2.Text = "Computer Programing 1"
        self._label3.Text = "Alegebra 1"
        self._label4.Text = "Biology"
        self._label5.Text = "English 9 Honors"
        self._label6.Text = "World Studies"
        self._label7.Text = "Culinary Arts 1"
        self._label8.Text = "Freshman Seminar"

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()