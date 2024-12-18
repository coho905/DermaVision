# DermaVision 

## This Project was for my senior year capstone culminating project @ the Commonwealth Governor's School. 
</br> I trained a ResNet 18 on ~1000 images of skin cancer tumors. 
</br> I used a flask server host to allow for image uploads on localhost (though would obviously be cloud compatible and production ready with gunicorn/nginx - I just don't have the funds). 

## How it works
1. Run the localhost
2. navigate to 127.0.0.1
3. upload image of potentially cancerous skin lesion
4. Recieve prediction and confidence level on each selected photo

## To run it
- Upload all of the paths (model path, upload path, path to photos (required to load the model with weights for some reason)
- Make sure the system is compatible with non-Windows OS (never had time to test it)

## Notes
+ I pieced this code together hurriedly in order to get it as a working demo for my presentation to several Spotsylvania school board representatives, Governor School faculty, and more. As a result, it is very rushed, with lots of patch fixes. Please let me know if you encounter any errors that make no sense whatsoever
+ Building off that note, feel free to make pull requests or let me know if something is wrong!
+ disclaimer+warning: NO result given should be considered medical advice of any sort. This is purely for technological growth and entertainment. This codebase is in no way FDA approved, nor should it be considered a valid medical tool. Please seek a doctor if you believe something is legitimately wrong.

MIT License, Copyright Colin Wolfe (2022)
