from kivy.config import Config

Config.set('graphics', 'resizable', '1')

Config.set('graphics', 'width', '430')

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
import os


KV = '''

<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "240dp"
    allow_stretch: True
    keep_ratio: False
    
    


ScreenManager:
    WelcomeScreen:
    LoginScreen:
    SignupScreen:
    MainScreen:
        name: 'mainscreen'
    
<WelcomeScreen>:
    name : 'welcomescreen'
    
    MDLabel:
        text:'DOCH'
        font_style:'H1'
        halign:'center'
        pos_hint: {'center_y':0.9}
    
    MDLabel:
        text:'Welcome to the market place of Balochi embroidery'
        font_style:'H5'
        halign:'center'
        pos_hint: {'center_y':0.7}
        
    MDRaisedButton:
        text:'Login'
        pos_hint : {'center_x':0.5,'center_y':0.3}
        size_hint: (0.2,0.05)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
            
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.5,'center_y':0.2}
        size_hint: (0.2,0.05)
        on_press: 
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'
            
<LoginScreen>:
    name:'loginscreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
        
    MDTextField:
        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        icon_right: 'email'
        hint_text: 'email'
        size_hint : (0.6,0.1)
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: 'rectangle'
        
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        icon_right: 'eye'
        hint_text: 'password'
        size_hint : (0.6,0.1)
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: 'rectangle'
        password: True
        
    MDRaisedButton:
        text:'Login'
        size_hint: (0.2,0.05)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            # app.username_changer() 
            
    MDTextButton:
        text: "Don't have an account"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'
            
<SignupScreen>:
    name:'signupscreen'
    
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.7,'center_x':0.5}
        icon_right: 'account'
        hint_text: 'username'
        size_hint : (0.6,0.1)
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: 'rectangle'
        
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.55,'center_x':0.5}
        icon_right: 'email'
        hint_text: 'email'
        size_hint : (0.6,0.1)
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: 'rectangle'
        
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        icon_right: 'eye'
        hint_text: 'password'
        size_hint : (0.6,0.1)
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: 'rectangle'
        password: True
        
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.2,0.05)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.signup()
            
    MDTextButton:
        text: "Already have an account"
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'
            

            
<MainScreen>:
    
                
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Doch"
            md_bg_color: app.theme_cls.primary_color
            
        MDBottomNavigation:
            MDBottomNavigationItem:
                # This is a fancy screen
                text: "Home"
                name: "home"
                icon: "home"
                MDGridLayout:
                    cols: 1
                    adaptive_height: True
                    padding: dp(4), dp(4)
                    spacing: dp(4)
            
                ScrollView:
            
                 
                    MDGridLayout:
                        cols: 1
                        adaptive_height: True
                        padding: dp(5), dp(5)
                        spacing: dp(5)
                
                        MyTile:
                            stars: 3
                            source: "images\doch-1.jpg"
                
                        MyTile:
                            stars: 3
                            source: "images\doch-2.jpg"
                
                        MyTile:
                            stars: 3
                            source: "images\doch-3.jpg"
                
                        MyTile:
                            stars: 3
                            source: "images\doch-4.jpg"
                            
                        MyTile:
                            stars: 3
                            source: "images\doch-5.jpg"
                            
                        MyTile:
                            stars: 3
                            source: "images\doch-6.jpg"
                
                        MyTile:
                            stars: 3
                            source: "images\doch-7.jpg"
                
                        MyTile:
                            stars: 3
                            source: "images\doch-8.jpg"
                
                        MyTile:
                            stars: 3
                            source: "images\doch-9.jpg"
                            
                        MyTile:
                            stars: 3
                            source: "images\doch-10.jpg"
                            
            MDBottomNavigationItem:
                text: "Favorites"
                name: "favorite"
                icon: "star"
                BoxLayout:
                    orientation: 'vertical'
                    
            MDBottomNavigationItem:
                text: "Notifications"
                name: "notification"
                icon: "bell"
                BoxLayout:
                    orientation: 'vertical'
                    
            MDBottomNavigationItem:
                text: "Profile"
                name: "profile"
                icon: "account"
                BoxLayout:
                ScrollView:
                    MDList:
                        OneLineAvatarListItem:
                            on_release: print("Opens the edit profile menu")
                            text: "Edit Profile"
                            ImageLeftWidget:
                                source: "images\doch-1.jpg"
                        OneLineListItem:
                            on_release: print("Logs out of the account. Goes Back to Login Page")
                            text: "Log Out"

    
'''

# Code to get the file names from the folder into a list
images = []
directory = 'images'
for entry in os.scandir(directory):
    if (entry.path.endswith(".jpg")
            or entry.path.endswith(".png")) and entry.is_file():
        images.append(entry.path)
print(images)


class WelcomeScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class MainScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))


class DochApp(MDApp):
    def build(self):
        self.kv_str = Builder.load_string(KV)
        self.url = "https://dochapp-ca322.firebaseio.com/.json"
        return self.kv_str

    def signup(self):
        signupEmail = self.kv_str.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.kv_str.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.kv_str.get_screen('signupscreen').ids.signup_username.text
        if len(signupEmail) == 0 or len(signupPassword) == 0 or len(signupUsername) == 0:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Empty inputs are not allowed', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        elif len(signupEmail.split()) > 1 or len(signupPassword.split()) > 1 or len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Spaces are not allowed in inputs', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            # put the code here to save user info to database
            print(signupEmail, signupPassword)
            signup_data = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_data = signup_data.replace(".", ",")
            signup_data = signup_data.replace("\'", "")
            to_database = json.loads(signup_data)
            print((to_database))
            requests.patch(url= self.url, json= to_database)
            # when you press the signup button it takes you to the login screen
            # change the screen to main screen later
            self.kv_str.get_screen('mainscreen').manager.current = 'mainscreen'

    auth_key = 'ddJiuLM5NKF6PPhzdV6W0BGRXz3YoswPTLDEC2JD'

    def login(self):
        self.login_check = False

        loginEmail = self.kv_str.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.kv_str.get_screen('loginscreen').ids.login_password.text

        if len(loginEmail) == 0 or len(loginPassword) == 0:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Empty inputs are not allowed', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        elif len(loginEmail.split()) > 1 or len(loginPassword.split()) > 1: #split isn't doing the work to catch the space
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Spaces are not allowed', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            # Put the code to check the database and decide either to give access to user or not
            print(loginEmail, loginPassword)
            supported_email = loginEmail.replace('.', ',')
            supported_password = loginPassword.replace('.', ',')
            request = requests.get(self.url + '?auth=' + self.auth_key)
            data = request.json()
            emails = set()
            for key, value in data.items():
                emails.add(key)

            if supported_email in emails and supported_password == data[supported_email]['Password']:
                self.login_check = True
                self.kv_str.get_screen('mainscreen').manager.current = 'mainscreen'
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='OK', on_release=self.close_username_dialog)
                self.dialog = MDDialog(title='Invalid User', text='Either the username or the password is incorrect',
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()


    def close_username_dialog(self, obj):
        self.dialog.dismiss()

DochApp().run()