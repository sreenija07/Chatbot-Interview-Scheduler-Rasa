## initial
* greet
  - verifiyUserName
  - slot{"name": "Shiv"}
  - slot{"emp": "Kumar"}
  - slot{"company": "ABC Company"}
  - slot{"FromDate": "23-08-2020"}
  - slot{"position": "Full Stack Developer"}
  - slot{"ToDate": "27-08-2020"}

  
## fallback story
* out_of_scope
  - action_default_fallback  
  
## FirstOption
* greet
  - verifiyUserName
* option1
  - utter_close_chat
 
 
## FourthOption
* greet
  - verifiyUserName
* option4
  - utter_for_available_dates
* getDates{"FromDate":"12-2-2020","ToDate":"15-2-2020"}
  - slot{"SelectDate1":"1-2-2019"}
  - ActionGetDateRange
* DateString{"RequireNextDay":true,"SelectDate1":"1-2-2019"}
  - slot{"SelectDate2":"11-2-2019"}
  - ActionSelectNextDate
* DateString{"RequireNextDay":true,"SelectDate1":"1-2-2019","SelectDate2":"11-2-2019"}
  - ActionSelectNextDate
* DateString{"RequireNextDay":true,"SelectDate1":"1-2-2019","SelectDate2":"11-2-2019","SelectDate2":"13-2-2019"}
  - ActionSelectNextDate
* DateString{"RequireNextDay":false}
  - ActionUtterUpdatedDates
  
## FourthOption2
* greet
  - verifiyUserName
* option4
  - utter_for_available_dates
* getDates{"FromDate":"1-2-2020"}
  - slot{"SelectDate1":"1-2-2020"}
  - ActionGetDateRange
* DateString{"RequireNextDay":false}
  - ActionUtterUpdatedDates
  
  
## FourthOption3
* greet
  - verifiyUserName
* option4
  - utter_for_available_dates
* getDates{"FromDate":"8.12.2020","ToDate":"5.12.2020"}
  - slot{"SelectDate1":"23-12-2020"}
  - ActionGetDateRange
* DateString{"RequireNextDay":true,"SelectDate1":"23-12-2020"}
  - slot{"SelectDate2":"24-12-2020"}
  - ActionSelectNextDate
* DateString{"RequireNextDay":true,"SelectDate1":"23-12-2020","SelectDate2":"24-12-2020"}
  - ActionSelectNextDate
* DateString{"RequireNextDay":true,"SelectDate1":"23-12-2020","SelectDate2":"24-12-2020","SelectDate2":"25-2-2019"}
  - ActionSelectNextDate
* DateString{"RequireNextDay":false}
  - ActionUtterUpdatedDates
 
## FourthOption3
* greet
  - verifiyUserName
* option4
  - utter_for_available_dates
* getDates{"FromDate":"06.4.2020"}
  - slot{"SelectDate1":"06-4-2020"}
  - ActionGetDateRange
* DateString{"RequireNextDay":false}
  - ActionUtterUpdatedDates
  
## FourthOption4
* greet
  - verifiyUserName
* option4
  - utter_for_available_dates
* getDates{"FromDate":"18/3/2020","ToDate":"12/03/2020"}
  - slot{"SelectDate1":"2.1.2020"}
  - ActionGetDateRange
* DateString{"RequireNextDay":true,"SelectDate1":"2-1-2020"}
  - slot{"SelectDate2":"4-1-2020"}
  - ActionSelectNextDate
* DateString{"RequireNextDay":true,"SelectDate1":"2-1-2020","SelectDate2":"4-1-2020"}
  - ActionSelectNextDate
* DateString{"RequireNextDay":true,"SelectDate1":"2-1-2020","SelectDate2":"4-1-2020","SelectDate2":"5-1-2019"}
  - ActionSelectNextDate
* DateString{"RequireNextDay":false}
  - ActionUtterUpdatedDates
  
 
## FourthOption4
* greet
  - verifiyUserName
* option4
  - utter_for_available_dates
* getDates{"FromDate":"29/7/2020"}
  - ActionGetDateRange
* DateString{"RequireNextDay":false}
  - ActionUtterUpdatedDates
  
## FifthOption1
* greet
  - verifiyUserName
* option5
  - ActionAskSlots
* PickSlotOnDay1{"slotSelected":"15 pm - 16 pm"}
  - ActionSlotSelect
* confirmSlot1
  - utter_confirm_slot
  - utter_confirm_slot2
  
## FifthOption1.2
* greet
  - verifiyUserName
* option5
  - ActionAskSlots
* PickSlotOnDay1{"slotSelected":"12 am - 13 pm"}
  - ActionSlotSelect
* confirmSlot1
  - utter_confirm_slot
  - utter_confirm_slot2
  
## FifthOption2
* greet
  - verifiyUserName
* option5
  - ActionAskSlots
* PickSlotOnDay1{"slotSelected":"12 pm - 13 pm"}
  - ActionSlotSelect
* askForSlotTimeChange
  - utter_option_to_change_date_or_only_time
* changeDateInterview
  - ActionChangeDateSelect
* getDates
  - slot{"SelectDate1":"2.3.2020"}
  - ActionGetDateRange
  - updateInterviewDate
  
  
  
## FifthOption2
* greet
  - verifiyUserName
* option5
  - ActionAskSlots
* PickSlotOnDay1{"slotSelected":"13 pm - 14 pm"}
  - ActionSlotSelect
* askForSlotTimeChange
  - utter_option_to_change_date_or_only_time
* changeDateInterview
  - ActionChangeDateSelect
* getDates
  - slot{"SelectDate1":"2.1.2020"}
  - ActionGetDateRange
  - updateInterviewDate
  - slot{"daySelected": "2-11-2020"}
  - slot{"isChangeSlot": "True"}
  
  
  
  
## FifthOption2-2-2
* greet
  - verifiyUserName
* option5
  - ActionAskSlots
* PickSlotOnDay1{"slotSelected":"13 pm - 14 pm"}
  - ActionSlotSelect
* askForSlotTimeChange
  - utter_option_to_change_date_or_only_time
* changeSlotInterview
  - updateInterviewSlot
  - slot{"isChangeSlot": "True"}

## FifthOption2-2-3
* greet
  - verifiyUserName
* option5
  - ActionAskSlots
* PickSlotOnDay1{"slotSelected":"13 pm - 14 pm"}
  - ActionSlotSelect
* otherDays
  - getAllAvailableOtherDays
  
##clear Story
* clear
- clearSlots

##clear Story2
* clear
- clearSlots


  
  
  




  
  


 



