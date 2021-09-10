import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import popup

tubelight1=0;
bench1=0
bulb1=0;
fan1=0;

tubelight2=0;
bench2=0
bulb2=0;
fan2=0;

layout0=[
    [
    [sg.Text("Enter number of Tubelight in class"),sg.Input(),],
    [sg.Text("Enter number of bench in class    "),sg.Input()],
    [sg.Text("Enter number of bulb in class       "),sg.Input()],
    [sg.Text("Enter number of fan in class         "),sg.Input()],
    [sg.Button(button_text='OK')]
    ]
        ]

layout1=[
    [
    [sg.Text("Enter number of Tubelight in store room"),sg.Input()],
    [sg.Text("Enter number of bench in store room    "),sg.Input()],
    [sg.Text("Enter number of bulb in store room      "),sg.Input()],
    [sg.Text("Enter number of fan in store room        "),sg.Input()],
    [sg.Button(button_text='OK')]
    ]
        ]

layout2=[
    [sg.Text("Choose iterm to replace"),
    sg.Combo(['Tubelight','Bench','Bulb','Fan'],key='type')],
    [sg.Text("Enter number of iterm to replace"),
    sg.Input(key='iterms')],
    [sg.Button(button_text='OK')]
        ]

window = sg.Window('class room data', layout0)
event, values = window.read()
tubelight1+=int(values[0]);
bench1+=int(values[1]);
bulb1+=int(values[2]);
fan1+=int(values[3]);
window.close()

window = sg.Window('store room data', layout1)
event, values = window.read()
tubelight2+=int(values[0]);
bench2+=int(values[1]);
bulb2+=int(values[2]);
fan2+=int(values[3]);
window.close()

sg.popup(
        "Class Room Data",
        "\nNumber of Tubelight in class room:",tubelight1,
        "Number of bench in class room:",bench1,
        "Number of bulb in class room:",bulb1,
        "Number of fan in class room:",fan1,
        "\n\nTotal number of iterm in class room:",tubelight1+bench1+bulb1+fan1
        )

sg.popup(
        "Store Room Data",
        "\nNumber of Tubelight in store room:",tubelight2,
        "Number of bench in store room:",bench2,
        "Number of bulb in store room:",bulb2,
        "Number of fan in store room:",fan2,
        "\n\nTotal number of iterm in class room:",tubelight2+bench2+bulb2+fan2
        )

window = sg.Window('Replacement Menu', layout2)
event, values = window.read()
ch=values['type'];
iterm=int(values['iterms']);
window.close()

if ch=='Tubelight':
    if tubelight2==0:
        tubelight1-=iterm;
        sg.popup("Tubelights only remove from class room,because no tubelight in store room");
    elif tubelight2<iterm:
        iterm-=tubelight2;
        tubelight1-=iterm;
        tubelight2=0;
        sg.popup("Only available tubelights are replaced,\nremaining only remove from class room.");
    else:
        tubelight2-=iterm;
        sg.popup("Tubelights are Replaced Successfully.");

elif ch=='Bench':
    if bench2==0:
        bench1-=iterm;
        sg.popup("Benches only remove from class room,because no bench in store room");
    elif bench2<iterm:
        iterm-=bench2;
        bench1-=iterm;
        bench2=0;
        sg.popup("Only available benches are replaced,\nremaining only remove from class room.");
    else:
        bench2-=iterm;
        sg.popup("Benches are Replaced Successfully.");

elif ch=='Bulb':
    if bulb2==0:
        bulb1-=iterm;
        sg.popup("Bulbs only remove from class room,because no bulb in store room");
    elif bulb2<iterm:
        iterm-=bulb2;
        bulb1-=iterm;
        bulb2=0;
        sg.popup("Only available bulbs are replaced,\nremaining only remove from class room.");
    else:
        bulb2-=iterm;
        sg.popup("Bulbs are Replaced Successfully.");

elif ch=='Fan':
    if fan2==0:
        fan1-=iterm;
        sg.popup("Fans only remove from class room,because no fan in store room");
    elif fan2<iterm:
        iterm-=fan2;
        fan1-=iterm;
        fan2=0;
        sg.popup("Only available fans are replaced,\nremaining only remove from class room.");
    else:
        fan2-=iterm;
        sg.popup("Fans are Replaced Successfully.");
    
sg.popup(
        "Class Room Data",
        "\nNumber of Tubelight in class room:",tubelight1,
        "Number of bench in class room:",bench1,
        "Number of bulb in class room:",bulb1,
        "Number of fan in class room:",fan1,
        "\n\nTotal number of iterm in class room:",tubelight1+bench1+bulb1+fan1
        )

sg.popup(
        "Store Room Data",
        "\nNumber of Tubelight in store room:",tubelight2,
        "Number of bench in store room:",bench2,
        "Number of bulb in store room:",bulb2,
        "Number of fan in store room:",fan2,
        "\n\nTotal number of iterm in class room:",tubelight2+bench2+bulb2+fan2
        )