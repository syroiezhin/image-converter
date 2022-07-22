from os import path, mkdir, getcwd
from PIL import Image # pip install Pillow
import pillow_avif # pip install pillow-avif-plugin

def create_an_array_of_images(image):
    
    (width, height) = image.size
    heaviest = (easiest := 0.0)

    enumerator = {'x':0,'y':0,'index':0}
    step = {'x':75,'y':71,'CTLC':56} # Cut Top Left Corner
    
    while (h := step['CTLC'] + enumerator['y']*step['y']) < (height-step['CTLC']):
        while (w := step['CTLC'] + enumerator['x']*step['x']) < (width-step['CTLC']):
            
            now_img = image.crop((w, h, w+50, h+50))
            if path.exists('img') == False: mkdir('img')
            now_img.convert("RGB").save(f"img/icon.{1+enumerator['index']}.{output}", output)
            
            weight = round( path.getsize(f"img/icon.{1+enumerator['index']}.{output}") / pow(1024,2) , 5) # Mb
            
            if (easiest == 0.0): easiest = weight
            elif (heaviest < weight): heaviest = weight
            elif (easiest > weight): easiest = weight
            else: pass
            
            enumerator['x']+=1
            enumerator['index']+=1
        
        enumerator['x']=0
        enumerator['y']+=1
        
    print( f"\n Perfect! We did it, the received files weigh from {easiest}Mb to {heaviest}Mb \n" )
        
        
if __name__== '__main__':
     
    address = input( f"\n Enter image address [{getcwd()}/image.png]: " ) 
    if path.isfile(address) == True: 
        print("\n Excellent! We work further...")
        image = Image.open(address)
        output = input("\n Choose the format to convert [webp,png,avif,jpeg,ico]: ")
        create_an_array_of_images(image)
    else: print("\n Wow, something went wrong, we can't find that file!")