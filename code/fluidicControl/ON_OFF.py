from PyQt5.QtCore import pyqtSlot,  QSize
from PyQt5.QtWidgets import QMainWindow,  QMessageBox,  QInputDialog,  QFileDialog
from .Ui_window import Ui_MainWindow
import sys
import time
import RPi.GPIO as GPIO
import numpy as np 
import os 
import csv

# Hardware Pin Assignment 
GPIO.setmode(GPIO.BCM) ##Use GPIO Pin Reference
logic_switch_pumpA = 17 ##Hardware pin 11 - GPIO 17 --> Turning switch IC A OPEN/CLOSE
logic_switch_pumpB = 27 ##Hardware pin 13 - GPIO 27 --> Turning switch IC B OPEN/CLOSE
frequency_PIN_pumpA = 13 ##Hardware pin 33 - GPIO 13 --> Adjust pump_A driving frequency
frequency_PIN_pumpB = 12 ##Hardware pin 32 - GPIO 12 --> Adjust pump_B driving frequency

# Function converting flow rate values (uL/Min) to frequency values (Hz)
def flowRate_convert(flow_rate):
    
    if (flow_rate < 8.0):
        
        driving_frequency = 1
        
    elif (flow_rate > 12000.0):
        driving_frequency = 1
        
    else:##Convert flow rate (uL/min) to frequency (Hz)
        driving_frequency = flow_rate * 2
        # Derive required PWM frequency to produce desired flow rate output
        # Pump driving frequency = 0 - 300 Hertz
        # Driver default output frequency = 200 Hertz
        # Driver output frequency control with quadruplicated (4X) input frequency = 50 - 800 Hz
        ## for 300 Hz driver output --> 300*4 = 1200 Hz PWM 50% duty is required
        ## for 200 Hz driver output --> 200*4 = 800 Hz PWM 50% duty is required
        
        # 1) Derive required driver output frequency (Hz) from desired flow rate (uL/Min)
        ##driver_output = 199 + (-386*flow_rate) + (331* pow(flow_rate, 2)) + (- 106 * pow(flow_rate, 3)) + (17.1* pow(flow_rate, 4)) + (-1.36 * pow(flow_rate, 5)) + (0.0417 * pow(flow_rate, 6))
        
        #2) Derive required drive input frequency (Hz) from desired output frequency (Hz)
        ##driving_frequency = 997 + (-8.67*driver_output) + (0.0575 * pow(driver_output, 2)) + ((-7.26 * pow(10, -5)) * pow(driver_output, 3)) + ((3.05 * pow(10, -8)) * pow(driver_output, 4))
    
    return driving_frequency
    
    

class ON_OFF_RESPONSES(QMainWindow, Ui_MainWindow):
    def __init__(self,  parent=None):

        super(ON_OFF_RESPONSES, self).__init__(parent)
        self.setupUi(self)
        
        # STATIC PARAMETERS
        self.run_time_pA = 0
        self.run_time_pB = 0
        self.flowRate_pumpA  = 0
        self.flowRate_pumpB = 0
        self.driving_frequency_pumpA = 0 ##flowRate_convert(self.flowRate_pumpA)
        self.driving_frequency_pumpB = 0 ##flowRate_convert(self.flowRate_pumpB)
        self.duty_cycle_pA = 0
        self.duty_cycle_pB = 0
        
        #FLOW MODE PARAMETERS
        self.customFlow_pumpB = False
        self.customFlow_pumpA = False
        self.staticFlow_pumpA = False
        self.staticFlow_pumpB = False
        self.dynamicFlow_pumpA = False
        self.dynamicFlow_pumpB = False
        
        # DYNAMIC PARAMETERS
        self.dynamic_sweepRate_pumpB = 0
        self.flowRate_end_pumpB = 0
        self.flowRate_start_pumpB = 0
        self.dynamic_sweepRate_pumpA = 0
        self.flowRate_start_pumpA = 0
        self.flowRate_end_pumpA = 0
        
        #CUSTOM PARAMETERS
        self.custom_flowRate_values_pA = [] ##List to store values from CSV file
        self.custom_flowRate_values_pB = [] ##List to store values from CSV file
        
    
