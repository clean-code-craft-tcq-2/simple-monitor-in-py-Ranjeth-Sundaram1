import define_defalut_value
import check_limit

def TestBatteryStatus(alert_messages):
    
    parameters_info = define_defalut_value.DefineParametersInfo()
    assert(check_limit.IsParameterInRange("Temperature", 40, parameters_info["Temperature"], alert_messages) == True)
    assert(check_limit.IsParameterInRange("Soc", 100, parameters_info["Soc"], alert_messages) == False)
    assert(check_limit.IsBatteryOK({"Charge Rate": 1, "Temperature": 50, "Soc": 77.5}, parameters_info, alert_messages) == False)
    assert(check_limit.IsBatteryOK({"Temperature": 50}, parameters_info, alert_messages) == False)
    assert(check_limit.PrintAlertInConsole("Temperature", "parámetro acercándose al rango máximo") == "Warning: Temperature parámetro acercándose al rango máximo")
    assert(check_limit.IsMinimumTolarenceCheckOK("Temperature", 44, parameters_info["Temperature"], alert_messages) == False)
    assert(check_limit.IsMinimumTolarenceCheckOK("Temperature", 2, parameters_info["Temperature"], alert_messages) == True)
    assert(check_limit.IsMaximumTolarenceCheckOK("Soc", 77.5, parameters_info["Soc"], alert_messages) == True)
    assert(check_limit.IsMaximumTolarenceCheckOK("Soc", 77.5, parameters_info["Soc"], alert_messages) == True)

if __name__ == '__main__':
    
    alert_messages = define_defalut_value.DefineAlertMessagesForLanguage("English")
    TestBatteryStatus(alert_messages)
