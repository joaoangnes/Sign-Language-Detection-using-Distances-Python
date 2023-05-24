Sign Language Detection using Distances - Python
-
- In this project, the main objective is to create a model that identifies sign language alphabet letters, excluding letters that require specific movements to be identified.

- It will use the coordinates of the hand landmarks found via webcam as data, with the following points as references:"
<img width="1073" alt="hand-landmarks" src="https://github.com/joaoangnes/Sign-Language-Detection-using-Landmarks-Python/assets/74597614/b57347b6-7a5a-4132-bba2-7761222d9182">

- But for this project, I only considered the distances between the fingertip points and the base of the hand, as shown by the purple lines in the following example:

![exemple-distances-land-mark](https://github.com/joaoangnes/Sign-Language-Detection-using-Distances-Python/assets/74597614/b922d1c5-758f-4a35-9992-21336b977558)

## File Structure

The repository contains several files for training the detection model. Here's a summary of each file's functionalities:

HandTrackingModule.py

    - This file stores all the important functions for identifying hand landmarks and parameterizing the used libraries.
    - It serves as the base file for the entire project.

CollectImages.py

    - This file creates the images that will be used for training.
    - It follows the step-by-step instructions displayed on the webcam.
    - It captures 150 photos with the right hand and 150 photos with the left hand. (All parameters can be easily modified)

CreateDataSet.py

    - This file retrieves all the collected images and stores the distances of tip finger points from the mediapipe library, in a 'pickle' file.

main.ipynb

    - This Jupyter notebook receives the collected data, processes it, and trains a model for identification.
    - Data normalization: ✅
    - Data balancing: ✅
    - Hyperparameter tuning: Using the RandomizedSearchCV method
    - Training Model: RandomForestClassifier
    - Validation Model: Cross Validate

    After all validations, the model is saved using pickle with the name 'model.p'.

## Utilized Libraries

- cv2
- HandTrackingModule
- Pickle
- Os

## Demonstration

Functioning Model:

Right Hand:

<img src="https://github.com/joaoangnes/Sign-Language-Detection-using-Distances-Python/assets/74597614/3beab86a-c345-44bd-ab63-0dd5746e920c" width="160">

Left Hand:

<img src="https://github.com/joaoangnes/Sign-Language-Detection-using-Distances-Python/assets/74597614/c5031f71-09d8-4e3b-a78d-2ae60028f6d0" width="160">

## Lessons Learned

It was a great learning experience to delve into data science and complete this project.
I faced many difficulties initially in understanding how each library worked, and I admit that I still have many doubts, particularly regarding the performance of landmark detection using the mediapipe library.

In summary, this project provided valuable learning opportunities, and despite some setbacks, I managed to create a model that identifies all static sign language alphabet letters.

I have also created another repository that follows the same structure, but it uses the main hand landmark as input and inference data. 

Here's the link to the repository: https://github.com/joaoangnes/Sign-Language-Detection-using-Landmarks-Python
