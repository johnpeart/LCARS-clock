# LCARS Clock

The LCARS Clock is a custom-made clock. It consists of:

- a Python app displaying the time and alerts on a Raspberry Pi connected to a HyperPixel 4 Square display
- a perspex cover and 3d printed mount

## The app

Th Python app displays the time and alerts in the style of the Star Trek LCARS interface.

### Clock

The clock shows the time in full screen in two formats:

- as a numeric date and time in military time style
- as a word clock showing the time in military style

The layout of the clock is user selectable by changing the `settings.py` file.

### Alerts

The app also shows alerts at during certain time periods. These are defined in the `alerts.py` file.

When an alert is shown on screen, the clock will be minimised to the bottom of the screen and the date and time will be shown in numeric format at the bottom of the screen.