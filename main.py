import clock as cl

displayType = 'clock' # set to 'clock' or 'wordclock'

def main():
    cl.updateDisplay(displayType)
    cl.mainloop()

if __name__ == "__main__":
    main()