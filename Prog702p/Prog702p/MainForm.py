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
        self._label16 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MistyRose
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(8, 24)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(181, 41)
        self._label1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.RosyBrown
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(396, 24)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(99, 64)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.RosyBrown
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(396, 94)
        self._button2.Name = "button2"
        self._button2.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._button2.Size = System.Drawing.Size(99, 64)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.RosyBrown
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(396, 166)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(99, 64)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MistyRose
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(195, 315)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(138, 128)
        self._label2.TabIndex = 4
        self._label2.Text = "The total animals is 15. The sum of all the fur is: $18.35. The number of words spoken in total is 29. The total number of steps is 316."
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MistyRose
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(8, 65)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(181, 41)
        self._label3.TabIndex = 5
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.MistyRose
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(8, 106)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(181, 41)
        self._label4.TabIndex = 6
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MistyRose
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(8, 147)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(181, 41)
        self._label5.TabIndex = 7
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.MistyRose
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(8, 188)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(181, 41)
        self._label6.TabIndex = 8
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.MistyRose
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label7.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(8, 229)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(181, 41)
        self._label7.TabIndex = 9
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.MistyRose
        self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label8.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(8, 270)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(181, 41)
        self._label8.TabIndex = 10
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.MistyRose
        self._label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label9.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(8, 311)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(181, 41)
        self._label9.TabIndex = 11
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.MistyRose
        self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label10.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(195, 24)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(181, 41)
        self._label10.TabIndex = 12
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.MistyRose
        self._label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label11.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(195, 65)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(181, 41)
        self._label11.TabIndex = 13
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.MistyRose
        self._label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label12.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(195, 106)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(181, 41)
        self._label12.TabIndex = 14
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.MistyRose
        self._label13.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label13.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(195, 147)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(181, 41)
        self._label13.TabIndex = 15
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.MistyRose
        self._label14.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label14.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(195, 186)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(181, 41)
        self._label14.TabIndex = 16
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.MistyRose
        self._label15.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label15.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(195, 227)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(181, 41)
        self._label15.TabIndex = 17
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.MistyRose
        self._label16.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label16.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.Location = System.Drawing.Point(195, 268)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(181, 41)
        self._label16.TabIndex = 18
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.Color.MistyRose
        self._label17.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label17.Font = System.Drawing.Font("Microsoft YaHei", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label17.Location = System.Drawing.Point(339, 315)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(138, 118)
        self._label17.TabIndex = 19
        self._label17.Text = "The average value for fur = $3.06. The average number of steps taken = 63.2 The average number of words spoken = 7.25"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightCoral
        self.ClientSize = System.Drawing.Size(507, 447)
        self.Controls.Add(self._label17)
        self.Controls.Add(self._label16)
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
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog702p"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Billy Buckner: $3.25"
        self._label3.Text = "Fred Ballony: 28.0 steps"
        self._label4.Text = "Nick Cuccia: Coolbeans"
        self._label5.Text = "Murray Cox: $4.0"
        self._label6.Text = "Carly Seifert: $2.58"
        self._label7.Text = "Elias Smith: $3.22"
        self._label8.Text = "Katy Rumberger: 45.0 steps"
        self._label9.Text = "Tanya Barton: 78.0 steps"
        self._label10.Text = "Casey Bats: 97.0 steps"
        self._label11.Text = "Brandon Davis: 68.0 steps"
        self._label12.Text = "Ingrid Sink: Superdude"
        self._label13.Text = "Nico Binge: Attaway"
        self._label14.Text = "Mike Break: Done"
        self._label15.Text = "Brad Williamson: $2.75"
        self._label16.Text = "Lorenzo Rapp: $2.55"

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""
        self._label9.Text = ""
        self._label10.Text = ""
        self._label11.Text = ""
        self._label12.Text = ""
        self._label13.Text = ""
        self._label14.Text = ""
        self._label15.Text = ""
        self._label16.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()