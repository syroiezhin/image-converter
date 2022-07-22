# <p id="UP">Do you want to change the extension of a bitmap and also cut out some fragment from it?</p>

## <p align="center">Give thanks : <u>5168 7450 1701 5535</u> <a href="https://en.privatbank.ua/all-ways-to-receive-send-an-international-transfer"><img src="https://upload.wikimedia.org/wikipedia/uk/f/ff/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%9F%D1%80%D0%B8%D0%B2%D0%B0%D1%8224.png" width = "25" alt="Privat Bank UA"> </a></p>

> Let's check if the required image exists for further manipulations.
- [X] `path.isfile(address)`
> Run it for editing!
- [X] `Image.open(address)`
> Сreate variables with image dimensions.
- [X] `(width, height) = image.size`
> Let's specify three important parameters for cutting out the fragments we need in the image. We need the STLC parameter in order to get rid of the extra "white frame" in the left and upper faces. The X and Y parameters in the Step are needed to move to the next fragment of the image grid. By the width of the X step, and by the height the y step is used.
- [X] `step = {'x':75,'y':71,'CTLC':56}`
> To crop a fragment we use: 
- [X] `image.crop((w, h, w+50, h+50))`
> To save all the fragments of the photo in one folder, we need to make sure that such a folder does not already exist in order to create it. 
- [X] `if path.exists('img') == False: mkdir('img')`
> We save the image fragment in the desired directory with the image number in the title and with the selected extension.
- [X] `now_img.convert("RGB").save(f"img/icon.{1+enumerator['index']}.{output}", output)`
> For clarity, you can see the size of the image in MB. To do this, we divide the bytes by $1024^2$ and round the number to 5 decimal places.
- [X] `round( path.getsize(f"img/icon.{1+enumerator['index']}.{output}") / pow(1024,2) , 5)`

[⇪](#UP)
