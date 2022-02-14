import check_limits
def PrintAlertInConsole(parameter, alert_message):
    print (f"Warning: {parameter} {alert_message}")
    return f"Warning: {parameter} {alert_message}"

def GenerateAlertMessageIfRequired(parameter, parameter_value, parameter_info,alert_messages):
    if parameter_info["alert"] == True:
        check_limits.IsMinimumTolarenceCheckOK(parameter, parameter_value, parameter_info,alert_messages)
        check_limits.IsMaximumTolarenceCheckOK(parameter, parameter_value, parameter_info,alert_messages)  
        check_limits.IsTrendTolaranceCheckOK(parameter, parameter_value, parameter_info,alert_messages)  
    else:
        pass
