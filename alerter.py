import check_limits

def PrintWarningInConsole(param_in_range, parameter, alert_message):
    if param_in_range:
        print(f"Warning: {parameter} {alert_message}")
        return f"Warning: {parameter} {alert_message}"
    else:
        return(PrintAlertInConsole(parameter))

def PrintAlertInConsole(parameter):
    print(f"Alert: {parameter} value out of range")
    return f"Alert: {parameter} value out of range"
def GenerateAlertMessageIfRequired(parameter, parameter_value, parameter_info, alert_messages):
    if parameter_info["alert"] == True:
        check_limits.IsMinimumTolarenceCheckOK(parameter, parameter_value, parameter_info, alert_messages)
        check_limits.IsMaximumTolarenceCheckOK(parameter, parameter_value, parameter_info, alert_messages)
        check_limits.IsTrendTolaranceCheckOK(parameter, parameter_value, parameter_info, alert_messages)
    else:
        pass
