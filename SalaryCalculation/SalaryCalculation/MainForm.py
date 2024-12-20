import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.MistyRose
        self._textBox1.Location = System.Drawing.Point(163, 31)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(316, 33)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.MistyRose
        self._textBox2.Location = System.Drawing.Point(163, 92)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(316, 33)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkGray
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.MistyRose
        self._label1.Location = System.Drawing.Point(12, 31)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(139, 42)
        self._label1.TabIndex = 3
        self._label1.Text = "Anual Salary"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkGray
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.MistyRose
        self._label2.Location = System.Drawing.Point(12, 92)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(139, 42)
        self._label2.TabIndex = 4
        self._label2.Text = "Pay Periods Per Year"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkGray
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft Tai Le", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.MistyRose
        self._label3.Location = System.Drawing.Point(12, 150)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(139, 42)
        self._label3.TabIndex = 5
        self._label3.Text = "Salary Per pay Period"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.WindowFrame
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.RosyBrown
        self._label4.Location = System.Drawing.Point(163, 150)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(316, 42)
        self._label4.TabIndex = 6
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightGray
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Red
        self._button1.Location = System.Drawing.Point(134, 223)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(227, 59)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(509, 296)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "SalaryCalculation"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        decAnualSalary = 0.0
        intPayPeriods = 0
        decSalary = 0
        
        decAnualSalary = float(self._textBox1.Text)
        intPayPeriods = float(self._textBox2.Text)
        decSalary = decAnualSalary / intPayPeriods
        self._label4.Text = str(round(decSalary, 2))
        