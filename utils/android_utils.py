import subprocess

def get_device_udid():
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    lines = result.stdout.split('\n')
    device = lines[1]
    if device:
        udid = device.split("\t")
        return udid[0]
    
    return None


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'deviceName': 'Pixel 3XL',
        'udid': get_device_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }