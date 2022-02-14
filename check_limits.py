import alerter

def IsParameterInRange(parameter, parameter_value, parameter_info, alert_message) -> bool:
    if parameter_value in range( parameter_info['min'], parameter_info['max']):
        return True
    alerter.PrintWarningInConsole(False,parameter, alert_message[2])
    return False

def IsParameterInTrend(parameter, parameter_value, parameter_info, alert_message) -> bool:
    if parameter_value < parameter_info['trend_value']:
        return True
    alerter.PrintWarningInConsole(False, parameter, alert_message[2])
    return False

def IsMinimumTolarenceCheckOK(parameter,parameter_value, parameter_info,alert_message) -> bool:
    if "min" in parameter_info.keys():
        if parameter_value < (parameter_info['min']+parameter_info['max']*(parameter_info['tolarance_in_percentage']/100)):            
            param_in_limit = IsParameterInRange(parameter, parameter_value, parameter_info, alert_message)
            alerter.PrintWarningInConsole(param_in_limit, parameter, alert_message[0])
            return param_in_limit
        return False
    else: 
        pass

def IsMaximumTolarenceCheckOK(parameter, parameter_value, parameter_info, alert_message) -> bool:
    if "max" in parameter_info.keys():    
        if parameter_value > parameter_info['max']-parameter_info['max']*(parameter_info['tolarance_in_percentage']/100):
            param_in_limit = IsParameterInRange(parameter, parameter_value, parameter_info, alert_message)
            alerter.PrintWarningInConsole(param_in_limit, parameter, alert_message[1])
            return  param_in_limit   
    else:
        pass

def IsTrendTolaranceCheckOK(parameter, parameter_value, parameter_info, alert_message) -> bool:
    if "trend_value" in parameter_info.keys():
        if  parameter_value > (parameter_info['trend_value']-parameter_info['trend_value']*(parameter_info['tolarance_in_percentage']/100)-1):
            param_in_limit = IsParameterInTrend(parameter, parameter_value, parameter_info, alert_messages)
            alerter.PrintWarningInConsole(param_in_limit, parameter, alert_message[1])
            return  param_in_limit   
    else:
        pass

def IsBatteryParameterOK(parameter, parameter_value, parameter_info, alert_messages):
    if "trend_value" in parameter_info.keys():
        battery_status_report = IsParameterInTrend(parameter, parameter_value, parameter_info, alert_messages)
    else:
        battery_status_report = IsParameterInRange(parameter, parameter_value, parameter_info, alert_messages)
    return battery_status_report

def IsBatteryOK(InputParameterFromSensor, parameters_info, alert_messages)->bool:
    battery_status_report = []
    for parameter, parameter_value in InputParameterFromSensor.items():
        alerter.GenerateAlertMessageIfRequired(parameter, parameter_value, parameters_info[parameter], alert_messages)
        one_param_check_report = IsBatteryParameterOK(parameter, parameter_value, parameters_info[parameter], alert_messages)
        battery_status_report.append(one_param_check_report)
    if all(battery_status_report) is True:
        return True    
    return False
