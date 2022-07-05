
![](https://github.com/kukujiaopython/Naruto-OpenCV-Machine-learning-Game/blob/main/naruto%20game%20banner.PNG)

# Naruto OpenCV MachineLearning Turn-base Game

For those who were, like me, a big fan of the Naruto series, and for those who are current fans of the Boruto series,
this Naruto OpenCV game is a turn-based game which features our best boi Sasuke as the main Character,
and where you, as the player, will help him kick some major bandit ass.

The main feature of this game uses OpenCV and Machine Learning to allows players to wave handsigns in real life, infront of their
webcam, in order to use some of Sasuke's signature ninjitsu. 

Let your inner weeb loose, and take a major feelz trip back to the simplier days in primary school,
where the only troubles we had was whether we'll make it home in time to catch Naruto on CrunchyRoll every friday.




## Demo

Insert gif or link to demo


## WorkFlow 

1) Labelling images of myself doing the various naruto handsigns using LabelImg. 

2) labelled images are seperated into train and test folders, used to train my selected machine learning model.

3) Model of choice is transfer learning model, SSD Mobilenet, as the mobile is versatile and yield better results than vgg16 for my project.

4) After the training of my model completed, the model was embedded into OpenCV for real time detection of handsigns

5) Finally, the model embedded OpenCV was integrated into pygame to make the Naruto OpenCV Machine-Learning Game


## Model


Model Accuracy:

| Hand Signs | Accuracy |
| ---------- | -------- |
| Monkey     | 85%      |
| Dragon     | 89%      |
| Rat        | 92%      |
| Bird       | 98%      |
| Snake      | 89%      |
| Ox         | 93%      |
| Dog        | 95%      |
| Horse      | 99%      |
| Tiger      | 91%      |
| Boar       | 87%      |
| Ram        | 93%      |
| Hare       | 96%      |





## Acknowledgements (References & Source of Inspirations)

 - [Nicholas Renotte - Tensorflow Object Detection in 5 Hours with Python ](https://www.youtube.com/watch?v=yqkISICHH-U)
 - [Learning with Rev - Transfer Learning Mobilenet V2 - Large Fish Project](https://www.youtube.com/watch?v=DElZ6sn3ADI)
 - [Custom Object Detection using TensorFlow from Scratch](https://towardsdatascience.com/custom-object-detection-using-tensorflow-from-scratch-e61da2e10087)
 - [PyGame: A Primer on Game Programming in Python](https://realpython.com/pygame-a-primer/)
 - [Python pygame – The Full Tutorial](https://coderslegacy.com/python/python-pygame-tutorial/)

## Limitation & Futurework

Limitations:

1) Accuracy of real-time object detection fluctuates when wearing T-shirt of colours other then White and Black. This is most likely due to the fact that I was wearing black/white t-shirt in my training labelled photos, and hence the colour of my t-shirt also became input for identifying the different signs.

2) Accuracy of object-detections were not consistent when faces can be seen in webcam feed. This is, again, likely due to the fact that my training photos includes only my hand and upper torso, with my face excluded.

3) There is a bug that stops background music whenever a jitsu is activated. This is due to the fact that the different states are coded in a nest while loop, instead of utilising state machine in pygame.


Futurework:

1) Instead of using tensorflow (transfer learning models) to detect and identify objects irl, google mediapipe line can be used to track poses on hand, extract them, and identify different hand gestures with simple logics codes. 
