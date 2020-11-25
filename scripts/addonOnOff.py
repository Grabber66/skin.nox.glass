import xbmc, time, xbmcaddon

xbmc.executebuiltin("ActivateWindow(home)")
time.sleep(1)
xbmc.executebuiltin('Addon.OpenSettings(script.enableit)')
time.sleep(2)
xbmc.executebuiltin('ActivateWindow(AddonBrowser,addons://user/all)')
time.sleep(3)
xbmc.executebuiltin('RunScript(script.enableit)')
time.sleep(4)
xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "script.enableit", "enabled": true }, "id":1}')
time.sleep(5)
xbmc.executebuiltin('RunScript(script.enableit)')

