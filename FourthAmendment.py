from MainClasses import *

def adf():
   
   """
   creates the ADF for the domain
   """
   adf = ADF('FourthAmendment') 

   #non leaf 
   adf.addNodes('Decide',['Privacy','Exigency'],['warantless search violates the fourth amendment','warantless search did not violate the fourth amendment','wrong decision'])
   adf.addNodes('Privacy',['ExpectationOfPrivacyInUse and ( not SubjectToInspectionRegulation or not VisibilityOfItem )','not PublicParking and not_authorised','OnlyVehicleContainer and not VisibilityOfItem'],['high expectation of privacy not justified under automobile exception','high expectation of privacy obtained warrant was issued by neutral and detached magustrate and not autorized','privacy is not justified under automobile exception','reduced expectation of privacy'])
   adf.addNodes('Exigency',['( Mobile and ExigencyWhenApproached and ProbableCauseToSearchVehicle )', 'reject EaseWarrant'],['justified under automobile exception cite carroll v us','reduce expectation of exigency','reduce expectation of exigency'])
   adf.addNodes('ExpectationOfPrivacyInUse',['( Accomodation and Residence ) or PrivateContentsCarriage'],['there is a high expectation of privacy in use','default low expectation of privacy in use'])
   adf.addNodes('Residence',['ConnectedServices'],['connected to one or more main living services','default not connected to one or more main living services'])
   adf.addNodes('PrivateContentsCarriage',['ProtectionType and GoodsCarried','reject GoodsCarried'],['private contents','private contents but not protected','default contents are not considered private'])
   adf.addNodes('Accomodation',['AccomodationSpaces or RoomsFunction'],['the place was used for accomodation','default the place was used for accomodation'])
   adf.addNodes('SubjectToInspectionRegulation',['reject Licence and RestrictedArea','Licence'],['subject to regular inspection but the search was allocated at restricted area','subject to regular inspection','it is not subject to regular inspection'])
   adf.addNodes('VisibilityOfItem',['OnPublicView or CanBeSeen'],['item is visible to public','default it is not visible to public'])
   adf.addNodes('ExigencyWhenApproached',['UrgentStatus or ( CapableToMove and ( PublicParking or PublicLocation ) )'],['there was exigency when approached','there was no exigency when approached'])
   adf.addNodes('Mobile',['Automobile or Vessel or Towable or LargeContainer or MovableContainer'],['it is a mobile','default it is not a mobile'])
   adf.addNodes('EaseWarrant',['not RiskofLosingEvidence or ( AvailiabilityofMagistrate and AuthorityOfAvailiableMagistrate ) '],['it is easy to obtain a warrant','it is not easy to obain a warrant'])
   adf.addNodes('ProbableCauseToSearchVehicle',['LegalSearchScope and UrgentReasonToSearch and AuthorizedOriginOfProbableCause','reject UrgentReasonToSearch and AuthorizedOriginOfProbableCause'],['there is a probable cause to search the vehicle','there is a probable cause to search the vehicle but the search scope was illegal','default there is no probable cause to search the vehicle'])
   adf.addNodes('AuthorizedOriginOfProbableCause',['Information or Observation or Procedure','not Information'],['there was an authorized origin of probable cause','default origin of probable cause is not authorized or not clarified',' '])
   adf.addNodes('UrgentReasonToSearch',['PublicSafety or Crime'],['the main reason to search was urgent','default the main reason to immediate search is not clarified'])
   adf.addNodes('LegalSearchScope',['WholeVehicle','reject OnlyVehicleContainer and SearchPlace'],['the search scope is legal','the search scope is illegal','default the serach scope is illegal'])
   
   #blf
   adf.addMulti('Automobile',['car','mobile_home'],['it is a vehicle cite carroll v us','it is a mobile home vehicle cite carney v california','default it is not an automobile cite carroll v us'],'If the vehicle that was searched was an automobile select the correct type:')
   adf.addMulti('Vessel',['not Automobile and vessel','not Automobile and sailboat','not Automobile and rowboat'],['motorboat is a vessel cite carroll v us','sailboat is a vessel cite carroll v us','rowboat is a vessel cite carroll v us','default it is not a vessel cite carroll v us'],'If the vehicle that was searched was a vessel select the correct type:')
   adf.addMulti('Towable',['trailer','wagon','cart'],['trailer is towable cite carroll v us','wagon is towable cite carroll v us','cart is towable cite carroll v us','default it is not towable cite carroll v us'],'If the vehicle that was searched was towable select the correct type:')
   adf.addMulti('LargeContainer',['not Vessel and foot_locker','not Vessel and goods_container'],['footlocker is a large container cite us v chadwick','large goods container','default no large containers'],'If a large container was searched select the correct type')
   adf.addMulti('MovableContainer',['pouch','paper_bag','briefcase','suitcase'],['pouch is a movable container','paper bag is a movable container','brief case is a movable container','suitcase is a movable container','default it is not a movable container'],'If a movable container was searched select the correct type')
   adf.addMulti('AuthorityOfAvailiableMagistrate',['authorised','reject not_authorised'],['neutral and detached authorized magistrate are availiabe cite johnson v us','warrant issued by unauthorized magistrate cite johnson v us','default authorized magistrate are not availiable'],'Is an authorised magistrate availiable?')
   adf.addNodes('RiskofLosingEvidence',['ExigencyWhenApproached','reject near_court'],['there is risk to lose evidence','there was no risk to lose evidence','default there was no risk to lose evidence'])
   adf.addNodes('near_court',question='Was there a risk of losing evidence?')
   adf.addMulti('AvailiabilityofMagistrate',['working_time','reject overnight'],['magistrate availiabe during working hours','magistrate are not availiable overnight','default magistrate are not availiable'],'What is the availiability, if any, of the magistrate?')
   adf.addMulti('Licence',['vehicle','motorhome','Automobile'],['has a vehicle licence','has a special motorhome licence','default all automobiles are registered','no automobile'],'What type of vehicle licence, if any, was held?')
   adf.addMulti('RestrictedArea',['airport','home','police_station'],['airport is a restricted area','private home is a restricted area','police station is a restricted area','default not restricted area'],'Did the search take place in a restricted area?')
   adf.addNodes('OnPublicView',['OnSeat'],['items were on the seat it is on public view','default item is not on public view or details are not provided'])
   adf.addNodes('OnSeat',question="Where the items on the seat in public view?")
   adf.addMulti('CanBeSeen',['not OnPublicView and public_view','not OnPublicView and on_floor'],['items can be seen by public','items were no floor it can be seen by public','default can not be seen by public or details are not provided'],'Were the items on the floor or in a place that could be seen by the public?')
   adf.addMulti('CannotBeSeen',['not CanBeSeen and opaque_container','not CanBeSeen and glovebox','not CanBeSeen and boot'],['items were in an opaque container it can not be seen by public','items were inside the glove box it can not be seen by public','items were inside the boot it can be not seen by public','default it is not clear that items can not be seen'],'Were the items not viewable to the public in one of the following?')
   adf.addMulti('UrgentStatus',['Mobile and moving','reject Mobile and stationary','reject Mobile and parked','reject Mobile and crashed'],['there was an urgent status when vehicle is moving cite carroll v us','there was no urgent status automobile found stationary','there was no urgent status automobile was parked','there was no urgent status automobile was crashed','default there is no urgent status'],'Was the vehicle any of the following:')
   adf.addMulti('CapableToMove',['Mobile and not UrgentStatus and ( driver_in or occupied or curtains_open or motive_force )', 'Mobile and not moving and not ( driver_in or occupied or curtains_open or motive_force )'],['the vehicle is capable to move','default the vehicle is capable to move',' '],'Was the vehicle capable to move for any of the following reasons?')
   adf.addMulti('PublicParking',['( UrgentStatus or CapableToMove ) and ( parked_on_highway or ( parking_lot and not dwelling ) )','reject ( UrgentStatus or CapableToMove ) and ( dwelling or ( ( ownland or work or rented_land ) and not parking_lot ) )','reject ( UrgentStatus or CapableToMove ) and UrgentStatus'],['the vehicle was parked in public parking','the vehicle was parked in private parking','default vehicle was not parked','default vehicle parking type is not specified'],'Where was the vehicle parked, if anywhere?')
   adf.addMulti('PublicLocation',['( UrgentStatus or CapableToMove ) and ( highway or downtown )','reject ( UrgentStatus or CapableToMove ) and ( dwelling or urban_residential or suburban or rural )'],['the vehicle was in public location','the vehicle was in private location','default vehicle location is not specified'],'In what location was the vehicle?')
   adf.addMulti('PermittedDuration',['short_stay','overnight','long_stay'],['the vehicle was parked for a short time','the vehicle was parked for one overnight','the vehicle was parked for over one night long period','default the vehicle was parked for unknown period'],'For how long was the vehicle parked?')
   adf.addMulti('Information',['public_informant','agent_officer'],['received information from public informant','received information from agent officer','default the original probable cause is not by information received'],'Did the original probable cause come from information received from:')
   adf.addMulti('Observation',['not Information and the_public','not Information and an_agent_officer'],['observed from public observer','observed from agent officer','default the original probable cause is not by observation'],'Was the original probable cause observed from:')
   adf.addMulti('Procedure',['not Observation and incident_to_arrest','not Observation and multiple_parking','not Observation and inspection_regulation'],['search incident to arrest cite harris v us and preseton v us','multiple parking procedure','inspection procedure cite harris v us and preston v us','default the original probable cause is not a procedure or procedure is not clarified'],'Was the original probable cause a procedure such as:')
   adf.addMulti('PublicSafety',['weapon and illegal_substance','weapon','illegal_substance','not weapon or not illegal_substance'],['main reason to search was to protect the public','main reason to search was to protect the public cite harris v us and preston v us','main reason to search was to protect the public cite carol v us','default main reason to search was to protect the public','main reason to search was not to protect the public'],'Was the main reason to search due to:')
   adf.addMulti('Crime',['smuggling or dealing or murder','robbery'],['main reason to search was due to a crime','main reason to search was not due to a crime','default main reason to search was not due to a crime'],'Had any of these crimes preempted the search?')
   adf.addNodes('WholeVehicle',['all_parts'],['all vehicle parts have been searched cite carrol v us and us v ross','default it is not clear if all vehicle parts have been searched'])
   adf.addNodes('all_parts',question='Have all the vehicle parts been searched?')
   adf.addMulti('OnlyVehicleContainer',['not WholeVehicle and ( car_trunk and glove_compartment )','not WholeVehicle and car_trunk','not WholeVehicle and glove_compartment'],['only vehicle containers have been searched','only vehicle containers have been searched cite us v chadwick and arkansas v sanders','only vehicle containers have been searched','default it is not clear which part of vehicle is searched'],'Were any of the following parts of the vehicle searched?')
   adf.addMulti('SearchPlace',['police_station_location and automobile_location','reject police_station_location','reject garage','automobile_location'],['the vehicle was searched twice at the same automobile location and at police station','the vehicle was searched at police station','the vehicle was searched at a garage','the vehicle was searched at the same automobile location','default the vehicle searching location is not clarified'],'Where was the vehicle searched?')
   adf.addMulti('GoodsCarried',['personal_effects or papers or commercial_items','reject weapons or illegal_substance','money'],['private goods','illegal goods','private goods','default goods carried are unknown'],'Which, if any, of these goods were being carried?')
   adf.addMulti('ProtectionType',['reject open','reject closed','locked','double_locked'],['not protected','just closed but not protected','locked and protected','double locked and protected','default protection level can not be determined'],'What was the protection level of the goods?')
   adf.addMulti('ConnectedServices',['gas and water','electricity and water','gas','electricity','water'],['gas and water services were connected','electricity and water services were connected','gas service was connected','electricity service was connected','water service was connected','default none of living main services are specified'],'Were any of the following services connected?')
   adf.addMulti('AccomodationSpaces',['cab and suitable_accomodation_space','reject cab','suitable_accomodation_space'],['consists of a cab and suitable accomodation space','consists of a cab only','consists of suitable accomodation space','default vehicle accomodation spaces are not clarified'],'Does the vehicle accomodation consist of:')
   adf.addMulti('RoomsFunction',['not AccomodationSpaces and ( bedroom or bathroom or kitchen or living_room )'],['essential room for accomodation','default there are no rooms or rooms function is not specified'],'Are there any rooms in the accomodation space?')
   
   #set to stop the program prompting it be set as a question but excluded from the question order 
   adf.addNodes('not_authorised',question='<>')
   
   adf.questionOrder = ['Automobile','Vessel','Towable','LargeContainer','MovableContainer','AuthorityOfAvailiableMagistrate','near_court','AvailiabilityofMagistrate','Licence','RestrictedArea','OnSeat','CanBeSeen','CannotBeSeen','UrgentStatus','CapableToMove','PublicParking','PublicLocation','PermittedDuration','Information','Observation','Procedure','PublicSafety','Crime','all_parts','OnlyVehicleContainer','SearchPlace','GoodsCarried','ProtectionType','ConnectedServices','AccomodationSpaces','RoomsFunction']
   
   return adf

