import random

class NeuroTestClass:
   LearningCurve = .05
   NumofArray = 0
   ChoosenButton = 0
   Buttons = []
   Weights = []
   FoundButtonCount = 0
   NoFoundButtonCount = 0
   ButtonNotPressed = 0
   CompletedRuns = 0

   def __init__(self, numofarray, learningcurve):
    self.LearningCurve = learningcurve
    self.NumofArray = numofarray
    self.AddToArray()
    self.Buttons[self.PickRandomArrayNumber()] = 1
    self.SetDefaultWeights()
    
   def AddToArray(self):
    for x in range(self.NumofArray):
      self.Buttons.append(0)
      self.Weights.append(0)
   
   def SetDefaultWeights(self):
    TotalWeightings = 0
    for x in range(self.NumofArray):
      self.Weights[x] = round(1/self.NumofArray,2) * 100
      TotalWeightings += self.Weights[x] 
    self.CheckWeights()

   def CheckWeights(self):
    TotalWeight = 0
    MissingWeight = 0
    for x in range(self.NumofArray):
      TotalWeight += self.Weights[x]
    if TotalWeight != 100:
      MissingWeight = 100 - TotalWeight
      self.Weights[self.PickRandomArrayNumber()] += MissingWeight
      self.CheckWeights()
  
   def CheckMinMaxValues(self):
     WeightDiffrence = 0;
     for x in range(self.NumofArray):
       if self.Weights[x] > 100:
         WeightDiffrence = self.Weights[x] - 100
         self.Weights[x] = 100
       if self.Weights[x] < 0:
         self.Weights[x] = 0
     self.AddWeight(WeightDiffrence)
     
   def CheckIfEqual(self):
    WeightsEqual = 1
    BaseWeight = 0;
    for x in range(self.NumofArray):
      BaseWeight = self.Weights[0]
      if self.Weights[x] != BaseWeight:
        WeightsEqual = 0
    return WeightsEqual

   def PickRandomArrayNumber(self):
     return random.randint(0,self.NumofArray) -1

   def ShowWeightValues(self):
      TotalWeight = 0
      print("\nWeights: ")
      for x in range(self.NumofArray):
        TotalWeight += self.Weights[x]
        print(self.Weights[x])
      print("Total Weight: " + str(TotalWeight))

   def ShowButtons(self):
      for x in range(self.NumofArray):
        if self.Buttons[x] == 1:
          print("Right button: " + str(self.Buttons[x]))

   def ShowCompletedRuns(self):
     print(self.CompletedRuns)

   def ShowWinLoss(self):
      print("\n\nResults: \n")
      print("Wins: " + str(self.FoundButtonCount))
      print("Lose: " + str(self.NoFoundButtonCount))
      print("AI Forgot to press button: " + str(self.ButtonNotPressed))
   
   def TryNextOne(self):
     input("Press enter:")

   def GetTotalWeight(self):
    TotalWeight = 0;
    for x in range(self.NumofArray):
        TotalWeight += self.Weights[x]
    return TotalWeight

   def SortByGreatest(self):
    Whileflag = 0
    SortFlag = 0
    TempWeightings = []
    SortedArrayLocation = []
  
    for x in range(len(self.Weights)):
      TempWeightings.append(self.Weights[x])
      SortedArrayLocation.append(x)

    while Whileflag == 0:
      SortFlag = 0
      for x in range(len(TempWeightings)):
        if(x+1 < len(TempWeightings)):
          if TempWeightings[x] < TempWeightings[x+1]:
            temp = TempWeightings[x]
            tempArray = SortedArrayLocation[x]
            TempWeightings[x] = TempWeightings[x+1]
            TempWeightings[x+1] = temp
            SortedArrayLocation[x] = SortedArrayLocation[x+1]
            SortedArrayLocation[x+1] = tempArray
            SortFlag = 1
      if SortFlag == 0:
        return SortedArrayLocation

   def SortByLeast(self):
    Whileflag = 0
    SortFlag = 0
    TempWeightings = []
    SortedArrayLocation = []
      
    for x in range(len(self.Weights)):
      TempWeightings.append(self.Weights[x])
      SortedArrayLocation.append(x)

    while Whileflag == 0:
      SortFlag = 0
      for x in range(len(TempWeightings)):
        if(x+1 < len(TempWeightings)):
          if TempWeightings[x] > TempWeightings[x+1]:
            temp = TempWeightings[x]
            tempArray = SortedArrayLocation[x]
            TempWeightings[x] = TempWeightings[x+1]
            TempWeightings[x+1] = temp
            SortedArrayLocation[x] = SortedArrayLocation[x+1]
            SortedArrayLocation[x+1] = tempArray
            SortFlag = 1
      if SortFlag == 0:
        return SortedArrayLocation
   def AddWeight(self, Weight):
    DividedWeight = round(Weight/self.NumofArray,0)
    RemainderWeight = Weight%self.NumofArray
    
    if self.GetTotalWeight() == 100:
      if(self.CheckIfEqual() == 1):
        self.Weights[self.PickRandomArrayNumber()] += RemainderWeight
        self.AddWeight(0)
    if self.GetTotalWeight() > 100:
      ArrayLocations = self.SortByGreatest()
      RemainderWeight = self.GetTotalWeight() - 100
      DividedRemainderWeight = round(RemainderWeight/(self.NumofArray),0)
      for x in range(1, len(self.Weights)):
        self.Weights[ArrayLocations[x]] -= DividedRemainderWeight
    if self.GetTotalWeight() < 100:
      ArrayLocations = self.SortByGreatest()
      RemainderWeight = 100 - self.GetTotalWeight()
      DividedRemainderWeight = round(RemainderWeight/(self.NumofArray),0)
      for x in range(1, len(self.Weights)):
        self.Weights[ArrayLocations[x]] += DividedRemainderWeight
    self.ForceEqualWeight()
  
   def ForceEqualWeight(self):
    WeightDiffrence = abs(self.GetTotalWeight() - 100)
    ArrayLocations = self.SortByLeast()
    if self.GetTotalWeight() <= 100:
      LowestArrayLocations = []
      LowestNumber = self.Weights[ArrayLocations[0]]
      for x in range(len(self.Weights)):
        if LowestNumber == self.Weights[ArrayLocations[x]]:
          LowestArrayLocations.append(ArrayLocations[x])
      self.Weights[ArrayLocations[random.randint(0,len(LowestArrayLocations) - 1)]] += WeightDiffrence
    elif self.GetTotalWeight() >= 100:
      HighestArrayLocations = []
      HighestNumber = self.Weights[ArrayLocations[0]]
      for x in range(len(self.Weights)):
        if HighestNumber == self.Weights[ArrayLocations[x]]:
          HighestArrayLocations.append(ArrayLocations[x])
      self.Weights[ArrayLocations[random.randint(0,len(HighestArrayLocations) - 1)]] -= WeightDiffrence

   def ChooseButton(self):
    CalcNumber = 0
    ChoosenNumber = random.randint(1,100)

    '''This is just a quick check to see if which button the AI chooses. The for loop adds the number of weights then checks if it's the calculated number is more than the chosen number. if the number is more than the chosen number the program now which button is press by what x equals'''
    for x in range(self.NumofArray):
      CalcNumber += self.Weights[x]
      if ChoosenNumber <= CalcNumber:
        self.ChoosenButton = x
        print("\nChosen Number: " + str(ChoosenNumber))
        print("Chosen Button: " + str(self.ChoosenButton)+ "\n")
        self.CheckRightButton()
        return
    '''Checks to see if for some reason the run isn't being counted'''
    self.ButtonNotPressed += 1 
    print("\nAI refuses to press button...\n")
  
   def CheckRightButton(self):
    if self.Buttons[self.ChoosenButton] == 1:
      print("FoundButton")
      self.FoundButtonCount += 1
      self.Weights[self.ChoosenButton] += self.LearningCurve
    else:
      print("Button not found")
      self.NoFoundButtonCount += 1
      self.Weights[self.ChoosenButton] -= self.LearningCurve
    self.AddWeight(0)
    self.CheckMinMaxValues()
    self.ShowWeightValues()
       
Testing = NeuroTestClass(4, 5)
for x in range(100):
  print("\nRun Number: " + str(x))
  Testing.ChooseButton()

Testing.ShowCompletedRuns()
Testing.ShowWeightValues()
Testing.ShowButtons()
Testing.ShowWinLoss()

'''Todo some weights are still going below 0
   Todo sometimes things recurring over 1000 times'''
