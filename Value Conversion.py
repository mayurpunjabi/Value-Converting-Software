from wx import *

class MainWindow(Dialog):
    def __init__(self, parent, id):
        Dialog.__init__(self, parent, id, 'Value Convertion', pos=(458,259), size=(450,250))
        self.panel = Panel(self)

        self.pre1 = ''
        self.pre2 = ''
        
        self.button = Button(self.panel, label="Numbers", pos=(30,16), size=(75,30))
        self.Bind(EVT_BUTTON, self.NumberBox, self.button)
        
        self.button = Button(self.panel, label="Length", pos=(135,16), size=(75,30))
        self.Bind(EVT_BUTTON, self.LengthBox, self.button)
        
        self.button = Button(self.panel, label="Mass", pos=(240,16), size=(75,30))
        self.Bind(EVT_BUTTON, self.MassBox, self.button)
        
        self.button = Button(self.panel, label="Temperature", pos=(345,16), size=(75,30))
        self.Bind(EVT_BUTTON, self.TemperatureBox, self.button)

        self.text1 = StaticText(self.panel, -1, 'Decimal:', (17,77))
        self.TextBox1 = TextCtrl(self.panel, -1, pos=(17,94), size=(416,-1))
        self.Text1 = 'Decimal:'
        
        arrow = Image('arrow.bmp', BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button1 = BitmapButton(self.panel, -1, arrow, pos=(200,120))
        self.Bind(EVT_BUTTON, self.Convert, self.button1)
        
        self.text2 = StaticText(self.panel, -1, 'Binary:', (17,147))
        self.TextBox2 = TextCtrl(self.panel, -1, pos=(17,165), size=(416,-1))
        self.Text2 = 'Binary:'
       
    def NumberBox(self, event):
        Numbers = ['Decimal To Binary', 'Decimal To Octal', 'Decimal To Hexadecimal', 'Binary To Octal', 'Binary To Hexadecimal', 'Octal To Hexadecimal']
        box = SingleChoiceDialog(None, "Select", "", Numbers)
        box.SetSelection(0)
        if box.ShowModal()==ID_OK:
            self.Units = box.GetStringSelection()
            self.ChangeUnits()
        box.Destroy()

    def LengthBox(self, event):
        Numbers = ['cm To inch', 'cm To foot', 'cm To yard', 'cm To mile', 'foot To yard', 'foot To mile', 'yard To mile']
        box = SingleChoiceDialog(None, "Select", "", Numbers)
        box.SetSelection(0)
        if box.ShowModal()==ID_OK:
            self.Units = box.GetStringSelection()
            self.ChangeUnits()
        box.Destroy()

    def MassBox(self, event):
        Numbers = ['Pound To Kilogram', 'Kilogram To Stone', 'Tonne To Kilogram', 'Ounce To Kilogram', 'Pound To Stone']
        box = SingleChoiceDialog(None, "Select", "", Numbers)
        box.SetSelection(0)
        if box.ShowModal()==ID_OK:
            self.Units = box.GetStringSelection()
            self.ChangeUnits()
        box.Destroy()

    def TemperatureBox(self, event):
        Numbers = ['Celsius To Fahrenheit', 'Celsius To Kelvin', 'Kelvin To Fahrenheit']
        box = SingleChoiceDialog(None, "Select", "", Numbers)
        box.SetSelection(0)
        if box.ShowModal()==ID_OK:
            self.Units = box.GetStringSelection()
            self.ChangeUnits()
        box.Destroy()

    def ChangeUnits(self):
        self.text1.Destroy()
        self.text2.Destroy()
        self.TextBox1.SetValue('')
        self.TextBox2.SetValue('')
        self.pre1=''
        self.pre2=''
        if self.Units == 'Decimal To Binary':
            self.text1 = StaticText(self.panel, -1, 'Decimal:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Binary:', (17,147))
            self.Text1 = 'Decimal:'
            self.Text2 = 'Binary:'

        elif self.Units == 'Decimal To Octal':
            self.text1 = StaticText(self.panel, -1, 'Decimal:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Octal:', (17,147))
            self.Text1 = 'Decimal:'
            self.Text2 = 'Octal:'

        elif self.Units == 'Decimal To Hexadecimal':
            self.text1 = StaticText(self.panel, -1, 'Decimal:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Hexadecimal:', (17,147))
            self.Text1 = 'Decimal:'
            self.Text2 = 'Hexadecimal:'
           
        elif self.Units == 'Binary To Octal':
            self.text1 = StaticText(self.panel, -1, 'Binary:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Octal:', (17,147))
            self.Text1 = 'Binary:'
            self.Text2 = 'Octal:'
           
        elif self.Units == 'Binary To Hexadecimal':
            self.text1 = StaticText(self.panel, -1, 'Binary:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Hexadecimal:', (17,147))
            self.Text1 = 'Binary:'
            self.Text2 = 'Hexadecimal:'

        elif self.Units == 'Octal To Hexadecimal':
            self.text1 = StaticText(self.panel, -1, 'Octal:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Hexadecimal:', (17,147))
            self.Text1 = 'Octal:'
            self.Text2 = 'Hexadecimal:'
           
        elif self.Units == 'cm To inch':
            self.text1 = StaticText(self.panel, -1, 'cm:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'inch:', (17,147))
            self.Text1 = 'cm:'
            self.Text2 = 'inch:'
           
        elif self.Units == 'cm To foot':
            self.text1 = StaticText(self.panel, -1, 'cm:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'foot:', (17,147))
            self.Text1 = 'cm:'
            self.Text2 = 'foot:'
           
        elif self.Units == 'cm To yard':
            self.text1 = StaticText(self.panel, -1, 'cm:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'yard:', (17,147))
            self.Text1 = 'cm:'
            self.Text2 = 'yard:'
           
        elif self.Units == 'cm To mile':
            self.text1 = StaticText(self.panel, -1, 'cm:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'mile:', (17,147))
            self.Text1 = 'cm:'
            self.Text2 = 'mile:'
           
        elif self.Units == 'foot To yard':
            self.text1 = StaticText(self.panel, -1, 'foot:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'yard:', (17,147))
            self.Text2 = 'foot:'
            self.Text2 = 'yard:'
            
        elif self.Units == 'foot To mile':
            self.text1 = StaticText(self.panel, -1, 'foot:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'mile:', (17,147))
            self.Text1 = 'yard:'
            self.Text2 = 'mile:'
           
        elif self.Units == 'yard To mile':
            self.text1 = StaticText(self.panel, -1, 'yard:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'mile:', (17,147))
            self.Text1 = 'yard:'
            self.Text2 = 'mile:'
           
        elif self.Units == 'Pound To Kilogram':
            self.text1 = StaticText(self.panel, -1, 'Pound:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Kilogram:', (17,147))
            self.Text1 = 'Pound:'
            self.Text2 = 'Kilogram:'
           
        elif self.Units == 'Kilogram To Stone':
            self.text1 = StaticText(self.panel, -1, 'Kilogram:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Stone:', (17,147))
            self.Text1 = 'Kilogram:'
            self.Text2 = 'Stone:'
           
        elif self.Units == 'Tonne To Kilogram':
            self.text1 = StaticText(self.panel, -1, 'Tonne:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Kilogram:', (17,147))
            self.Text1 = 'Tonne:'
            self.Text2 = 'Kilogram:'
           
        elif self.Units == 'Ounce To Kilogram':
            self.text1 = StaticText(self.panel, -1, 'Ounce:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Kilogram:', (17,147))
            self.Text1 = 'Ounce:'
            self.Text2 = 'Kilogram:'
           
        elif self.Units == 'Pound To Stone':
            self.text1 = StaticText(self.panel, -1, 'Pound:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Stone:', (17,147))
            self.Text1 = 'Pound:'
            self.Text2 = 'Stone:'
           
        elif self.Units == 'Celsius To Fahrenheit':
            self.text1 = StaticText(self.panel, -1, 'Celsius:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Fahrenheit:', (17,147))
            self.Text1 = 'Celsius:'
            self.Text2 = 'Fahrenheit:'
           
        elif self.Units == 'Celsius To Kelvin':
            self.text1 = StaticText(self.panel, -1, 'Celsius:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Kelvin:', (17,147))
            self.Text1 = 'Celsius:'
            self.Text2 = 'Kelvin:'
           
        elif self.Units == 'Kelvin To Fahrenheit':
            self.text1 = StaticText(self.panel, -1, 'Kelvin:', (17,77))
            self.text2 = StaticText(self.panel, -1, 'Fahrenheit:', (17,147))
            self.Text1 = 'Kelvin:'
            self.Text2 = 'Fahrenheit:'
               
    def Convert(self, event):
        if self.TextBox1.GetValue() != '' and self.TextBox1.GetValue() != self.pre1:
            if self.Text1=='Binary:':
                if 'b' in self.TextBox1.GetValue():
                    con1 = -int(self.TextBox1.GetValue()[1:], 2)
                else:
                    con1 = int(self.TextBox1.GetValue(), 2)
            elif self.Text1=='Decimal:':
                con1 = int(self.TextBox1.GetValue())
            elif self.Text1=='Octal:':
                if 'o' in self.TextBox1.GetValue():
                    con1 = -int(self.TextBox1.GetValue(), 8)
                else:
                    con1 = int(self.TextBox1.GetValue(), 8)
            elif self.Text1=='cm:':
                con1 = float(self.TextBox1.GetValue())
            elif self.Text1=='foot:':
                con1 = float(self.TextBox1.GetValue())*30.48
            elif self.Text1=='yard:':
                con1 = float(self.TextBox1.GetValue())*91.44
            elif self.Text1=='Kilogram:':
                con1 = float(self.TextBox1.GetValue())
            elif self.Text1=='Pound:':
                con1 = float(self.TextBox1.GetValue())*0.453592
            elif self.Text1=='Tonne:':
                con1 = float(self.TextBox1.GetValue())*1000
            elif self.Text1=='Ounce:':
                con1 = float(self.TextBox1.GetValue())*0.0283495
            elif self.Text1=='Celsius:':
                con1 = float(self.TextBox1.GetValue())
            elif self.Text1=='Kelvin:':
                con1 = float(self.TextBox1.GetValue()) - 273.15
                
            if self.Text2=='Binary:':
                con2 = bin(con1)[2:]
            elif self.Text2=='Octal:':
                con2 = oct(con1)[2:]
            elif self.Text2=='Hexadecimal:':
                con2 = hex(con1)[2:]
            elif self.Text2=='inch:':
                con2 = str(con1*0.393701)
            elif self.Text2=='foot:':
                con2 = str(con1*0.0328084)
            elif self.Text2=='yard:':
                con2 = str(con1*0.0109361)
            elif self.Text2=='mile:':
                con2 = str(con1*0.00000621371)
            elif self.Text2=='Kilogram:':
                con2 = str(con1)
            elif self.Text2=='Stone:':
                con2 = str(con1*0.157473)
            elif self.Text2=='Fahrenheit:':
                con2 = str(con1*1.8+32)
            elif self.Text2=='Kelvin:':
                con2 = str(con1+273.15)

            self.TextBox2.SetValue(con2)

        elif self.TextBox2.GetValue() != ''  and self.TextBox2.GetValue() != self.pre2:
            if self.Text2=='Binary:':
                if 'b' in self.TextBox2.GetValue():
                    con1 = -int(self.TextBox2.GetValue()[1:], 2)
                else:
                    con1 = int(self.TextBox2.GetValue(), 2)
            elif self.Text2=='Octal:':
                if 'o' in self.TextBox2.GetValue():
                    con1 = -int(self.TextBox2.GetValue()[1:], 8)
                else:
                    con1 = int(self.TextBox2.GetValue(), 8)
            elif self.Text2=='Hexadecimal:':
                if 'x' in self.TextBox2.GetValue():
                    con1 = -int(self.TextBox2.GetValue()[1:], 16)
                else:
                    con1 = int(self.TextBox2.GetValue(), 16)
            elif self.Text2=='inch:':
                con1 = float(self.TextBox2.GetValue())*2.54
            elif self.Text2=='foot:':
                con1 = float(self.TextBox2.GetValue())*30.48
            elif self.Text2=='yard:':
                con1 = float(self.TextBox2.GetValue())*91.44
            elif self.Text2=='mile:':
                con1 = float(self.TextBox2.GetValue())*160934
            elif self.Text2=='Kilogram:':
                con1 = float(self.TextBox2.GetValue())
            elif self.Text2=='Stone:':
                con1 = float(self.TextBox2.GetValue())*6.35029
            elif self.Text2=='Fahrenheit:':
                con1 = (float(self.TextBox2.GetValue())-32)/1.8
            elif self.Text2=='Kelvin:':
                con1 = float(self.TextBox2.GetValue())-273.15

            if self.Text1=='Binary:':
                con2 = bin(con1)[2:]
            elif self.Text1=='Decimal:':
                con2 = str(con1)
            elif self.Text1=='Octal:':
                con2 = oct(con1, 8)
            elif self.Text1=='cm:':
                con2 = str(con1)
            elif self.Text1=='foot:':
                con2 = str(con1*0.0328084)
            elif self.Text1=='yard:':
                con2 = str(con1*0.0109361)
            elif self.Text1=='Kilogram:':
                con2 = str(con1)
            elif self.Text1=='Pound:':
                con2 = str(con1*2.20462)
            elif self.Text1=='Tonne:':
                con2 = str(con1*0.001)
            elif self.Text1=='Ounce:':
                con2 = str(con1*35.274)
            elif self.Text1=='Celsius:':
                con2 = str(con1)
            elif self.Text1=='Kelvin:':
                con2 = str(con1 + 273.15)

            self.TextBox1.SetValue(con2)

        self.pre1 = self.TextBox1.GetValue()
        self.pre2 = self.TextBox2.GetValue()
        
if __name__=='__main__':
    app = App()
    frame = MainWindow(parent = None, id = -1)
    frame.Show()
    app.MainLoop()

