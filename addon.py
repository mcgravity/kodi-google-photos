import xbmcaddon
import xbmcgui
from script.module.requests import requests
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

# Set a string variable to use 
line1 = "Begining of new addon"

# Launch a dialog box in kodi showing the string variable 'line1' as the contents
xbmcgui.Dialog().ok(addonname, line1)
