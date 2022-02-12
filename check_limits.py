def DefineParametersInfo():
    global defined_parameters_info
    defined_parameters_info ={}
    defined_parameters_info['Temperature']  = {'min' : 0, 'max' : 45, 'tolarance_in_percentage': 5}
    defined_parameters_info['Soc']          = {'min' : 20, 'max' : 80, 'tolarance_in_percentage': 5}
    defined_parameters_info['Charge Rate']  = {'trend_value' : 0.8, 'tolarance_in_percentage': 5}
    return defined_parameters_info

def DefineAlertMessages():
    alert_messages = {}
    # 2: Out of Range , 1: approaching maximum tolarance , 0 : appraching minimum tolarance
    alert_messages ['English'] = {2: "parameter is out of range",  1: "parameter approaching maximum range", 1: "parameter approaching minimum range"}
    alert_messages['Spanish'] = {2: "el parámetro está fuera de rango", 1: "parámetro acercándose al rango máximo", 1: "parámetro acercándose al rango mínimo"}
    alert_messages['German'] = {2: "Parameter ist außerhalb des gültigen Bereichs", 2: "Parameter nähert sich dem maximalen Bereich", 1: "Parameter nähert sich dem Mindestbereich"}
    return alert_messages

def DefineAlertMessagesForLanguage(choosen_language):
    alert_messages = DefineAlertMessages()
    return alert_messages[choosen_language]

def IsParameterInRange(parameter, parameter_value, parameter_info, alert_messages) -> bool:
    if parameter_value in range(parameter_info['min'], parameter_info['max'], ):
        return True
    PrintAlertInConsole(parameter, alert_messages[2])
    return False

def IsParameterInTrend(parameter, parameter_value, parameter_info, alert_messages) -> bool:
    if parameter_value < parameter_info['trend_value']:
        return True
    PrintAlertInConsole(parameter, alert_messages[2])
    return False

def IsMinimumTolarenceCheckOK(parameter,parameter_value, parameter_info,alert_message) -> bool:
    if parameter_value not in range(parameter_info['min'], (parameter_info['min']+parameter_info['min']*(parameter_info['tolarance_in_percentage']/100))):
        return True
    PrintAlertInConsole(parameter, alert_message[0])
    return False

def IsMaximumTolarenceCheckOK(parameter, parameter_value, parameter_info, alert__message) -> bool:
    if parameter_value not in range(parameter_info['max'], (parameter_info['max']+parameter_info['max']*(parameter_info['tolarance_in_percentage']/100))):
        return True
    PrintAlertInConsole(parameter, alert__message[1])
    return False

def PrintAlertInConsole(parameter, alert_message):
    print (f"{parameter} {alert_message}")

def IsBatteryOK(InputParameterFromSensor, parameters_info, alert_messages)->bool:
    battery_status_report = True
    for parameter, parameter_value in InputParameterFromSensor.items():
        if "trend_value" in parameters_info[parameter].keys():
            battery_status_report = IsParameterInTrend(parameter, parameter_value, parameters_info[parameter], alert_messages)
        else:
            battery_status_report = IsParameterInRange(parameter, parameter_value, parameters_info[parameter], alert_messages)
        if battery_status_report == False:
            return False
        else:
            IsMinimumTolarenceCheckOK(parameter, parameter_value, parameters_info[parameter],alert_messages)
            IsMaximumTolarenceCheckOK(parameter, parameter_value, parameters_info[parameter],alert_messages)
    return True

def TestBatteryStatus(alert_messages, parameters_info):
    parameters_info =  DefineParametersInfo()
    assert(IsParameterInRange("Temperature", 40, parameters_info["Temperature"], alert_messages))

if __name__ == '__main__':
    alert_messages = DefineAlertMessagesForLanguage("English")
    TestBatteryStatus(alert_messages)