# ================ ON / OFF BUTTONS  ==================    
    #ON BUTTON PUMP_A
    @pyqtSlot()
    def on_ON_btn_pumpA_clicked(self):
        #Pin State Assignment 
        GPIO.setmode(GPIO.BCM) ##Use GPIO Pin
        GPIO.setup(logic_switch_pumpA,  GPIO.OUT)
        GPIO.setup(frequency_PIN_pumpA,  GPIO.OUT)
        
        # Derive and define driving frequencies (Hz) from flow rate input (uL/Min)
        driving_frequency_pumpA = flowRate_convert(self.flowRate_pumpA) ##Hertz (Driver = 4x pump freq)
        dynamic_start_frequency_pA = flowRate_convert(self.flowRate_start_pumpA)
        dynamic_end_frequency_pA = flowRate_convert(self.flowRate_end_pumpA)
        ##dynamic_sweepRate_pumpA = flowRate_convert(self.dynamic_sweepRate_pumpA)
        duty_cycle_pA = 50 ## % 

        #Define possible flow modes
        staticMode = (self.staticFlow_pumpA == True and self.dynamicFlow_pumpA == False and self.customFlow_pumpA == False)
        dynamicMode = (self.staticFlow_pumpA == False and self.dynamicFlow_pumpA == True and self.customFlow_pumpA == False)
        customMode = (self.staticFlow_pumpA == False and self.dynamicFlow_pumpA == False and self.customFlow_pumpA == True)
        
        #Flow Mode Condition 
        if (staticMode):
            #Condition handling out of range flow rate values
            if ((self.flowRate_pumpA < 8.0) or (self.flowRate_pumpA > 12000.0)):
                #Error message pop-up
                msg = QMessageBox()
                msg.setWindowTitle("---> FLOW RATE OUT OF RANGE <---")
                msg.setText("----->   THE FLOW RATE MUST BE BETWEEN 8 - 12 000 uL/Min   <-----")
                msg.setInformativeText("Information regarding flow range scope can be found below.")
                msg.setDetailedText("mp6-liq piezoelectric pump: \n\n Liquids flow range: 8 - 12 000 uL/Min \n\n Typical flow rate: 8 mL/Min \n\n Typical back pressure: 600 mbar @ 100Hz, 250 Vpp \n\n *** Review datasheet for further information. \n\n ")
                msg.setStyleSheet("background-color: rgb(114, 159, 207);")
                msg.setIcon(QMessageBox.Warning) ##.Information or .Warning or .Question
                msg.setStandardButtons(QMessageBox.Retry) ##.Ok or .Ignore or .Save or .Cancel
                msg.setDefaultButton(QMessageBox.Retry)
                x = msg.exec_()
                self.flowRate_pumpA = 0
                
            #Drive the pumps according to selected parameters 
            else:
                GPIO.output(logic_switch_pumpA,  GPIO.HIGH)
                frequency_ON_pumpA = GPIO.PWM(frequency_PIN_pumpA,  driving_frequency_pumpA)
                #Set 100% progress bar to the total run time entered
                self.progressBar_staticFlow_pumpA.setMaximum(self.run_time_pA)
                progressBar_staticFlowA_index = 0
                
                #Turn pumping ON
                frequency_ON_pumpA.start(duty_cycle_pA)
                #Iterate until run_time_pA value is reached
                for i in np.arange(self.run_time_pA):
                    progressBar_staticFlowA_index +=1
                    time.sleep(1)
                    self.progressBar_staticFlow_pumpA.setValue(progressBar_staticFlowA_index)
                
                #Stop pumping frequency
                frequency_ON_pumpA.stop()
                #Static mode terminated pop up message
                msg = QMessageBox()
                msg.setWindowTitle("COMPLETED")
                msg.setInformativeText(" PREDEFINED STATIC FLOW TERMINATED \n\n PRESS OFF TO STOP PUMPING ")
                msg.setStyleSheet("background-color: rgb(114, 159, 207);")
                msg.setIcon(QMessageBox.Information) ##.Information or .Warning or .Question
                msg.setStandardButtons(QMessageBox.Ok) ##.Ok or .Ignore or .Save or .Cancel
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()

            
        
        elif (dynamicMode):
            #Condition handling out of range flow rate values
            if ((self.flowRate_start_pumpA < 8.0) or (self.flowRate_end_pumpA >12000.0)):
                #Error message pop-up
                msg = QMessageBox()
                msg.setWindowTitle("---> FLOW RATE OUT OF RANGE <---")
                msg.setText("----->   THE FLOW RATE MUST BE BETWEEN 8 - 12 000 uL / Min   <-----")
                msg.setInformativeText("Information regarding flow range scope can be found below.")
                msg.setDetailedText("mp6-liq piezoelectric pump: \n\n Liquids flow range: 8 - 12 000 uL/Min \n\n Typical flow rate: 8 mL/Min \n\n Typical back pressure: 600 mbar @ 100Hz, 250 Vpp \n\n *** Review datasheet for further information. \n\n ")
                msg.setStyleSheet("background-color: rgb(114, 159, 207);")
                msg.setIcon(QMessageBox.Warning) ##.Information or .Warning or .Question
                msg.setStandardButtons(QMessageBox.Retry) ##.Ok or .Ignore or .Save or .Cancel
                msg.setDefaultButton(QMessageBox.Retry)
                x = msg.exec_()
                self.flowRate_start_pumpA = 0
                self.flowRate_end_pumpA = 0
                
            #Drive the pumps according to selected parameters
            else:
                GPIO.output(logic_switch_pumpA,  GPIO.HIGH)
                frequency_ON_pumpA = GPIO.PWM(frequency_PIN_pumpA,  dynamic_start_frequency_pA)
                #Define a range of frequencies from the input
                frequency_range = np.arange(dynamic_start_frequency_pA,  dynamic_end_frequency_pA,  self.dynamic_sweepRate_pumpA)
                #Set 100% progress to the total frequency values to be iterated upon
                self.progressBar_dynamicFlow_pumpA.setMaximum(len(frequency_range))
                progressBar_dynamicFlowA_index = 0
                
                # Iterate through frequency_range following dynamic_sweepRate_pumpA
                frequency_ON_pumpA.start(duty_cycle_pA)
                for n in frequency_range:
                    progressBar_dynamicFlowA_index +=1
                    time.sleep(1)
                    frequency_ON_pumpA.ChangeFrequency(n)
                    self.progressBar_dynamicFlow_pumpA.setValue(progressBar_dynamicFlowA_index)
                
                #Stop pumping frequency
                frequency_ON_pumpA.stop()
                #Dynamic mode terminated pop-up message
                msg = QMessageBox()
                msg.setWindowTitle("COMPLETED")
                msg.setInformativeText(" DYNAMIC FLOW TERMINATED \n\n PRESS OFF TO STOP PUMPING ")
                msg.setStyleSheet("background-color: rgb(114, 159, 207);")
                msg.setIcon(QMessageBox.Information) ##.Information or .Warning or .Question
                msg.setStandardButtons(QMessageBox.Ok) ##.Ok or .Ignore or .Save or .Cancel
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()
            
        elif(customMode):
            
            GPIO.output(logic_switch_pumpA,  GPIO.HIGH)
            frequency_ON_pumpA = GPIO.PWM(frequency_PIN_pumpA,  flowRate_convert(self.custom_flowRate_values_pA[0]))
            #Set 100% progress bar value to the number of values contained in the CSV file
            self.progressBar_customFlow_pumpA.setMaximum(len(self.custom_flowRate_values_pA))
            progressBar_customFlowA_index = 0
            
            #Initiate pumping and iterate through all flow rate values parsed from the CSV file
            frequency_ON_pumpA.start(duty_cycle_pA)
            for n in self.custom_flowRate_values_pA:
                    progressBar_customFlowA_index +=1
                    time.sleep(1)
                    frequency_ON_pumpA.ChangeFrequency(flowRate_convert(n))
                    self.progressBar_customFlow_pumpA.setValue(progressBar_customFlowA_index)
                
            #Terminate custom pumping frequency
            frequency_ON_pumpA.stop()
            #Custom mode terminated message
            msg = QMessageBox()
            msg.setWindowTitle("COMPLETED")
            msg.setInformativeText(" CUSTOM FLOW TERMINATED \n\n PRESS OFF TO STOP PUMPING ")
            msg.setStyleSheet("background-color: rgb(114, 159, 207);")
            msg.setIcon(QMessageBox.Information) ##.Information or .Warning or .Question
            msg.setStandardButtons(QMessageBox.Ok) ##.Ok or .Ignore or .Save or .Cancel
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()           
            
            
        #Condition handling invalid flow mode selection
        else:
            #Error message pop-up
            msg = QMessageBox()
            msg.setWindowTitle("---> INVALID FLOW MODE <---")
            msg.setText("----->  ONE FLOW MODE MUST BE SELECTED   <-----")
            msg.setInformativeText("   Details regarding the flow modes available can be found below.   ")
            msg.setDetailedText("\n STATIC FLOW MODE: Constant flow rate (uL / Min) during a pre-defined time period (Sec).  \n\n DYNAMIC FLOW MODE: Constant change of flow rate within a pre-define range of values following a desired sweep rate (uL/Min). \n\n CUSTOM FLOW MODE: Flow rate output follows complex periodic functions uploaded via CSV file. \n\n")
            msg.setStyleSheet("background-color: rgb(114, 159, 207);")
            msg.setIcon(QMessageBox.Critical) ##.Information or .Warning or .Question
            msg.setStandardButtons(QMessageBox.Retry) ##.Ok or .Ignore or .Save or .Cancel
            msg.setDefaultButton(QMessageBox.Retry)
            x = msg.exec_()
    
    #OFF BUTTON PUMP_A
    @pyqtSlot()
    def on_OFF_btn_pumpA_clicked(self):
        
        driving_frequency_pumpA = flowRate_convert(self.flowRate_pumpA)
        GPIO.setmode(GPIO.BCM) ##Use GPIO Pin
        GPIO.setup(logic_switch_pumpA,  GPIO.OUT)
        GPIO.setup(frequency_PIN_pumpA,  GPIO.OUT)
        
        #Turn OFF switch IC Logic Pin
        GPIO.output(logic_switch_pumpA,  GPIO.LOW)
        #Turn OFF frequency pin 
        frequency_ON_pumpA = GPIO.PWM(frequency_PIN_pumpA,  driving_frequency_pumpA)
        frequency_ON_pumpA.stop()
        #Clean up pins 
        GPIO.cleanup((logic_switch_pumpA, frequency_PIN_pumpA))
        
        #Reset progress bar to 0% + flow modes to default
        if (self.staticFlow_pumpA == True):
            self.progressBar_staticFlow_pumpA.setValue(0)
            self.staticFlow_pumpA = False
            #self.flow_rate_pumpA.setValue(0.00)
            #self.run_time_pumpA.setValue(0.00)
        
        elif (self.dynamicFlow_pumpA == True):
            self.progressBar_dynamicFlow_pumpA.setValue(0)
            self.dynamicFlow_pumpA = False
            #self.flowRate_start_pumpA.setValue(0.00)
            #self.flowRate_end_pumpA.setValue(0.00)
            #self.dynamic_sweepRate_pumpA.setValue(0.00)
        
        elif (self.customFlow_pumpA == True):
            self.progressBar_customFlow_pumpA.setValue(0)
            self.dynamicFlow_pumpA = False

    #ON BUTTON PUMP_B
    @pyqtSlot()
    def on_ON_btn_pumpB_clicked(self):
        
        GPIO.setmode(GPIO.BCM) ##Use GPIO Pin
        GPIO.setup(frequency_PIN_pumpB,  GPIO.OUT)
        GPIO.setup(logic_switch_pumpB,  GPIO.OUT)
        
        # Derive & define pumping frequencies (Hz) from fow rate input (uL/Min)
        driving_frequency_pumpB = flowRate_convert(self.flowRate_pumpB) ##Hertz (Driver = 4x pump freq)
        dynamic_start_frequency_pB = flowRate_convert(self.flowRate_start_pumpB)
        dynamic_end_frequency_pB = flowRate_convert(self.flowRate_end_pumpB)
        ##dynamic_sweepRate_pumpB= flowRate_convert(self.dynamic_sweepRate_pumpB)
        duty_cycle_pB = 50 ## %      
        
        #Define available flow modes
        staticMode = (self.staticFlow_pumpB == True and self.dynamicFlow_pumpB == False and self.customFlow_pumpB == False)
        dynamicMode = (self.staticFlow_pumpB == False and self.dynamicFlow_pumpB == True and self.customFlow_pumpB == False)
        customMode = (self.staticFlow_pumpB == False and self.dynamicFlow_pumpB == False and self.customFlow_pumpB == True) 
        
        if (staticMode):
            #Condition handling out of range flow rate input
            if ((self.flowRate_pumpB < 8.0) or (self.flowRate_pumpB > 12000.0)):
                #Error message pop-up
                msg = QMessageBox()
                msg.setWindowTitle("---> FLOW RATE OUT OF RANGE <---")
                msg.setText("----->   THE FLOW RATE MUST BE BETWEEN 8 - 12 000 uL/Min   <-----")
                msg.setInformativeText("Information regarding flow range scope can be found below.")
                msg.setDetailedText("mp6-liq piezoelectric pump: \n\n Liquids flow range: 8 - 12 000 uL/Min \n\n Typical flow rate: 8 mL/Min \n\n Typical back pressure: 600 mbar @ 100Hz, 250 Vpp \n\n *** Review datasheet for further information. \n\n ")
                msg.setStyleSheet("background-color: rgb(114, 159, 207);")
                msg.setIcon(QMessageBox.Warning) ##.Information or .Warning or .Question
                msg.setStandardButtons(QMessageBox.Retry) ##.Ok or .Ignore or .Save or .Cancel
                msg.setDefaultButton(QMessageBox.Retry)
                x = msg.exec_()
                self.flowRate_pumpB = 0
                
            #Drive the pump according to the parameters selected
            else:
                GPIO.output(logic_switch_pumpB,  GPIO.HIGH)
                frequency_ON_pumpB = GPIO.PWM(frequency_PIN_pumpB,  driving_frequency_pumpB)
                #Set 100% progress bar value to total run time selected 
                self.progressBar_staticFlow_pumpB.setMaximum(self.run_time_pB)
                progressBar_staticFlowB_index = 0
                
                #Initiate pumping until total run time has been reached
                frequency_ON_pumpB.start(duty_cycle_pB)
                for i in np.arange(self.run_time_pB):
                    progressBar_staticFlowB_index +=1
                    time.sleep(1)
                    self.progressBar_staticFlow_pumpB.setValue(progressBar_staticFlowB_index)
                
                #Terminate pumping frequency
                frequency_ON_pumpB.stop()
                #Static terminated message
                msg = QMessageBox()
                msg.setWindowTitle("COMPLETED")
                msg.setInformativeText(" PREDEFINED STATIC FLOW TERMINATED \n\n PRESS OFF TO STOP PUMPING ")
                msg.setStyleSheet("background-color: rgb(114, 159, 207);")
                msg.setIcon(QMessageBox.Information) ##.Information or .Warning or .Question
                msg.setStandardButtons(QMessageBox.Ok) ##.Ok or .Ignore or .Save or .Cancel
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()

        
        elif (dynamicMode):
            #Condition handling out of range flow rate input
            if ((self.flowRate_start_pumpB < 8.0) or (self.flowRate_end_pumpB >12000.0)):
                #Error message pop-up
                msg = QMessageBox()
                msg.setWindowTitle("---> FLOW RATE OUT OF RANGE <---")
                msg.setText("----->   THE FLOW RATE MUST BE BETWEEN 8 - 12 000 uL / Min   <-----")
                msg.setInformativeText("Information regarding flow range scope can be found below.")
                msg.setDetailedText("mp6-liq piezoelectric pump: \n\n Liquids flow range: 8 - 12 000 uL/Min \n\n Typical flow rate: 8 mL/Min \n\n Typical back pressure: 600 mbar @ 100Hz, 250 Vpp \n\n *** Review datasheet for further information. \n\n ")
                msg.setStyleSheet("background-color: rgb(114, 159, 207);")
                msg.setIcon(QMessageBox.Warning) ##.Information or .Warning or .Question
                msg.setStandardButtons(QMessageBox.Retry) ##.Ok or .Ignore or .Save or .Cancel
                msg.setDefaultButton(QMessageBox.Retry)
                x = msg.exec_()
                self.flowRate_start_pumpB = 0
                self.flowRate_end_pumpB = 0
            
            #Initiate pumping according to the parameters selected
            else:
                
                GPIO.output(logic_switch_pumpB,  GPIO.HIGH)
                frequency_ON_pumpB = GPIO.PWM(frequency_PIN_pumpB,  dynamic_start_frequency_pB)
                #Define the range of frequencies to be iterated upon
                frequency_range = np.arange(dynamic_start_frequency_pB,  dynamic_end_frequency_pB,  self.dynamic_sweepRate_pumpB)
                #Set 100% progress bar value to the total number of frequency values
                self.progressBar_dynamicFlow_pumpB.setMaximum(len(frequency_range))
                progressBar_dynamicFlowB_index = 0
                
                # Iterate through frequency_range following dynamic_sweepRate_pumpA
                frequency_ON_pumpB.start(duty_cycle_pB)
                for n in frequency_range:
                    progressBar_dynamicFlowB_index +=1
                    time.sleep(1)
                    frequency_ON_pumpB.ChangeFrequency(n)
                    self.progressBar_dynamicFlow_pumpB.setValue(progressBar_dynamicFlowB_index)
                
                #Terminate pumping frequency
                frequency_ON_pumpB.stop()
                #Dynamic mode terminated message
                msg = QMessageBox()
                msg.setWindowTitle("COMPLETED")
                msg.setInformativeText(" DYNAMIC FLOW TERMINATED \n\n PRESS OFF TO STOP PUMPING ")
                msg.setStyleSheet("background-color: rgb(114, 159, 207);")
                msg.setIcon(QMessageBox.Information) ##.Information or .Warning or .Question
                msg.setStandardButtons(QMessageBox.Ok) ##.Ok or .Ignore or .Save or .Cancel
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()
        
        elif(customMode):
            
            GPIO.output(logic_switch_pumpB,  GPIO.HIGH)
            frequency_ON_pumpB = GPIO.PWM(frequency_PIN_pumpB,  flowRate_convert(self.custom_flowRate_values_pB[0]))
            #Set 100% progress bar value to the total number of flow rate value parsed in the CSV file
            self.progressBar_customFlow_pumpB.setMaximum(len(self.custom_flowRate_values_pB))
            progressBar_customFlowB_index = 0
            
            #Initiate pumping following the range of values parsed in the CSV file
            frequency_ON_pumpB.start(duty_cycle_pB)
            for n in self.custom_flowRate_values_pB:
                    progressBar_customFlowB_index += 1
                    time.sleep(1)
                    frequency_ON_pumpB.ChangeFrequency(flowRate_convert(n))
                    self.progressBar_customFlow_pumpB.setValue(progressBar_customFlowB_index)
            
            #Terminate pumping frequency
            frequency_ON_pumpB.stop()
            #Custom mode terminated message
            msg = QMessageBox()
            msg.setWindowTitle("COMPLETED")
            msg.setInformativeText(" CUSTOM FLOW TERMINATED \n\n PRESS OFF TO STOP PUMPING ")
            msg.setStyleSheet("background-color: rgb(114, 159, 207);")
            msg.setIcon(QMessageBox.Information) ##.Information or .Warning or .Question
            msg.setStandardButtons(QMessageBox.Ok) ##.Ok or .Ignore or .Save or .Cancel
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()  
            
        
        #Condition handling invalid flow mode selections
        else:
            #Error message pop-up
            msg = QMessageBox()
            msg.setWindowTitle("---> INVALID FLOW MODE <---")
            msg.setText("----->  ONE FLOW MODE MUST BE SELECTED   <-----")
            msg.setInformativeText("   Details regarding the flow modes available can be found below.   ")
            msg.setDetailedText("\n STATIC FLOW MODE: Constant flow rate (uL / Min) during a pre-defined time period (Sec).  \n\n DYNAMIC FLOW MODE: Constant change of flow rate within a pre-define range of values following a desired sweep rate (uL/Min). \n\n CUSTOM FLOW MODE: Flow rate output follows complex periodic functions uploaded via CSV file. \n\n")
            msg.setStyleSheet("background-color: rgb(114, 159, 207);")
            msg.setIcon(QMessageBox.Critical) ##.Information or .Warning or .Question
            msg.setStandardButtons(QMessageBox.Retry) ##.Ok or .Ignore or .Save or .Cancel
            msg.setDefaultButton(QMessageBox.Retry)
            x = msg.exec_()
    
    
    
    #OFF BUTTON PUMP_B
    @pyqtSlot()
    def on_OFF_btn_pumpB_2_clicked(self):
        
        driving_frequency_pumpB = flowRate_convert(self.flowRate_pumpB)
        GPIO.setmode(GPIO.BCM) ##Use GPIO Pin
        GPIO.setup(logic_switch_pumpB,  GPIO.OUT)
        GPIO.setup(frequency_PIN_pumpB,  GPIO.OUT)
        
        #Turn OFF all pins
        GPIO.output(logic_switch_pumpB,  GPIO.LOW)
        frequency_ON_pumpB = GPIO.PWM(frequency_PIN_pumpB,  driving_frequency_pumpB)
        frequency_ON_pumpB.stop()
        GPIO.cleanup((logic_switch_pumpB, frequency_PIN_pumpB))
        
        #Reset progress bars & flow modes
        if (self.staticFlow_pumpB == True):
            self.progressBar_staticFlow_pumpB.setValue(0)
            self.staticFlow_pumpB = False
            #self.flow_rate_pumpB.setValue(0.00)
            #self.run_time_pumpB.setValue(0.00)
        
        elif (self.dynamicFlow_pumpB == True):
            self.progressBar_dynamicFlow_pumpB.setValue(0)
            self.dynamicFlow_pumpB = False
            #self.flowRate_start_pumpB.setValue(0.00)
            #self.flowRate_end_pumpB.setValue(0.00)
            #self.dynamic_sweepRate_pumpB.setValue(0.00)
        
        elif (self.customFlow_pumpB == True):
            self.progressBar_customFlow_pumpB.setValue(0)
            self.customFlow_pumpB = False
   
  








