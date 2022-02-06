def DefineParametersRange():
    parameter_range ={}
    parameter_range['temperature']  = {'min' : 0, 'max' : 45}
    parameter_range['soc']          = {'min' : 20, 'max' : 80}
    parameter_range['charge_rate']  = {'max' : 0.8}
    return parameter_range
    
def DefineParametersMinLimit():
    min_temperature = 0

def TemperatureIsOK(temperature_range, temperature:float)->bool:
    if temperature < temperature_range['min'] or temperature > temperature_range['max']:
        print('Temperature is out of range!')
        return False
    return True

def SocIsOK(soc_range, soc:float)->bool:
    if soc < soc_range['min'] or soc > soc_range['max']:
        print('State of Charge is out of range!')
        return False
    return True

def ChargerateIsOK(charge_rate_range, charge_rate:float)->bool:
    if charge_rate > charge_rate_range['max']:
        print('Charge rate is out of range!')
        return False
    return True

def IsBatteryOK(Parameter_range, temperature, soc, charge_rate)->bool:
    if TemperatureIsOK(Parameter_range['temperature'], temperature) and SocIsOK(Parameter_range['soc'], soc) and ChargerateIsOK(Parameter_range['charge_rate'], charge_rate):
        return True
    else:
        return False

if __name__ == '__main__':
    Parameter_range = DefineParametersRange()
    assert(TemperatureIsOK(Parameter_range['temperature'], 40) is True)
    assert(TemperatureIsOK(Parameter_range['temperature'], 100) is False)
    assert(SocIsOK(Parameter_range['soc'], 10) is False)
    assert(SocIsOK(Parameter_range['soc'], 50) is True)
    assert(ChargerateIsOK(Parameter_range['charge_rate'], 1) is False)
    assert(ChargerateIsOK(Parameter_range['charge_rate'], 0.5) is True)
    assert(IsBatteryOK(Parameter_range, 25, 70, 0.7) is True)
    assert(IsBatteryOK(Parameter_range, 50, 85, 0) is False)
    assert(IsBatteryOK(Parameter_range, -50, 85, 0) is False)
    assert(IsBatteryOK(Parameter_range, -50, 85, 0.9) is False)
