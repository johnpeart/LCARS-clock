options = {
    # You can set the clock style to be EITHER
    # - "numeric" - for number-formatted time and date e.g. 0900, 2021.01.31
    # - "words" - for a word-formatted time only e.g. zero-nine hundred hours
    'clockStyle': 'numeric',
    'refreshTime': 60000
}

defaults = {
    # These are the defaults for the app GUI

    ## APP NAME
    'appName': 'Library Computer Access Retrieval System',

    ## SCREEN SIZE / WINDOW SIZE
    ## The screen size assumes a HyperPixel 4 Square is being used
    'screenSize': '720x720',
    'screenWidth': 720,
    'screenHeight': 720,
    'fullScreen': False,

    ## COLOURS
    'windowBackground': '#000000',
    'textColor_Label': '#FFCC99',
    'textColor_RedAlert': '#F09693',
    'textColor_YellowAlert': '#F8DC77',
    'textColor_AlertSecondary': '#FFFFFF',
    'textColor_Time': '#FF9900',
    'textColor_Date': '#FFCC99',

    ## FONTS AND TYPOGRAPHY
    'fontFace': 'Context Ultra Condensed SSi',

    ## IMAGES
    'horizontalRule_Default': 'assets/images/default-banner.png',
    'horizontalRule_YellowAlert': 'assets/images/yellow-alert-banner.png',
    'horizontalRule_RedAlert': 'assets/images/red-alert-banner.png',

    ## OTHER STYLES
    'borderWidth': 0
}

messages = {

    "nelson sandford birthday" : {
        "name" : "Nelson Sandford",
        "relationship" : null,
        "type": "birthday",
        "year" : 1970,
        "month" : 8,
        "day" : 2
    },

    "linda sandford birthday" : {
        "name" : "Linda Sandford",
        "relationship" : "wife",
        "type": "birthday",
        "year" : 1973,
        "month" : 12,
        "day" : 4
    },

    "linda sandford wedding anniversary" : {
        "name" : "Linda Sandford",
        "relationship" : "wife",
        "type": "wedding anniversary",
        "year" : 2010,
        "month" : 11,
        "day" : 1
    },

    "linda sandford valentine's day" : {
        "name" : "Linda Sandford",
        "relationship" : "wife",
        "type": "valentines day",
        "year" : null,
        "month" : 2,
        "day" : 14
    },

    "john peart birthday" : {
        "name" : "John Peart",
        "relationship" : "son",
        "type": "birthday",
        "year" : 1991,
        "month" : 11,
        "day" : 26
    },

    "charlotte peart birthday" : {
        "name" : "Charlotte Peart",
        "relationship" : "daughter",
        "type": "birthday",
        "year" : 1990,
        "month" : 2,
        "day" : 24
    },

    "olivia forscutt-peart birthday" : {
        "name" : "Olivia Forscutt-Peart",
        "relationship" : "grand daughter",
        "type": "birthday",
        "year" : 2021,
        "month" : 7,
        "day" : 23
    }

}