# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 05:41:32 2020

@author: hi
"""

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from rasa_sdk.events import UserUttered, Restarted
from typing import Any, Text, Dict, List
from rasa_sdk.events import AllSlotsReset
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import datetime as dt
from datetime import date, timedelta
from rasa_sdk.events import FollowupAction
import configparser
import numpy as np
import pandas as pd
from rasa_sdk.forms import FormAction
import random
class Action_Get_Date_Range(Action):

    def name(self) -> Text:
        return "ActionGetDateRange"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        fromDateSlot=None;
        toDateSlot=None;
        fromDateSlot = tracker.get_slot("FromDate");
        try:
            toDateSlot = tracker.get_slot("ToDate")
        except:
            pass
        print("fd,td",fromDateSlot,toDateSlot)
        
        if fromDateSlot!=None:
            try:
                 fromDateSlot = dt.datetime.strptime(fromDateSlot, '%d-%m-%Y')
            except:
                try:
                        fromDateSlot = dt.datetime.strptime(fromDateSlot, '%d.%m.%Y')
                except:
                     try:
                        fromDateSlot = dt.datetime.strptime(fromDateSlot, '%d/%m/%Y')
                     except Exception as ex:
                        fromDateSlot=None;
                        message = "Please give dates in correct format"
                        dispatcher.utter_message(message)
                        return[]
                       # print("Error =========> "+ex)
                        
                        
             
        print("so date format is",fromDateSlot)
        fromdateFormat=fromDateSlot
        fromDateSlot=fromDateSlot.strftime('%d-%m-%Y') 
        isChangeDate = tracker.get_slot("isChangeDate");print("isChangeDate",isChangeDate)
        if isChangeDate== True: 
                ent = tracker.latest_message['entities'][0]['value'];print("extracted entities",ent)
                message = "Your changed interview date is {} ".format(ent)
                
                dispatcher.utter_message(message)
                return[SlotSet("changedDate", ent),SlotSet("isChangeDate", False)]
                
        if toDateSlot!=None:
            try:
                 toDateSlot = dt.datetime.strptime(toDateSlot, '%d-%m-%Y')
            except:
                try:
                        toDateSlot = dt.datetime.strptime(toDateSlot, '%d.%m.%Y')
                except:
                     try:
                        toDateSlot = dt.datetime.strptime(toDateSlot, '%d/%m/%Y')
                     except Exception as ex:
                        toDateSlot=None;
                        message = "Please give dates in correct format"
                        dispatcher.utter_message(message)
                        return[]
                        
                        
            delta = toDateSlot-fromdateFormat  ;print(delta,"delta")       # as timedelta
            allDays=[];buttons=[];
            toDateSlot=toDateSlot.strftime('%d-%m-%Y')
            for i in range(delta.days + 1):
                day = fromdateFormat + timedelta(days=i);
                weekno = day.weekday();
                day=day.strftime('%d-%m-%Y')
                
                if weekno<5:
                    allDays.append(day) ; #"payload":"{}".format(day)
                    #print(day) ;  "/intent_1{"test_slot_1":"test_value_1"}"
                    buttons.append({"title": "{}".format(day), "payload":'''/DateString{"SelectDate1":"'''+"{}".format(day)+'''"}'''})
                    #buttons.append({"title": "{}".format(day), "payload":'/DateString' })
            print("all days===>",allDays)
            if len(allDays)==1:
                dispatcher.utter_message("You selected {}".format(allDays[0]))
            elif len(allDays)==2:
                dispatcher.utter_message("Your selected dates are {},{}".format(allDays[0],allDays[1]))
            elif len(allDays)==3:
                dispatcher.utter_message("Your selected dates are {},{},{}".format(allDays[0],allDays[1],allDays[2]))
            else :
                message = "please let us know 3 possible dates when you are available "
                
                dispatcher.utter_message(message, buttons=buttons)
                return[SlotSet("RequireNextDay", True),SlotSet("DateRange", allDays)]
        else:       
            dispatcher.utter_message("You selected {}".format(fromDateSlot))  
            
        return[SlotSet("RequireNextDay", False)]
        
        
class Action_Select_Another_Date(Action):

    def name(self) -> Text:
        return "ActionSelectNextDate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("came to ActionSelectNextDate")
        
        RequireNextDaySlot = tracker.get_slot("RequireNextDay");
        SelectDate1Slot = tracker.get_slot("SelectDate1");
        SelectDate2Slot = tracker.get_slot("SelectDate2");
        SelectDate3Slot = tracker.get_slot("SelectDate3");
        GetDateRangeSlot = tracker.get_slot("DateRange");
        print("GetDateRangeSlot",GetDateRangeSlot);
        print("SelectDate1",SelectDate1Slot);
        print("SelectDate2",SelectDate2Slot)
        print("SelectDate3",SelectDate3Slot)
        print("RequireNextDaySlot",RequireNextDaySlot)
        try:
           GetDateRangeSlot.remove(SelectDate1Slot)
           try:
               GetDateRangeSlot.remove(SelectDate2Slot);
           except Exception as ex:
               print("error here===>" + ex)
               pass
           
        except:
            pass
        
        
        buttons=[]  
        if RequireNextDaySlot==False or (RequireNextDaySlot==True and (SelectDate1Slot!=None and SelectDate2Slot!=None and SelectDate3Slot!=None)):
                    FollowupAction("ActionUtterUpdatedDates");
                    return []
                    
        elif RequireNextDaySlot==True and (SelectDate1Slot!=None and SelectDate2Slot!=None):
                    print("GetDateRangeSlot",GetDateRangeSlot,"------------");
                    print("SelectDate1",SelectDate1Slot,"----------------")
                    for datebutton in GetDateRangeSlot:
                         buttons.append({"title": datebutton, "payload":'''/DateString{"SelectDate3":"'''+datebutton+'''"}'''})
                    message = "Select your Third day"
                    dispatcher.utter_message(message, buttons=buttons)
                    return[SlotSet("RequireNextDay", False),SlotSet("daySelected", None),SlotSet("slotSelected", None)]
        
                    
        elif RequireNextDaySlot==True and (SelectDate1Slot!=None):
                    print("GetDateRangeSlot",GetDateRangeSlot,"------------");
                    print("SelectDate1",SelectDate1Slot,"----------------")
                    for datebutton in GetDateRangeSlot:
                         buttons.append({"title": datebutton, "payload":'''/DateString{"SelectDate2":"'''+datebutton+'''"}'''})
                    message = "Select your second day"
                    dispatcher.utter_message(message, buttons=buttons)
                    return[SlotSet("RequireNextDay", True)]
                    
         
                
        
          
class Action_Utter_Updated_Dates(Action):

    def name(self) -> Text:
        return "ActionUtterUpdatedDates"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        RequireNextDaySlot = tracker.get_slot("RequireNextDay");
        if RequireNextDaySlot==False:
            dispatcher.utter_message("we update our records, and we couldn't imagine anything better than to meet up with you later date with new meeting dates, in the interim ,We need you to appreciate all that life brings to the table – Much obliged")  
        return []
    
class Action_Ask_Slots_For_Day(Action):

    def name(self) -> Text:
        return "ActionAskSlots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("-------------------ActionAskSlots-----------------------------'")
        configFile = configparser.RawConfigParser()
        configFile.readfp(open(r'External_config.txt'))
        InterviewPanelPerSlot=configFile.get('SlotDetails', 'InterviewPanelPerSlot');
        selectDay1 = tracker.get_slot("SelectDate1");
        FromDate = tracker.get_slot("FromDate");print(FromDate,"FromDate")
        daySelected = tracker.get_slot("daySelected");
        
        
        if daySelected!=None:
            Date1Slot=selectDay1;
        elif daySelected==None and selectDay1!=None:
            Date1Slot=selectDay1
        elif daySelected==None and selectDay1==None and FromDate!=None :
            Date1Slot=FromDate
        else:
            Date1Slot="19-02-2029"
            
            
        print("date taken ------>" ,Date1Slot )
        try:
                 Date1Slot = dt.datetime.strptime(Date1Slot, '%d-%m-%Y')
        except:
                try:
                        Date1Slot = dt.datetime.strptime(Date1Slot, '%d.%m.%Y')
                except:
                     try:
                        Date1Slot = dt.datetime.strptime(Date1Slot, '%d/%m/%Y')
                     except Exception as ex:
                        Date1Slot=None;
                        message = "Please give dates in correct format"
                        dispatcher.utter_message(message)
                        return[]  
                        
        Date1Slot=Date1Slot.strftime('%d-%m-%Y')               
        df = pd.read_csv("timeSlots.csv");
        print("columns",df.columns)
        datePresent=df[df["Days"] == Date1Slot].index.tolist()
        if len(datePresent)<=0:
            row = [Date1Slot, InterviewPanelPerSlot, InterviewPanelPerSlot,InterviewPanelPerSlot, InterviewPanelPerSlot,0, InterviewPanelPerSlot, InterviewPanelPerSlot,InterviewPanelPerSlot, InterviewPanelPerSlot]
            df.loc[len(df)] = row
            df.to_csv("timeSlots.csv", index=False);
            datePresent=df[df["Days"] == Date1Slot].index.tolist()
            
        buttons=[]
        values=df.iloc[datePresent, 1:];
        print(values,"values present======================================");
        dict_slotButtons=values.to_dict('list');print("dict1",dict_slotButtons)
        for k,v in dict_slotButtons.items():
                if int(v[0])>0:
                     buttons.append({"title": k, "payload":'''/PickSlotOnDay1{"slotSelected":"'''+k+'''"}'''})
        message = "Choose your Slot"
        buttons.append({"title":"Sorry I am not available on this", "payload":'''/option4'''})
        dispatcher.utter_message(message, buttons=buttons)
        return[SlotSet("daySelected", Date1Slot)]      
                    
#        else:
#            row = [Date1Slot, InterviewPanelPerSlot, InterviewPanelPerSlot,InterviewPanelPerSlot, InterviewPanelPerSlot,0, InterviewPanelPerSlot, InterviewPanelPerSlot,InterviewPanelPerSlot, InterviewPanelPerSlot]
#            df.loc[len(df)] = row
#            df.to_csv("timeSlots.csv", index=False)
            
            
class Action_Selected_slot(Action):

    def name(self) -> Text:
        return "ActionSlotSelect"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("----ActionSlotSelect---------")
        df = pd.read_csv("timeSlots.csv");
        dateUpdate = tracker.get_slot("daySelected");
        slotUpdate = tracker.get_slot("slotSelected");
        rowIndex=df[df["Days"] == dateUpdate].index.tolist()
        print("present value",df.iloc[rowIndex][slotUpdate] ,print(type(df.iloc[rowIndex][slotUpdate] )))
        presentvalue=df.iloc[rowIndex][slotUpdate] 
        #df.set_value(rowIndex, slotUpdate,presentvalue-1)
        df.at[rowIndex, slotUpdate] = presentvalue-1
        df.to_csv("timeSlots.csv", index=False)
        buttons=[]
        message = "<first name >, you choose Interview Slot {} on date {} , confirm ? or You want to Book at any other time on {}".format(slotUpdate,dateUpdate,dateUpdate)
        buttons.append({"title":"Confirm for {} and Interview Slot {}".format(slotUpdate,dateUpdate), "payload":'''/confirmSlot1'''})
        buttons.append({"title":"No , I need Another time on {}".format(dateUpdate), "payload":'''/askForSlotTimeChange'''})
        buttons.append({"title":"Is any thing possible to do in Weekend or any After hours on {}".format(dateUpdate), "payload":'''/otherDays'''})
        dispatcher.utter_message(message, buttons=buttons)
        return[]      
       
        



        
class Action_Slot_ChangeDate(Action):

    def name(self) -> Text:
        return "ActionChangeDateSelect"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("----ActionChangeDateSelect---------")
#        buttons=[]
#        GetDateRangeSlot = tracker.get_slot("DateRange");
#        originalDaySelected = tracker.get_slot("daySelected");
#        if GetDateRangeSlot!=None:
#            for datebutton in GetDateRangeSlot:
#                        buttons.append({"title": datebutton, "payload":'''/DateString{"daySelected":"'''+datebutton+'''"}'''})
#                        message = "Select your prefered day of interview from the given range"
#                        dispatcher.utter_message(message, buttons=buttons)
#                        return[]
#        else:
        print("else statetment----------------------")
        message = "Give your prefered day of interview"
        dispatcher.utter_message(message)
        given=tracker.latest_message.get('text');print("given",given);
        return[SlotSet("isChangeDate", True)]      
          #  return [UserUttered(text=, parse_data= {'intent': {'DateString': 'recipe', 'confidence': 1.0}})]
        
class Update_Changed_Interview_Date_And_Slot(Action):

    def name(self) -> Text:
        return "updateInterviewDate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("----updateInterviewDate---------")
        df = pd.read_csv("timeSlots.csv");
        changedDate = tracker.get_slot("changedDate");
        originalSlot = tracker.get_slot("slotSelected");
        originalDate = tracker.get_slot("daySelected");
        configFile = configparser.RawConfigParser()
        configFile.readfp(open(r'External_config.txt'))
        InterviewPanelPerSlot=configFile.get('SlotDetails', 'InterviewPanelPerSlot');
        datePresent=df[df["Days"] == changedDate].index.tolist();
        buttons=[]
        if len(datePresent)>0:
            
            values=df.iloc[datePresent, 1:];
            print(values);
            dict_slotButtons=values.to_dict('list');print("dict1",dict_slotButtons)
            for k,v in dict_slotButtons.items():
                if v[0]>0:
                     buttons.append({"title": k, "payload":'''/PickSlotOnDay1{"slotSelected":"'''+k+'''"}'''})
            message = "Choose your Slot"
            #buttons.append({"title":"Sorry I am not available on this", "payload":'''/option4'''})
            dispatcher.utter_message(message, buttons=buttons)
             
                    
        else:
            row = [changedDate, InterviewPanelPerSlot, InterviewPanelPerSlot,InterviewPanelPerSlot, InterviewPanelPerSlot,0, InterviewPanelPerSlot, InterviewPanelPerSlot,InterviewPanelPerSlot, InterviewPanelPerSlot]
            df.loc[len(df)] = row;print("row##########################",row)
            headers=df.columns[1:]
            values=row[1:];print("values---->",values)
            #dict_slotButtons=values.to_dict('list');print("dict1",dict_slotButtons)
            for i in range(len(headers)):
                if int(values[i])>0:
                     buttons.append({"title":headers[i], "payload":'''/PickSlotOnDay1{"slotSelected":"'''+headers[i]+'''"}'''})
            message = "Choose your Slot"
            #buttons.append({"title":"Sorry I am not available on this", "payload":'''/option4'''})
            dispatcher.utter_message(message, buttons=buttons)
        
            df.to_csv("timeSlots.csv", index=False)
        df = pd.read_csv("timeSlots.csv");    
        rowIndex=df[df["Days"] == originalDate].index.tolist()
        presentvalue=df.iloc[rowIndex][originalSlot] 
        df.at[rowIndex, originalSlot] = presentvalue+1
        df.to_csv("timeSlots.csv", index=False)
        message = "Pick the slots From Available ones"
        dispatcher.utter_message(message, buttons=buttons)
        return[SlotSet("isChangeSlot", True),SlotSet("daySelected", changedDate)]


class Update_Changed_Interview__Slot(Action):

    def name(self) -> Text:
        return "updateInterviewSlot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("----updateInterviewDate---------")
        df = pd.read_csv("timeSlots.csv");
        originalDate = tracker.get_slot("daySelected");
        originalSlot = tracker.get_slot("slotSelected");
        configFile = configparser.RawConfigParser()
        configFile.readfp(open(r'External_config.txt'))
        InterviewPanelPerSlot=configFile.get('SlotDetails', 'InterviewPanelPerSlot');
        datePresent=df[df["Days"] == originalDate].index.tolist();
        buttons=[]
        if len(datePresent)>0:
            
            values=df.iloc[datePresent, 1:];
            print(values);
            dict_slotButtons=values.to_dict('list');print("dict1",dict_slotButtons)
            for k,v in dict_slotButtons.items():
                if v[0]>0:
                     buttons.append({"title": k, "payload":'''/PickSlotOnDay1{"slotSelected":"'''+k+'''"}'''})
            message = "Choose your Slot"
            #buttons.append({"title":"Sorry I am not available on this", "payload":'''/option4'''})
            dispatcher.utter_message(message, buttons=buttons)
                
                    
        else:
            row = [originalDate, InterviewPanelPerSlot, InterviewPanelPerSlot,InterviewPanelPerSlot, InterviewPanelPerSlot,0, InterviewPanelPerSlot, InterviewPanelPerSlot,InterviewPanelPerSlot, InterviewPanelPerSlot]
            df.loc[len(df)] = row;print("row##########################",row)
            headers=df.columns[1:]
            values=row[1:];print("values---->",values)
            #dict_slotButtons=values.to_dict('list');print("dict1",dict_slotButtons)
            for i in range(len(headers)):
                if int(values[i])>0:
                     buttons.append({"title":headers[i], "payload":'''/PickSlotOnDay1{"slotSelected":"'''+headers[i]+'''"}'''})
            message = "Choose your Slot"
            #buttons.append({"title":"Sorry I am not available on this", "payload":'''/option4'''})
            dispatcher.utter_message(message, buttons=buttons)
        
            df.to_csv("timeSlots.csv", index=False)
        df = pd.read_csv("timeSlots.csv");    
        rowIndex=df[df["Days"] == originalDate].index.tolist();print(originalSlot,"originalSlot")
        presentvalue=df.iloc[rowIndex][originalSlot] ;print("presentvalue",presentvalue)
        df.at[rowIndex, originalSlot] = presentvalue+1;print(rowIndex,"rowIndex")
        df.to_csv("timeSlots.csv", index=False)
        message = "Pick the slots From Available ones"
        dispatcher.utter_message(message, buttons=buttons)
        return[SlotSet("isChangeSlot", True)]
#                      
        
        
class GetOtherAvailableDays(Action):

    def name(self) -> Text:
        return "getAllAvailableOtherDays"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("--------------getAllAvailableOtherDays----------------")
        df = pd.read_csv("timeSlots.csv");   
        daysList=df['Days'].tolist()
        buttons=[]
        for day in daysList:
            try:
                 day = dt.datetime.strptime(day, '%d-%m-%Y')
            except:
                try:
                        day = dt.datetime.strptime(day, '%d.%m.%Y')
                except:
                     try:
                        day = dt.datetime.strptime(day, '%d/%m/%Y')
                     except Exception as ex:
                        day=None;
                        message = "Please give dates in correct format"
                        dispatcher.utter_message(message)
                        return[]
                        
            if day>=dt.datetime.now():
               buttons.append({"title": day.strftime('%d-%m-%Y'), "payload":'''/updateInterviewDate{"changedDate":"'''+day.strftime('%d-%m-%Y')+'''"}'''})
        name = tracker.get_slot("name");
        message = "{} unfortunately our system is not showing any available time above those displayed".format(name)
        dispatcher.utter_message(message, buttons=buttons)
        return[]
#                       


class clear_All_slots(Action):

    def name(self) -> Text:
        return "clearSlots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("--------------clear All Slots----------------")
        return [AllSlotsReset()]
#                                 
       
        
class ActionRestarted(Action):
#""" This is for restarting the chat"""

    def name(self):
        return "action_chat_restart"
    
    def run(self, dispatcher, tracker, domain):
        return [Restarted()]
    
class Ask_UserName(Action):

    def name(self) -> Text:
        return "action_name"
#  utter_name:
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("--------------Ask username----------------")
        message = "Please provide your name , for verification"
        dispatcher.utter_message(message)
        input_str = tracker.latest_message.get('text');print("input_str",input_str)
        return[UserUttered(input_str, "/userName")] 
#                                 
    
class Verify_name(Action):

    def name(self) -> Text:
        return "verifiyUserName"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                  print("--------------verifiyUserName----------------")
                  df = pd.read_csv("Applicants.csv");
                  tab = pd.read_csv("table1.csv");
                  rowno=tab.shape[0];
                  randData=random.randint(0,rowno-1)
                  interviewData=tab.iloc[randData,:] ;
                  print("interviewData",interviewData)
                  emp=interviewData.iloc[0];print(emp,"emp")
                  company=interviewData.iloc[2];print(company,"company")
                  position=interviewData.iloc[1];print(position,"position")
                  dateRange=interviewData.iloc[7];print(dateRange,"dateRange")
                  name=interviewData.iloc[8]
                  try :
                      fromDate=dateRange.split(" ")[0];print(fromDate,"fromDate")
                      toDate=dateRange.split(" ")[-1];print(toDate,"toDate")
                  except:
                      toDate=None
                      fromDate=dateRange.split(" ")[-1]
                      
                  try:
                        fromDate = dt.datetime.strptime(fromDate, '%d-%m-%Y')
                  except:
                        try:
                                fromDate = dt.datetime.strptime(fromDate, '%d.%m.%Y')
                        except:
                             try:
                                fromDate = dt.datetime.strptime(fromDate, '%d/%m/%Y')
                             except Exception as ex:
                                fromDate=None;
                  fromDate=fromDate.strftime('%d-%m-%Y')        
                  if toDate!=None:
                      try:
                        toDate = dt.datetime.strptime(toDate, '%d-%m-%Y')
                      except:
                            try:
                                    toDate = dt.datetime.strptime(toDate, '%d.%m.%Y')
                            except:
                                 try:
                                    toDate = dt.datetime.strptime(toDate, '%d/%m/%Y')
                                 except Exception as ex:
                                    toDate=None;
                      toDate=toDate.strftime('%d-%m-%Y')
                  if toDate!= None:
                   message=name+" Howdy I am your hirepal ( fueled by hirextra.com) ,like to interface with you for "+position+" and conceivable Meeting with our customer "+company+", are you prepared to take a meeting by means of conference call on between "+fromDate+" to "+toDate+" ?"
                  else:
                   message=name+" Howdy I am your hirepal ( fueled by hirextra.com) ,like to interface with you for "+position+" and conceivable Meeting with our customer "+company+", are you prepared to take a meeting by means of conference call on "+fromDate+" ?"
                  buttons=[]
                  buttons.append({"title":"No , I am not interested in this role now", "payload":"/option1"})  
                  buttons.append({"title":"Sorry, I am not available now – I got a job already", "payload":"/option1"})  
                  buttons.append({"title":"Sorry, I am not applied for this job, please delete CV from your system", "payload":"/option1"})  
                  buttons.append({"title":"Yes I am interested but not on those dates", "payload":"/option4"})  
                  buttons.append({"title":"Yes Available", "payload":"/option5"})  
                  dispatcher.utter_message(message, buttons=buttons)
                  return[SlotSet("name", name),SlotSet("emp", emp),SlotSet("company", company),SlotSet("FromDate", fromDate),SlotSet("ToDate", toDate),SlotSet("position", position)]
        