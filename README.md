
![](https://github.com/kukujiaopython/Naruto-OpenCV-Machine-learning-Game/blob/main/naruto%20game%20banner.PNG)

# Naruto OpenCV MachineLearning Turn-base Game

For those who were a big fan of the Naruto anime series like me, and for those who are current fans of the Boruto anime series,
this Naruto OpenCV game is a turn-based game which features our best boi Sasuke as the main character.
You, as the player, will help Sasuke kick some major bandit butts.

The main feature of this game uses OpenCV and Machine Learning to allow players to wave ninja handsigns in real life, infront of their
webcam, in order to use some of Sasuke's signature ninjitsu in-game. 

Let your inner weeb loose, and take a major feelz trip back to the simplier times,
when the only worry we had was whether we'll make it home from school in time to catch Naruto on CrunchyRoll every friday.




## Demo



https://user-images.githubusercontent.com/102948566/177392191-bf9f3681-54f4-4507-8bd0-c1b9f70f8a56.mp4




## WorkFlow 

1) Labelling images of myself doing the various naruto handsigns using LabelImg. 

2) labelled images are seperated into train and test folders, used to train my selected machine learning model.

3) Model of choice is transfer learning model, SSD Mobilenet, as the mobile is versatile and yield better results than vgg16 for my project.

4) After the training of my model completed, the model was embedded into OpenCV for real time detection of handsigns

5) Finally, the model embedded OpenCV was integrated into pygame to make the Naruto OpenCV Machine-Learning Game


## Model

Model of Choice: SSD MobileNet

![mobileNet-SSD-network-architecture](https://user-images.githubusercontent.com/102948566/177393896-15cdbfdf-5ee1-42d9-ae99-5b7b659baa23.png)

Model Accuracy:

| Hand Signs | Train    | Test |
| ---------- | -------- | ---- |
| Monkey     | 85%      | 80%  |
| Dragon     | 89%      | 79%  |
| Rat        | 92%      | 87%  |
| Bird       | 98%      | 85%  |
| Snake      | 89%      | 76%  |
| Ox         | 93%      | 71%  |
| Dog        | 95%      | 80%  |
| Horse      | 99%      | 75%  |
| Tiger      | 91%      | 74%  |
| Boar       | 87%      | 70%  | 
| Ram        | 93%      | 87%  | 
| Hare       | 96%      | 90%  |





## Acknowledgements (References & Source of Inspirations)

 - [Nicholas Renotte - Tensorflow Object Detection in 5 Hours with Python ](https://www.youtube.com/watch?v=yqkISICHH-U)
 - [Learning with Rev - Transfer Learning Mobilenet V2 - Large Fish Project](https://www.youtube.com/watch?v=DElZ6sn3ADI)
 - [Custom Object Detection using TensorFlow from Scratch](https://towardsdatascience.com/custom-object-detection-using-tensorflow-from-scratch-e61da2e10087)
 - [PyGame: A Primer on Game Programming in Python](https://realpython.com/pygame-a-primer/)
 - [Python pygame – The Full Tutorial](https://coderslegacy.com/python/python-pygame-tutorial/)
 - [Banner Photo - Ronald @seerlight](https://www.instagram.com/seerlight/?hl=en)

## Limitation & Futurework

Limitations:

1) Accuracy of real-time object detection fluctuates when wearing T-shirt of colours other then White and Black. This is most likely due to the fact that I was wearing black/white t-shirt in my training labelled photos, and hence the colour of my t-shirt also became input for identifying the different signs.

2) Accuracy of object-detections were not consistent when faces can be seen in webcam feed. This is, again, likely due to the fact that my training photos includes only my hand and upper torso, with my face excluded.

3) There is a bug that stops background music whenever a jitsu is activated. This is due to the fact that the different states are coded in a nest while loop, instead of utilising state machine in pygame.


Futurework:

1) Instead of using tensorflow (transfer learning models) to detect and identify objects irl, google mediapipe line can be used to track poses on hand, extract them, and identify different hand gestures with simple logics codes. 
