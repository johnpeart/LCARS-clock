import chooseDisplay as choose
import showDisplay as display


def main():
    # determines what to show
    displayType = choose.displayType() 
    # sets up what the display will show
    display.updateDisplay(displayType)
    # updates the GUI
    display.mainloop()

if __name__ == "__main__":
    main()