# =============== FLOW MODE TOGGLE BUTTONS ================
    @pyqtSlot(bool)
    def on_staticFlow_pumpA_toggled(self, staticFlow_pumpA):
       if staticFlow_pumpA == True:
            self.staticFlow_pumpA = True
       elif staticFlow_pumpA == False:
           self.staticFlow_pumpA = False
        
    @pyqtSlot(bool)
    def on_dynamicFlow_pumpA_toggled(self, dynamicFlow_pumpA):
        if dynamicFlow_pumpA == True:
            self.dynamicFlow_pumpA = True
        elif dynamicFlow_pumpA == False:
            self.dynamicFlow_pumpA = False

    @pyqtSlot(bool)
    def on_customFlow_pumpA_toggled(self, customFlow_pumpA):
        if customFlow_pumpA == True:
            self.customFlow_pumpA = True
        elif customFlow_pumpA == False:
            self.customFlow_pumpA = False
     
    @pyqtSlot(bool)
    def on_staticFlow_pumpB_toggled(self, staticFlow_pumpB):
        if staticFlow_pumpB == True:
            self.staticFlow_pumpB = True
        elif staticFlow_pumpB == False:
            self.staticFlow_pumpB = False
        
    @pyqtSlot(bool)
    def on_dynamicFlow_pumpB_toggled(self, dynamicFlow_pumpB):
        if dynamicFlow_pumpB == True:
            self.dynamicFlow_pumpB = True
        elif dynamicFlow_pumpB == False:
            self.dynamicFlow_pumpB = False
        
    @pyqtSlot(bool)
    def on_customFlow_pumpB_toggled(self, customFlow_pumpB):
        if customFlow_pumpB == True:
            self.customFlow_pumpB = True
        elif customFlow_pumpB == False:
            self.customerFlow_pumpB = False
        
    