def cases():
   """
   test cases
   """
   cvus = ['car','moving','public_informant','illegal_substance','all_parts','automobile_location','illegal_substance'] #pass
   cvm = ['car','ft015w','moving','highway','inspection_regulation','robbery','all_parts'] #pass
   #cvnh = ['car','not_authorised','parked','dwelling','dwelling','inspection_regulation','murder','all_parts'] #can't tell
   cvd = ['car','public_view','boot','crashed','parked_on_highway','dwelling','inspection_regulation','murder','all_parts','garage'] #pass
   sdvo = ['car','paper_bag','glovebox','parked','parking_lot','multiple_parking','illegal_substance','all_parts','automobile_location','illegal_substance'] #pass
   usvc = ['car','foot_locker','police_station','boot','parked','parking_lot','public_informant','illegal_substance','car_trunk','police_station_location','illegal_substance','double_locked'] #pass
   avs = ['car','goods_container','suitcase','airport','boot','moving','agent_officer','illegal_substance','car_trunk','illegal_substance','closed'] #pass
   usvr = ['car','paper_bag','police_station','parked','parking_lot','public_informant','illegal_substance','all_parts','car_trunk','automobile_location','police_station_location','illegal_substance','money','closed'] #pass
   cvc = ['mobile_home','paper_bag','near_court','motorhome','police_station','parked','driver_in','parking_lot','downtown','public_informant','the_public','illegal_substance','all_parts','police_station_location','automobile_location','illegal_substance','closed','cab','suitable_accomodation_space','bedroom','kitchen'] #pass
   cva = ['car','paper_bag','police_station','boot','moving','highway','public_informant','illegal_substance','car_trunk','automobile_location','illegal_substance','closed'] #pass
   
   cases = {'Carroll v United States':cvus,'Chambers v Maroneys':cvm,'Cady v Dombrowski':cvd,'South Dakota v Opperman':sdvo,'United States v Chadwick':usvc,'Arkansas v Sanders':avs,'United States v Ross':usvr,'California v Carney':cvc,'California v Acevedo': cva}#,'Coolidge v New Hampshire':cvnh}
   
   return cases

