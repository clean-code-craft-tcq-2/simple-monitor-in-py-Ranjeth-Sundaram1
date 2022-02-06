
def TemperatureIsNOK(temperature:float)->bool:
    if temperature < 0 or temperature > 45:
        print('Temperature is out of range!')
        return False
    else:
        return True

def SocIsNOK(soc:float)->bool:
    if soc < 20 or soc > 80:
        print('State of Charge is out of range!')
        return False
    else:
        return True

def ChargerateIsNOK(charge_rate:float)->bool:
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    else:
        return True

def IsBatteryOK(temperature, soc, charge_rate)->bool:
    if TemperatureIsNOK(temperature) and SocIsNOK(soc) and ChargerateIsNOK(charge_rate):
        return True
    else:
        return False

if __name__ == '__main__':
    assert(IsBatteryOK(25, 70, 0.7) is True)
    assert(IsBatteryOK(50, 85, 0) is False)
    assert(IsBatteryOK(-50, 85, 0) is False)
    assert(IsBatteryOK(-50, 85, 0.9) is False)
