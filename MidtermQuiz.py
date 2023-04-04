class TempConversion():
  def __init__(self, temp):
    self.__temp = temp

  def FtoC(self):
    return (self.__temp-32)*5/9
  def KtoC(self):
    return self.__temp-273.15
  def CtoF(self):
    return (self.__temp*9/5)+32
  def KtoF(self):
    return ((1.8*self.__temp)-459.67)
  def CtoK(self):
    return self.__temp+273.15
  def FtoK(self):
    return ((self.__temp+459.67)/1.8)


temp = int(input("input temperature:"))
tempconversion = TempConversion(temp)
print(f"The value of the temperature from Fahrenheit to Celsius is {tempconversion.FtoC()}")
print(f"The value of the temperature from Kelvin to Celsius is {tempconversion.KtoC()}")
print(f"The value of the temperature from Celsius to Fahrenheit is {tempconversion.CtoF()}")
print(f"The value of the temperature from Kelvin to Fahrenheit is {tempconversion.KtoF()}")
print(f"The value of the temperature from Celsius to Kelvin is {tempconversion.CtoK()}")
print(f"The value of the temperature from Fahrenheit to Kelvin is {tempconversion.FtoK()}")
