import random

class NeuroTestClass:
   LearningCurve = .05
   NumofArray = 0
   ChoosenButton = 0
   Buttons = []
   Weights = []
   FoundButtonCount = 0
   NoFoundButtonCount = 0

   def __init__(self, numofarray, learningcurve):
    self.LearningCurve = learningcurve
    self.NumofArray = numofarray
    self.AddToArray()
    self.Buttons[self.PickRandomArrayNumber()] = 1
    self.SetDefaultWeights()
    self.CheckWeights()
    
   def AddToArray(self):
    for x in range(self.NumofArray):
      self.Buttons.append(0)
      self.Weights.append(0)
   
   def SetDefaultWeights(self):
    TotalWeightings = 0
    for x in range(self.NumofArray):
      self.Weights[x] = round(1/self.NumofArray,2) * 100
      TotalWeightings += self.Weights[x] 
      '''print("Weights:")
      print(self.Weights[x])
      print(TotalWeightings)'''

   def CheckWeights(self):
    TotalWeight = 0
    MissingWeight = 0
    for x in range(self.NumofArray):
      TotalWeight += self.Weights[x]
    if TotalWeight != 100:
      MissingWeight = 100 - TotalWeight
      self.Weights[self.PickRandomArrayNumber()] += MissingWeight
      '''self.ShowWeightValues()'''
  
   def CheckMinMaxValues(self):
     for x in range(self.NumofArray):
       if self.Weights[x] > 100:
         self.Weights[x] = 100
       if self.Weights[x] < 0:
         self.Weights[x] = 0
      
   def PickRandomArrayNumber(self):
     return random.randint(0,self.NumofArray) -1

   def ShowWeightValues(self):
      print("Weightings: ")
      for x in range(self.NumofArray):
        print(self.Weights[x])
   def ShowTotalWeight(self):
     TotalWeight = 0;
     for x in range(self.NumofArray):
       TotalWeight += self.Weights[x] 
     print(TotalWeight)
   def ShowButtons(self):
      print("Showing right button: ")
      for x in range(self.NumofArray):
        print(self.Buttons[x])
        
   def ShowWinLoss(self):
      print("Wins:")
      print(self.FoundButtonCount)
      print("Lose:")
      print(self.NoFoundButtonCount)

   def SetButtonChances(self):
      test = 0
      for x in range(self.NumofArray):
        test += self.Weights[x]
      print(test)

   def ChooseButton(self):

    CalcNumber = 0
    ChoosenNumber = random.randint(1,100)

    '''This is just a quick check to see if which button the AI chooses. The for loop adds the number of weights then checks if it's the calculated number is more than the chosen number. if the number is more than the chosen number the program now which button is press by what x equals'''

    for x in range(self.NumofArray):
      CalcNumber += self.Weights[0]
      if ChoosenNumber <= CalcNumber:
        self.ChoosenButton = x
        '''print(ChoosenNumber)
        print(self.ChoosenButton)'''
        self.CheckRightButton()
        return
  
   def CheckRightButton(self):
    if self.Buttons[self.ChoosenButton] == 1:
      print("FoundButton")
      self.FoundButtonCount += 1
      self.Weights[self.ChoosenButton] += self.LearningCurve
    else:
      print("Button not found")
      self.NoFoundButtonCount += 1
      self.Weights[self.ChoosenButton] -= self.LearningCurve
    self.CheckMinMaxValues()
    self.CheckWeights()
       
    


Testing = NeuroTestClass(4, 3)
for x in range(100):
  Testing.ChooseButton()
  Testing.ShowTotalWeight()

Testing.ShowWeightValues()
Testing.ShowButtons()
Testing.ShowWinLoss()

