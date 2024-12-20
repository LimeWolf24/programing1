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
        self._label18 = System.Windows.Forms.Label()
        self._label19 = System.Windows.Forms.Label()
        self._label20 = System.Windows.Forms.Label()
        self._label21 = System.Windows.Forms.Label()
        self._label22 = System.Windows.Forms.Label()
        self._label23 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Gray
        self._button1.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._button1.Location = System.Drawing.Point(220, 404)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(114, 81)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Gray
        self._button2.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._button2.Location = System.Drawing.Point(340, 404)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(122, 81)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Gray
        self._button3.ForeColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self._button3.Location = System.Drawing.Point(286, 491)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(114, 84)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label18
        # 
        self._label18.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label18.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label18.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label18.Location = System.Drawing.Point(200, 11)
        self._label18.Name = "label18"
        self._label18.Size = System.Drawing.Size(105, 50)
        self._label18.TabIndex = 20
        self._label18.Text = "Sum:"
        self._label18.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label19
        # 
        self._label19.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label19.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label19.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label19.Location = System.Drawing.Point(200, 75)
        self._label19.Name = "label19"
        self._label19.Size = System.Drawing.Size(105, 50)
        self._label19.TabIndex = 21
        self._label19.Text = "Number of Scores:"
        self._label19.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label20
        # 
        self._label20.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label20.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label20.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label20.Location = System.Drawing.Point(200, 139)
        self._label20.Name = "label20"
        self._label20.Size = System.Drawing.Size(105, 50)
        self._label20.TabIndex = 22
        self._label20.Text = "Avrage:"
        self._label20.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label21
        # 
        self._label21.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label21.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label21.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label21.Location = System.Drawing.Point(311, 20)
        self._label21.Name = "label21"
        self._label21.Size = System.Drawing.Size(151, 32)
        self._label21.TabIndex = 23
        self._label21.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label22
        # 
        self._label22.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label22.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label22.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label22.Location = System.Drawing.Point(311, 84)
        self._label22.Name = "label22"
        self._label22.Size = System.Drawing.Size(151, 32)
        self._label22.TabIndex = 24
        self._label22.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label23
        # 
        self._label23.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label23.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label23.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label23.Location = System.Drawing.Point(311, 148)
        self._label23.Name = "label23"
        self._label23.Size = System.Drawing.Size(151, 32)
        self._label23.TabIndex = 25
        self._label23.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label13.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label13.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(7, 413)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(187, 32)
        self._label13.TabIndex = 15
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label14.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label14.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(7, 445)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(187, 32)
        self._label14.TabIndex = 16
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label15.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label15.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(7, 477)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(187, 32)
        self._label15.TabIndex = 17
        self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label16.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label16.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.Location = System.Drawing.Point(7, 509)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(187, 32)
        self._label16.TabIndex = 18
        self._label16.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label17.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label17.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label17.Location = System.Drawing.Point(7, 541)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(187, 32)
        self._label17.TabIndex = 19
        self._label17.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Navy
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(7, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(187, 52)
        self._label1.TabIndex = 0
        self._label1.Text = "Scores"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(7, 61)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(187, 32)
        self._label2.TabIndex = 1
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(7, 93)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(187, 32)
        self._label3.TabIndex = 5
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(7, 125)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(187, 32)
        self._label4.TabIndex = 6
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(7, 157)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(187, 32)
        self._label5.TabIndex = 7
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label6.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(7, 189)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(187, 32)
        self._label6.TabIndex = 8
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label7.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(7, 221)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(187, 32)
        self._label7.TabIndex = 9
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label8.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(7, 253)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(187, 32)
        self._label8.TabIndex = 10
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label9.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(7, 285)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(187, 32)
        self._label9.TabIndex = 11
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label10.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(7, 317)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(187, 32)
        self._label10.TabIndex = 12
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label11.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(7, 349)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(187, 32)
        self._label11.TabIndex = 13
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label12.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(7, 381)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(187, 32)
        self._label12.TabIndex = 14
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(474, 584)
        self.Controls.Add(self._label23)
        self.Controls.Add(self._label22)
        self.Controls.Add(self._label21)
        self.Controls.Add(self._label20)
        self.Controls.Add(self._label19)
        self.Controls.Add(self._label18)
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
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog155t"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label2.Text = (int)"12"
        self._label3.Text = (int)"73"
        self._label4.Text = (int)"84"
        self._label5.Text = (int)"95"
        self._label6.Text = (int)"100"
        self._label7.Text = (int)"88"
        self._label8.Text = (int)"77"
        self._label9.Text = (int)"85"
        self._label10.Text = (int)"88"
        self._label11.Text = (int)"62"
        self._label12.Text = (int)"91"
        self._label13.Text = (int)"87"
        self._label14.Text = (int)"70"
        self._label15.Text = (int)"63"
        self._label16.Text = (int)"89"
        self._label17.Text = (int)"98"
        sum = self._label18.Text = (int)"" 
        self._label18.Text = (int)"16"  
        
        
    def Button2Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        pass