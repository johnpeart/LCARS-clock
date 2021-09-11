import chooseDisplay as choose
import showDisplay as display

displayType = choose.displayType() # set to 'clock' or 'wordclock'

def main():
    display.updateDisplay(displayType)
    display.mainloop()

if __name__ == "__main__":
    main()