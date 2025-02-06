# style input the same
import sys

import turtle
colors = {'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen',
              'lawngreen', 'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick',
              'lightseagreen', 'chocolate', 'yellowgreen', 'darkolivegreen', 'violet', 'ivory', 'sandybrown',
              'wheat', 'mediumvioletred', 'bisque', 'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred ',
              'antiquewhite', 'royalblue', 'yellow', 'indigo ', 'lightcoral', 'darkslategrey',
              'sienna', 'lightslategray', 'mediumblue', 'red', 'khaki', 'darkviolet', 'mediumorchid', 'darkblue',
              'lightskyblue', 'turquoise', 'lightyellow', 'grey', 'whitesmoke', 'blueviolet', 'orchid', 'mediumslateblue',
              'darkturquoise', 'coral', 'forestgreen', 'gainsboro', 'darkorange',
              'cornflowerblue', 'lightsteelblue', 'plum', 'lavender', 'palegreen',
              'darkred', 'dimgray', 'floralwhite', 'orangered', 'oldlace', 'darksalmon',
              'lavenderblush', 'darkslategray', 'tan', 'cadetblue', 'silver', 'tomato',
              'darkkhaki', 'slategray', 'maroon', 'olive', 'deeppink', 'linen', 'magenta',
              'crimson', 'mistyrose', 'lime', 'saddlebrown', 'blanchedalmond', 'black', 'snow', 'seashell',
              'darkcyan', 'gold', 'midnightblue', 'darkgoldenrod', 'palevioletred', 'fuchsia', 'teal', 'lightpink',
              'darkgrey', 'mediumspringgreen','aquamarine', 'lightsalmon', 'navajowhite',
              'darkgreen', 'burlywood','rosybrown', 'springgreen', 'purple', 'olivedrab', 'lightslategrey','orange',
              'aliceblue', 'mediumaquamarine', 'navy', 'salmon', 'rebeccapurple', 'darkmagenta', 'limegreen',
              'deepskyblue', 'pink', 'mediumpurple', 'skyblue', 'aqua', 'blue', 'slategrey', 'darkslateblue',
              'honeydew', 'darkseagreen', 'paleturquoise', 'brown', 'thistle',
              'lemonchiffon', 'peru', 'cornsilk', 'papayawhip', 'green', 'lightgoldenrodyellow',
              'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey', 'beige', 'palegoldenrod', 'darkgray', 'white',
              'ghostwhite', 'dodgerblue', 'greenyellow',
              'dimgrey', 'darkorchid'}

DOCTYPE = "<!DOCTYPE html>"
HTML1 = "<html>"
HTML2 = "</html>"
HEAD1 = "<head>"
HEAD2 = "</head>"
BODY1 = "<body>"
BODY2 = "</body>"
TITLE1 = "<title>"
TITLE2 = "</title>"
BODYTITLE1 = "<h1>"
BODYTITLE2 = "</h1>"
PARAGRAPH_TITLE1 = "<h2>"
PARAGRAPH_TITLE2 = "</h2>"
PARAGRAPH_TEXT1 = "<p>"
PARAGRAPH_TEXT2  = "</p>"
IMG1 = "<img src=images/"
IMG2 = ">"
N = '\n'  # newline character

