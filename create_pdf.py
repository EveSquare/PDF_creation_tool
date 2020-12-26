#       ::::::::::    :::     :::       ::::::::::       ::::::::       ::::::::      :::    :::           :::        :::::::::       ::::::::::
#      :+:           :+:     :+:       :+:             :+:    :+:     :+:    :+:     :+:    :+:         :+: :+:      :+:    :+:      :+:
#     +:+           +:+     +:+       +:+             +:+            +:+    +:+     +:+    +:+        +:+   +:+     +:+    +:+      +:+
#    +#++:++#      +#+     +:+       +#++:++#        +#++:++#++     +#+    +:+     +#+    +:+       +#++:++#++:    +#++:++#:       +#++:++#
#   +#+            +#+   +#+        +#+                    +#+     +#+    +#+     +#+    +#+       +#+     +#+    +#+    +#+      +#+
#  #+#             #+#+#+#         #+#             #+#    #+#     #+#    #+#     #+#    #+#       #+#     #+#    #+#    #+#      #+#
# ##########        ###           ##########       ########       ###########    ########        ###     ###    ###    ###      ##########
import sys
import os
from PIL import Image
import img2pdf

def create_pdf(file_list: list):
    out_put_name = os.path.splitext(os.path.basename(file_list[0]))
    i = 1
    if os.path.exists(f"{out_put_name[0]}.pdf"):
        while True:
            if os.path.exists(f"{out_put_name[0]}_{str(i)}.pdf"):
                i = i + 1
            else:
                with open(f"{out_put_name[0]}_{str(i)}.pdf", "wb") as f:
                    f.write(img2pdf.convert(file_list))
                return
    
    with open(f"{out_put_name[0]}.pdf", "wb") as f:
        f.write(img2pdf.convert(file_list))

def main():
    current_dir = os.getcwd()
    file_ex = [".jpg", ".png", ".jpeg", ".bmp", ".PNG"]
    imgs = []

    for i in range(1,len(sys.argv)):
        if os.path.splitext(sys.argv[i])[1] in file_ex:
            imgs.append(sys.argv[i])
    
    if len(imgs) == 0:
        exit()

    create_pdf(imgs)

if __name__ == "__main__":
    main()

