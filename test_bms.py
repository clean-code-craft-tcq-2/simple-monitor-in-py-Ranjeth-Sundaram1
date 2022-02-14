import define_defalut_value
import check_limit

def TestBatteryStatus(alert_messages):
    parameters_info =  DefineParametersInfo()
    assert(IsParameterInRange("Temperature", 40, parameters_info["Temperature"], alert_messages) == True)
    assert(IsParameterInRange("Soc", 100, parameters_info["Soc"], alert_messages) == False)
    assert(IsBatteryOK({"Charge Rate": 1, "Temperature": 50}, parameters_info, alert_messages)==False)
    assert(IsBatteryOK({"Temperature": 50}, parameters_info, alert_messages)==False)
    assert(PrintAlertInConsole("Temperature", "parámetro acercándose al rango máximo") == "Warning: Temperature parámetro acercándose al rango máximo")
    assert(IsMinimumTolarenceCheckOK("Temperature",44,parameters_info["Temperature"], alert_messages)==False)
    assert(IsMinimumTolarenceCheckOK("Temperature",2,parameters_info["Temperature"], alert_messages)==True)
    assert(IsMaximumTolarenceCheckOK("Soc", 77.5, parameters_info["Soc"], alert_messages)==True)
    assert(IsMaximumTolarenceCheckOK("Soc", 77.5, parameters_info["Soc"], alert_messages)==True)

if __name__ == '__main__':
    alert_messages = DefineAlertMessagesForLanguage("English")
    TestBatteryStatus(alert_messages)
