from pilgram import *
from PIL import Image


def filter_lofi(image_path, save_path):
    try:
    
        lofi(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False


def filter_1977(image_path, save_path):
    try:
       
        _1977(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_aden(image_path, save_path):
    try:
       
        aden(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False


def filter_brannan(image_path, save_path):
    try:
       
        brannan(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_brooklyn(image_path, save_path):
    try:
       
        brooklyn(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_clarendon(image_path, save_path):
    try:
       
        clarendon(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_earlybird(image_path, save_path):
    try:
       
        earlybird(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_gingham(image_path, save_path):
    try:
       
        gingham(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_hudson(image_path, save_path):
    try:
       
        hudson(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_inkwell(image_path, save_path):
    try:
       
        inkwell(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_kelvin(image_path, save_path):
    try:
       
        kelvin(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_lark(image_path, save_path):
    try:
       
        lark(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_maven(image_path, save_path):
    try:
       
        maven(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_mayfair(image_path, save_path):
    try:
       
        mayfair(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False
 

def filter_moon(image_path, save_path):
    try:
       
        moon(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_nashville(image_path, save_path):
    try:
       
        nashville(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_perpetua(image_path, save_path):
    try:
       
        perpetua(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_reyes(image_path, save_path):
    try:
       
        reyes(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_rise(image_path, save_path):
    try:
       
        rise(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_slumber(image_path, save_path):
    try:
       
        slumber(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_stinson(image_path, save_path):
    try:
       
        stinson(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_toaster(image_path, save_path):
    try:
       
        toaster(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_valencia(image_path, save_path):
    try:
       
        valencia(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_walden(image_path, save_path):
    try:
       
        walden(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False
               
def filter_willow(image_path, save_path):
    try:
       
        willow(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False

def filter_xpro2(image_path, save_path):
    try:
       
        xpro2(Image.open(image_path)).save(save_path)
        return True
    except Exception as exp:
        print(exp)
        return False
          
def LoadAllFilters(image_path):
    import tempfile
    from datetime import datetime
    import os
    image_path = image_path.replace("\\", "/")
    functions = ['filter_lofi', 'filter_1977', 'filter_aden', 'filter_brannan', 'filter_brooklyn', 'filter_clarendon', 'filter_earlybird', 'filter_gingham', 'filter_hudson', 'filter_inkwell', 'filter_kelvin', 'filter_lark', 'filter_maven', 'filter_mayfair', 'filter_moon', 'filter_nashville', 'filter_perpetua', 'filter_reyes', 'filter_rise', 'filter_slumber', 'filter_stinson', 'filter_toaster', 'filter_valencia', 'filter_walden', 'filter_willow', 'filter_xpro2']
    temp_dir = os.path.abspath(os.path.join(tempfile.gettempdir(), "FILTERGRAM_" + datetime.now().strftime("%H.%M.%S")))
    os.mkdir(temp_dir)
    extension = image_path.split('.')[-1]
    for function in functions:
        encoded_filename = os.path.join(temp_dir, function.split("_")[1] + '.' + extension)
        encoded_filename = encoded_filename.replace("\\", "/",)
        exec(f"{function}('{image_path}', '{encoded_filename}')")
    return temp_dir
