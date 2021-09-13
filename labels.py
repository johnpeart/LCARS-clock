def update(labelToUpdate, textToShow):
    text = textToShow
    labelToUpdate.config(
        text = text.upper(),
        wraplength = 700
    )