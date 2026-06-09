[app]
title = General Chat
package.name = generalchat
package.domain = org.generalchat
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pyrebase4==4.5.0,plyer==2.1,requests==2.31.0,pillow==10.0.0,sounddevice==0.4.6,numpy==1.24.3
orientation = portrait
permissions = INTERNET,RECORD_AUDIO,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
fullscreen = 0
presplash.filename = %(source.dir)s/icon.png
icon.filename = %(source.dir)s/icon.png
android.accept_sdk_license = True