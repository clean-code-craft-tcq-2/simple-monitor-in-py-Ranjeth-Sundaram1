def DefineParametersInfo():
    global defined_parameters_info
    defined_parameters_info ={}
    defined_parameters_info['Temperature']  = {'min' : 0, 'max' : 45, 'tolarance_in_percentage': 5, 'alert': True}
    defined_parameters_info['Soc']          = {'min' : 20, 'max' : 80, 'tolarance_in_percentage': 5, 'alert': True}
    defined_parameters_info['Charge Rate']  = {'trend_value' : 0.8, 'tolarance_in_percentage': 5, 'alert': False}
    return defined_parameters_info

def DefineAlertMessages():
    alert_messages = {}
    # 2: Out of Range , 1: approaching maximum tolarance , 0 : appraching minimum tolarance
    alert_messages ['English'] = {2: "parameter is out of range",  1: "parameter approaching maximum range", 0: "parameter approaching minimum range"}
    alert_messages['Spanish'] = {2: "el parámetro está fuera de rango", 1: "parámetro acercándose al rango máximo", 0: "parámetro acercándose al rango mínimo"}
    alert_messages['German'] = {2: "Parameter ist außerhalb des gültigen Bereichs", 2: "Parameter nähert sich dem maximalen Bereich", 0: "Parameter nähert sich dem Mindestbereich"}
    return alert_messages

def DefineAlertMessagesForLanguage(choosen_language):
    alert_messages = DefineAlertMessages()
    return alert_messages[choosen_language]