# ================== STATIC PARAMETERS SELECTION BUTTONS ============
    @pyqtSlot(float)
    def on_run_time_pumpA_valueChanged(self, run_time_pA):
        self.run_time_pA = run_time_pA
            
        
    @pyqtSlot(float)
    def on_run_time_pumpB_valueChanged(self, run_time_pB):
        self.run_time_pB = run_time_pB
        
    @pyqtSlot(float)
    def on_flow_rate_pumpA_valueChanged(self, flowRate_pumpA):
        self.flowRate_pumpA = flowRate_pumpA
        
    
    @pyqtSlot(float)
    def on_flow_rate_pumpB_valueChanged(self, flowRate_pumpB):
        self.flowRate_pumpB = flowRate_pumpB
         
    








# ================= DYNAMIC PARAMETERS SELECTION BUTTONS ===========
    @pyqtSlot(float)
    def on_flowRate_start_pumpA_valueChanged(self, flowRate_start_pumpA):
        self.flowRate_start_pumpA = flowRate_start_pumpA
        
    
    @pyqtSlot(float)
    def on_flowRate_end_pumpA_valueChanged(self, flowRate_end_pumpA):
        self.flowRate_end_pumpA = flowRate_end_pumpA
        
    
    @pyqtSlot(float)
    def on_dynamic_sweepRate_pumpA_valueChanged(self, dynamic_sweepRate_pumpA):
        self.dynamic_sweepRate_pumpA = dynamic_sweepRate_pumpA
        
    
    @pyqtSlot(float)
    def on_flowRate_start_pumpB_valueChanged(self, flowRate_start_pumpB):
        self.flowRate_start_pumpB = flowRate_start_pumpB
        
    
    @pyqtSlot(float)
    def on_flowRate_end_pumpB_valueChanged(self, flowRate_end_pumpB):
        self.flowRate_end_pumpB = flowRate_end_pumpB
        
    @pyqtSlot(float)
    def on_dynamic_sweepRate_pumpB_valueChanged(self, dynamic_sweepRate_pumpB):
        self.dynamic_sweepRate_pumpB = dynamic_sweepRate_pumpB



# =====================CUSTOM PARAMETERS / FILE UPLOAD BUTTONS ====================
    @pyqtSlot()
    def on_upload_pumpA_clicked(self):
        file_filter = '(*.csv)'
        filename = QFileDialog.getOpenFileName(parent = self,  caption = 'SELECT A DATA FILE', directory = os.getcwd(), filter = file_filter)
        
        #Read the CSV file
        with open("testFile.csv",  'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            #Parse + save flow rate values in list
            for row in csv_reader:
                self.custom_flowRate_values_pA.append(row)
            #Convert values to float
            self.custom_flowRate_values_pA = list(np.float_(self.custom_flowRate_values_pA))

    @pyqtSlot()
    def on_upload_pumpB_clicked(self):
        file_filter = '(*.csv)'
        filename = QFileDialog.getOpenFileName(parent=self,  caption = 'SELECT A DATA FILE', directory = os.getcwd(), filter = file_filter)
        
        #Read the CSV file
        with open("testFile.csv",  'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            #Parse + save flow rate values
            for row in csv_reader:
                self.custom_flowRate_values_pB.append(row)
            #Convert values to float
            self.custom_flowRate_values_pB = list(np.float_(self.custom_flowRate_values_pB))
