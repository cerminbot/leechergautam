from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1438892370:AAF7V-VjuZbSXltr_oIDSBgnZNjNS8UKJXw"
    APP_ID = 1046625
    API_HASH = "c68afc924b92d73ce27708b155f1e5b4"
    OWNER_ID = 617426792
    AUTH_CHANNEL = [-1001455886928]
    DESTINATION_FOLDER = "YLeechDrive" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nclient_id = 833850923810-cliasc9ugki633o3v4b4l9avbgbc5pvr.apps.googleusercontent.com\nclient_secret = N1sA4jINJ4yg07NUTZs03Q7Y\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMB_YghsLByBwYikXsdcWJ6FpavGbxfYXW7UlcPE936FZbMyiQ-BV-NMXG4WGc-aS0ADIFvEbfW-Hm1mhbqD24HFKt6A5fAFDNfsuR-mfE9lOVjAt8Jzn0p93M-mhrxK032gIRGpJNjxdO3VWf6IO1CP0dxoYxc","token_type":"Bearer","refresh_token":"1//0g6FeVdL-g8yeCgYIARAAGBASNwF-L9IrRy13QID9XAYy9dXC81ecQaVQbd30qhbjmbTQ_tAUCuzNjJ6pmCTRnUflk7HL0T_yrBw","expiry":"2020-10-09T20:49:30.3276637+07:00"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