def expectedOutcomeCases():
   """
   first factor is the outcome - the other factors are those from the prolog program of the domain 
   
   """
 
   cvus = ['warantless search did not violate the fourth amendment','car','moving','public_informant','illegal_substance','all_parts','automobile_location','illegal_substance','Exigency','RiskofLosingEvidence','SubjectToInspectionRegulation','Licence','ProbableCauseToSearchVehicle','LegalSearchScope','SearchPlace','WholeVehicle','UrgentReasonToSearch','PublicSafety','AuthorizedOriginOfProbableCause','Information','ExigencyWhenApproached','UrgentStatus','Mobile','Automobile'] #pass
   cvm = ['warantless search did not violate the fourth amendment','car','ft015w','moving','highway','inspection_regulation','robbery','all_parts','RiskofLosingEvidence','SubjectToInspectionRegulation','Licence','ProbableCauseToSearchVehicle','LegalSearchScope','WholeVehicle','UrgentReasonToSearch','Crime','PublicSafety','AuthorizedOriginOfProbableCause','Procedure','ExigencyWhenApproached','PublicLocation','UrgentStatus','Mobile','Automobile','Exigency'] #pass
   cvd = ['warantless search did not violate the fourth amendment','car','public_view','boot','crashed','parked_on_highway','dwelling','inspection_regulation','murder','all_parts','garage','RiskofLosingEvidence','VisibilityOfItem','CanBeSeen','SubjectToInspectionRegulation','Licence','ProbableCauseToSearchVehicle','LegalSearchScope','WholeVehicle','UrgentReasonToSearch','Crime','PublicSafety','AuthorizedOriginOfProbableCause','Procedure','ExigencyWhenApproached','PublicParking','CapableToMove','Mobile','Automobile','Exigency'] #pass
   sdvo = ['warantless search did not violate the fourth amendment','car','paper_bag','glovebox','parked','parking_lot','multiple_parking','illegal_substance','all_parts','automobile_location','illegal_substance','RiskofLosingEvidence','CannotBeSeen','SubjectToInspectionRegulation','Licence','ProbableCauseToSearchVehicle','LegalSearchScope','SearchPlace','WholeVehicle','UrgentReasonToSearch','PublicSafety','AuthorizedOriginOfProbableCause','Procedure','ExigencyWhenApproached','PublicParking','CapableToMove','Mobile','MovableContainer','Automobile','Exigency'] #pass
   usvc = ['warantless search violates the fourth amendment','car','foot_locker','police_station','boot','parked','parking_lot','public_informant','illegal_substance','car_trunk','police_station_location','illegal_substance','double_locked','RiskofLosingEvidence','ProtectionType','CannotBeSeen','RestrictedArea','Licence','OnlyVehicleContainer','UrgentReasonToSearch','PublicSafety','AuthorizedOriginOfProbableCause','Information','ExigencyWhenApproached','PublicParking','CapableToMove','Mobile','LargeContainer','Automobile','Privacy'] #pass
   avs = ['warantless search violates the fourth amendment','car','goods_container','suitcase','airport','boot','moving','agent_officer','illegal_substance','car_trunk','illegal_substance','closed','RiskofLosingEvidence','CannotBeSeen','RestrictedArea','Licence','OnlyVehicleContainer','UrgentReasonToSearch','PublicSafety','AuthorizedOriginOfProbableCause','Information','ExigencyWhenApproached','UrgentStatus','Mobile','MovableContainer','LargeContainer','Automobile','Privacy'] #pass
   usvr = ['warantless search did not violate the fourth amendment','car','paper_bag','police_station','parked','parking_lot','public_informant','illegal_substance','all_parts','car_trunk','automobile_location','police_station_location','illegal_substance','money','closed','RiskofLosingEvidence','RestrictedArea','Licence','ProbableCauseToSearchVehicle','LegalSearchScope','SearchPlace','WholeVehicle','UrgentReasonToSearch','PublicSafety','AuthorizedOriginOfProbableCause','Information','ExigencyWhenApproached','PublicParking','CapableToMove','Mobile','MovableContainer','Automobile','Exigency'] #pass
   cvc = ['warantless search did not violate the fourth amendment','mobile_home','paper_bag','near_court','motorhome','police_station','parked','driver_in','parking_lot','downtown','public_informant','the_public','illegal_substance','all_parts','police_station_location','automobile_location','illegal_substance','closed','cab','suitable_accomodation_space','bedroom','kitchen','RiskofLosingEvidence','Accomodation','AccomodationSpaces','RestrictedArea','Licence','ProbableCauseToSearchVehicle','LegalSearchScope','SearchPlace','WholeVehicle','UrgentReasonToSearch','PublicSafety','AuthorizedOriginOfProbableCause','Information','ExigencyWhenApproached','PublicParking','PublicLocation','CapableToMove','Mobile','MovableContainer','Automobile','Exigency'] #pass
   cva = ['warantless search violates the fourth amendment','car','paper_bag','police_station','boot','moving','highway','public_informant','illegal_substance','car_trunk','automobile_location','illegal_substance','closed','RiskofLosingEvidence','CannotBeSeen','RestrictedArea','Licence','SearchPlace','OnlyVehicleContainer','UrgentReasonToSearch','PublicSafety','AuthorizedOriginOfProbableCause','Information','ExigencyWhenApproached','PublicLocation','UrgentStatus','Mobile','MovableContainer','Automobile','Privacy'] #pass

   #prolog for this case is not fully functional so cannot obtain an accurate expected list
   #cvnh = ['warantless search violates the fourth amendment','car','not_authorised','parked','dwelling','dwelling','inspection_regulation','murder','all_parts']
   
   cases = {'Carroll v United States':cvus,'Chambers v Maroneys':cvm,'Cady v Dombrowski':cvd,'South Dakota v Opperman':sdvo,'United States v Chadwick':usvc,'Arkansas v Sanders':avs,'United States v Ross':usvr,'California v Carney':cvc,'California v Acevedo': cva}#,'Coolidge v New Hampshire':cvnh}
   
   return cases