def style_input():
    """
    Prompts the user for colors and font
    :return:
    """
    style_part = ''
    boo = True
    while boo:
      backcolor = input("Enter a background color")
      if backcolor[0].isdigit():
          print("Illegal format")

      elif backcolor[1:].isdigit(): #if the first and next characters are digits
         if len(backcolor) == 7:
           if backcolor[0] != '#':
            print("Illegal format")
           else:
            boo = False
         else: #if len(backcolor) != 7
            print("Illegal format")

      elif backcolor not in colors: #If it is not a digit, it could be a color; colors is a set
        print("Illegal format")

      else:
        boo = False


    boo1 = True
    while boo1:
     fontcolor = input("Enter a fontcolor")
     if fontcolor[0].isdigit():
         print("Illegal format")

     elif fontcolor[1:].isdigit():  # if the first and next characters are digits
         if len(fontcolor) == 7:
             if fontcolor[0] != '#':
                 print("Illegal format")
             else:
                 boo1 = False
         else:
             print("Illegal format")

     elif fontcolor not in colors:  # If it is not a digit, it could be a color; colors is a set
         print("Illegal format")
     else:
         boo1 = False


    boo2 = True
    while boo2:
     headcolor = input("Enter a heading color")
     if headcolor[0].isdigit():
         print("Illegal format")

     elif headcolor[1:].isdigit():  # if the first and next characters are digits
         if len(headcolor) == 7:
             if headcolor[0] != '#':
                 print("Invalid format")
             else:
                 boo2 = False
         else:
             print("Invalid format")

     elif headcolor not in colors:  # If it is not a digit, it could be a color; colors is a set
         print("Invalid format")
     else:
         boo2 = False

    #for font style
    print("You will now choose a font")
    ans = input("Do you want to see what the fonts look like?[yes]")
    if ans == "yes":
        print("Close the window when you have made your choice")
        turtle.write("Arial", move=False, align='left', font=("Arial", 14, "normal"))
        turtle.write("Comic Sans MS", move=False, align='right', font=("ComicSansMS", 14, "normal")) #spaces here
        turtle.write("Lucida Grande", move=False, align='left', font=("LucidaGrande", 14, "normal"))
        turtle.write("Tahoma", move=False, align='right', font=("Tahoma", 14, "normal"))
        turtle.write("Verdana", move=False, align='left', font=("Verdana", 14, "normal"))
        turtle.write("Helvetica", move=False, align='right', font=("Helvetica", 14, "normal"))
        turtle.write("Times New Roman", move=False, align='left', font=("TimesNewRoman", 14, "normal"))
        turtle.title("Font Options")
        turtle.showturtle()
        print("Choose a font by its number")
        print("0: Arial,size 14")
        print("1: Comic Sans MS, size 14")
        print("2: Lucida Grande, size 14")
        print("3: Tahoma, size 14")
        print("4: Verdana, size 14")
        print("5: Helvetica, size 14")
        print("6: Times New Roman, size 14")
        font = input(">>")
        if font == '0':
          fontstyle = 'Arial'
        elif font == '1':
          fontstyle = '\'Comic Sans MS\'' #do I exclude whitespace?
        elif font == '2':
          fontstyle = '\'Lucida Grande\''
        elif font == '3':
          fontstyle = 'Tahoma'
        elif font == '4':
          fontstyle = 'Verdana'
        elif font == '5':
          fontstyle = 'Helvetica'
        elif font == '6':
          fontstyle = '\'Times New Roman\''
    #else: if they don't want a font?

    else:
        print("Choose a font by its number")
        print("0: Arial,size 14")
        print("1: Comic Sans MS, size 14")
        print("2: Lucida Grande, size 14")
        print("3: Tahoma, size 14")
        print("4: Verdana, size 14")
        print("5: Helvetica, size 14")
        print("6: Times New Roman, size 14")
        font = input(">>")
        if font == '0':
            fontstyle = 'Arial'
        elif font == '1':
            fontstyle = '\'Comic Sans MS\'' #do I exclude whitespace?
        elif font == '2':
            fontstyle = '\'Lucida Grande\''
        elif font == '3':
            fontstyle = 'Tahoma'
        elif font == '4':
            fontstyle = 'Verdana'
        elif font == '5':
            fontstyle = 'Helvetica'
        elif font == '6':
            fontstyle = '\'Times New Roman\''

    file = open('style_template.txt')
    for line in file:
     line = line.replace("@BACKCOLOR", backcolor)
     line = line.replace("@FONTCOLOR", fontcolor)
     line = line.replace("@HEADCOLOR", headcolor)
     line = line.replace("@FONTSTYLE", fontstyle)
     style_part += line
    return style_part


def body():
 info = ''
 for line in open(sys.argv[1]): #how to get the title
    #line = line.strip()
    if len(line) > 0 and line[0] == "!":
        if line[1:14] == "new_paragraph":
            line = line.replace("!new_paragraph", '')
            info += line + N
        elif line[1:6] == "title":
            line = line.replace("!title", PARAGRAPH_TITLE1)
            info += line + PARAGRAPH_TITLE2 + N + PARAGRAPH_TEXT1 + N

        elif line[1:6] == "image":
            line = line.strip()
            line = line.replace("!image", PARAGRAPH_TEXT2 + N + IMG1)
            info += line + IMG2
        elif line == '\n':
            info += PARAGRAPH_TEXT2
    else:
          info += line
 return info

def create_website():
    info = body()
    title = ''
    for ch in info:
        if ch == "<":
            break
        else:
            title += ch
    style = style_input()
    head_html = HEAD1 + N + TITLE1 + title + TITLE2 + N + style\
                + N + HEAD2
    body_html = BODY1 + N + BODYTITLE1 + title + BODYTITLE2 \
                + N + info + N + BODY2
    head_and_body = head_html + body_html
    website = DOCTYPE + N + HTML1 + N + head_and_body\
              + N + HTML2
    outfile = open('index.html', 'w')
    outfile.write(website)
    outfile.close()
    print("Your website has been saved as index.html")

create_website()

