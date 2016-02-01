init python:
    style.my_text = Style(style.default)
    style.warning = Style(style.default)
    style.green = Style(style.default)
    style.description = Style(style.default)
    style.myBox = Style(style.default)
    style.navigation_button = Style(style.button_text)
    # style.navigation_button.background = Frame("pic/bg.png", 25, 25)
    # style.navigation_button.hover_background = Frame("pic/bg.png", 25, 25)
    # style.navigation_button.selected_background = Frame("images/interface/music_library_button_selected.png", 25, 25)
    style.navigation_button_text.color = "#FFFFFF"
    style.navigation_button_text.size = 18
    style.navigation_button_text.font = "segoeuib.ttf"
    style.navigation_button_text.outlines = [(2, "#494949", 0, 0)]
    style.navigation_button_text.hover_color = "#00FF80"
    # style.navigation_button_text.selected_color = "#00FF00"
    
    style.action_button_text.color = "#FF8B8B"
    style.action_button_text.size = 18
    style.action_button_text.font = "segoeuib.ttf"
    style.action_button_text.outlines = [(2, "#494949", 0, 0)]
    style.action_button_text.hover_color = "#FF0000"
    
    
    style.small_button = Style(style.button_text)
    style.small_button_text.color = "#FFFFFF"
    style.small_button_text.outlines = [(1, "#494949", 0, 0)]
    style.small_button_text.hover_color = "#0000FF"
    # style.small_button_text.selected_color = "#00FF00"
    style.small_button_text.size = 14
    
    style.bluesmall_button = Style(style.button_text)
    style.bluesmall_button.color = "#60D5FC"
    style.bluesmall_button.outlines = [(1, "#494949", 0, 0)]
    style.bluesmall_button.hover_color = "#0000FF"
    # style.bluesmall_button.selected_color = "#00FF00"
    style.bluesmall_button.size = 14
    
    style.myFrame = Style(style.frame)
    style.myFrame.background = "#0000FF50"
    style.myFrame.xmargin  = 10
    style.myFrame.ymargin   = 10
    
    style.peopleTextList = Style(style.frame)
    style.peopleTextList.background = Frame("pic/frame.png", 0, 0)
    # style.peopleTextList.xmargin  = 100
    # style.peopleTextList.ymargin   = 100
    style.peopleTextList.xpadding  = 10
    style.peopleTextList.ypadding  = 10
    
    style.myBar = Style(style.vbar)
    style.myBar.background = "#FF0000"
    style.myBar.thumb = "#FF0000"
     
style my_text is text:
    size 15
    outlines [(1, "#494949", 0, 0)]
    
style small_text is text:
    size 10
    outlines [(1, "#494949", 0, 0)]
    
style verticalText is text:
    vertical True
    size 18
    outlines [(2, "#494949", 0, 0)]

style param is text:
    size 15
    outlines [(2, "#494949", 0, 0)]
    bold True
    # drop_shadow [ (2, 1) ,(3, 2)] 

style paramwarning is text:
    size 15
    outlines [(2, "#494949", 0, 0)]
    color "#FF1E1E"
    bold True
    # drop_shadow [ (2, 1) ,(3, 2)] 

style paramgreen is text:
    size 15
    outlines [(2, "#494949", 0, 0)]
    bold True
    color "#00FF00"
    # drop_shadow [ (2, 1) ,(3, 2)] 
      
style warning is text:
    size 15
    outlines [(2, "#494949", 0, 0)]
    color "#FF1E1E"

style green is text:
    size 15
    outlines [(2, "#494949", 0, 0)]
    color "#00FF00"

style description is text:
    size 20
    font 'verdana.ttf'
    outlines [(2, "#494949", 0, 0)]

style statButton is button:
    size 15
    
style myBox is box:
    spacing 5

style mytimer is text:
    color "#FFFFFF"
    size 24
    font "segoeuib.ttf"
    outlines [(2, "#494949", 0, 0)]
    # drop_shadow [ (2, 1) ,(3, 2)] 
