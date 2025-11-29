# Forest-seedling-count-using-machine-learning-from-UAV-images
Forest seedling count using machine learning from UAV images - Using Ultralytics library
#EN_US

This Python script was entirely authored by Luis Fernando Machado de Oliveira as part of a graduation project at the Federal University of Paraná,
titled "Use of Deep Learning Algorithms on Drone Images to Measure Seedling Mortality in Silviculture.". 
 
You are free to use this script as long as proper credit is given.

##IMPORTANT:

The algorithm uses the "LabelImg" library for image labeling. However, this library does not work correctly in Python versions later than 3.8. 
You are welcome to use another labeling method, but if you wish to continue with LabelImg, please follow these steps for proper functionality:

1) in your python directory, locate the folder: C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\libs
2) open file named: "canvas.py"
3) Inside "canvas.py" make the following changes:
    
    - in line 526: replace: p.drawRect(left_top.x(), left_top.y(), rect_width, rect_height)
                    with: p.drawRect(int(left_top.x()), int(left_top.y()), int(rect_width), int(rect_height))

    - in line 530: replace: p.drawLine(self.prev_point.x(), 0, self.prev_point.x(), self.pixmap.height())
                    with: p.drawLine(int(self.prev_point.x()), 0, int(self.prev_point.x()), int(self.pixmap.height()))

    - in line 531: replace: p.drawLine(0, self.prev_point.y(), self.pixmap.width(), self.prev_point.y())
                    witch: p.drawLine(0, int(self.prev_point.y()), int(self.pixmap.width()), int(self.prev_point.y()))

4) Navigate to C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\labelImg
5) open file named: "LabelImg.py" 
6) Inside "LabelImg.py" make the following changes: 

    - in line 965: replace: p.drawRect(left_top.x(), left_top.y(), rect_width, rect_height)
                    with: p.drawRect(int(left_top.x()), int(left_top.y()), int(rect_width), int(rect_height))

##HOW TO USE:

The script allows you to define labels for training, train the algorithm, and based on the training results, it performs
the seedling counting and mortality calculation according to the best training you define.

##WHEN RUNNING THE SCRIPT:

- Press 1 to open LabelImg
- Press 2 to start training using the created labels. IMPORTANT: the images for training and validation, as well as
the labels, must be manually placed in the appropriate folders. Do not forget that the labels must have the same file name
as the images!
- Press 3 to start the counting mode. The program will ask you to define the planting spacing to be evaluated, the area (in hectares),
select the file with the best result from step 2 (usually best.pt), and finally select the image you want to count
- Press 4 if you wish to exit the script

##ACKNOWLEDGMENTS: 
- My actual internship company (2025) that supports me in the creation and develpment of the project 
- Everyone who provided materials for algorithm training and contributed to the DTB.
- All my friends and family for their unwavering support throughout this project.

###Contact: 
e-mail: luisfernando.mo@hotmail
github: https://github.com/LuisMachadoCODES

#PT_BR

Esse script python é de total autoria de Luis Fernando Machado de Oliveira para teste de conclusão de curso na Universidade Federal do Paraná 
entitulado de "Uso de algoritmos de deeplearning em imagens de drone para metrificar de mortalidade de mudas na silvicultura". 

Sinta-se livre para utilizar o script desde que seja corretamente citado.

##IMPORTANTE:

O algoritmo utiliza a biblioteca "Labelimg" para definição das labels das imagens, entretanto a biblioteca não funciona corretamente em versões
posteriores do python 3.8. Sinta-se livre para utlizar outro meio de definição de labels, mas caso deseje continuar com o Labelimg, por favor siga
esses passos para o correto funcionamento:

1) em seu diretório python procure a pasta: C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\libs
2) entre no arquivo chamado "canvas.py"
3) Dentro do arquivo "canvas.py" faça as seguintes alterações:
    
    - Na linha 526: substitua: p.drawRect(left_top.x(), left_top.y(), rect_width, rect_height)
                    para: p.drawRect(int(left_top.x()), int(left_top.y()), int(rect_width), int(rect_height))

    - Na linha 530: substitua: p.drawLine(self.prev_point.x(), 0, self.prev_point.x(), self.pixmap.height())
                    para: p.drawLine(int(self.prev_point.x()), 0, int(self.prev_point.x()), int(self.pixmap.height()))

    - Na linha 531: substitua: p.drawLine(0, self.prev_point.y(), self.pixmap.width(), self.prev_point.y())
                    para: p.drawLine(0, int(self.prev_point.y()), int(self.pixmap.width()), int(self.prev_point.y()))

4) No diretório C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\labelImg
5) entre no arquivo chamado "LabelImg.py" 
6) dentro do arquivo "LabelImg.py" faça as seguintes alterações: 

    - Na linha 965: substitua: p.drawRect(left_top.x(), left_top.y(), rect_width, rect_height)
                    para: p.drawRect(int(left_top.x()), int(left_top.y()), int(rect_width), int(rect_height))

##COMO UTILIZAR :

O script permite que você defina as labels para treinamento, treine o algoritmo e a partir dos resultados do treinamento ele realiza
a contagem de mudas e cálculo de mortalidade de acordo com o melhor treinamento que você definir. 

##Ao executar o script: 

- Aperte 1 para abrir o LabelImg;
- Aperte 2 para iniciar o treinamento a partir das labels criadas. IMPORTANTE: as imagens para treinamento e validação, assim como
as labels devem ser direcionadas para as devidas pastas manualmente. Não se esqueça que as labels devem ser com o mesmo nome de arquivo
das imagens!;
- Aperte 3 para inciar o modo treinamento. O programa irá pedir para você definir o espaçamento do plantio a ser avaliado, área (em hectares),
selecionar o arquivo com o melhor resultado do passo 2 (geralmente best.pt), e por fim selecionar a imagem que você deseja realizar a contagem.
- Aperte 4 caso deseje encerrar o script

##AGRADECIMENTOS:

- Atual empresa em que faço estágio (2025) que me apoiou na criação e deselvolvimento do projeto
- A todos que disponibilizaram os materiais para treinamento do altoritmo e colaboraram com o DTB
- A todos os meus amigos e família por todo apoio durante a excecução desse projeto

###Contato: 
e-mail: luisfernando.mo@hotmail
github: https://github.com/LuisMachadoCODES
