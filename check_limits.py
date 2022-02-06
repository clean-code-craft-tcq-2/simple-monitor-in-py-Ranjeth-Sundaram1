def DefineParametersRange():
    parameter_range ={}
    parameter_range['temperature']  = {min : 0, max : 45}
    parameter_range['soc']          = {min : 20, max : 80}
    parameter_range['charge_rate']  = {min : 0.8}
    return parameter_range
    
def DefineParametersMinLimit():
    min_temperature = 0

def TemperatureIsNOK(Parameter_range, temperature:float)->bool:
    if temperature < Parameter_range['temperature']['min'] or temperature > Parameter_range['temperature']['max']:
        print('Temperature is out of range!')
        return False
    return True

def SocIsNOK(Parameter_range, soc:float)->bool:
    if soc < Parameter_range['soc']['min'] or soc > Parameter_range['soc']['max']:
        print('State of Charge is out of range!')
        return False
    return True

def ChargerateIsNOK(Parameter_range, charge_rate:float)->bool:
    if charge_rate > Parameter_range['charge_rate']['min']:
        print('Charge rate is out of range!')
        return False
    return True

def IsBatteryOK(Parameter_range, temperature, soc, charge_rate)->bool:
    if TemperatureIsNOK(Parameter_range, temperature) or SocIsNOK(Parameter_range, soc) or ChargerateIsNOK(Parameter_range, charge_rate):
        return False
    else:
        return True

if __name__ == '__main__':
    Parameter_range = DefineParametersRange()
    assert(IsBatteryOK(Parameter_range, 25, 70, 0.7) is True)
    assert(IsBatteryOK(Parameter_range, 50, 85, 0) is False)
    assert(IsBatteryOK(Parameter_range, -50, 85, 0) is False)
    assert(IsBatteryOK(Parameter_range, -50, 85, 0.9) is False)
