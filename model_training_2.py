import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG19
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.optimizers import Adam
import os


train_dir = './data/potato data/data/train'  
img_size = 224 
batch_size = 32


train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)


train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical'
)


base_model = VGG19(weights='imagenet', include_top=False, input_shape=(img_size, img_size, 3))


for layer in base_model.layers:
    layer.trainable = False


model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])


model.summary()


epochs = 10
history = model.fit(
    train_generator,
    epochs=epochs,
    steps_per_epoch=train_generator.samples // batch_size
)


model.save('potato_disease_vgg19_model_3.h5')
print("Model saved as 'potato_disease_vgg19_model_3.h5'")



#Jupyter notebook code


# # Import necessary libraries
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.applications import VGG19
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Flatten, Dropout
# from tensorflow.keras.optimizers import Adam
# import matplotlib.pyplot as plt
# import os

# # Define the training directory path
# train_dir = './data/potato data/data/train'  # Replace with your actual path

# # Set image size, batch size, and number of classes
# img_size = 224  # VGG19 input size
# batch_size = 32
# num_classes = 4  # Number of classes: Healthy, Early Blight, Late Blight, Not Leaf

# # Set up data augmentation and preprocessing for training images
# train_datagen = ImageDataGenerator(
#     rescale=1./255,
#     rotation_range=20,
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     shear_range=0.2,
#     zoom_range=0.2,
#     horizontal_flip=True,
#     fill_mode='nearest'
# )

# # Load training images
# train_generator = train_datagen.flow_from_directory(
#     train_dir,
#     target_size=(img_size, img_size),
#     batch_size=batch_size,
#     class_mode='categorical'
# )

# # Load the VGG19 base model without top layers (pre-trained on ImageNet)
# base_model = VGG19(weights='imagenet', include_top=False, input_shape=(img_size, img_size, 3))

# # Freeze base model layers to retain pre-trained weights
# for layer in base_model.layers:
#     layer.trainable = False

# # Build the model
# model = Sequential([
#     base_model,
#     Flatten(),
#     Dense(256, activation='relu'),
#     Dropout(0.5),
#     Dense(num_classes, activation='softmax')
# ])

# # Compile the model
# model.compile(optimizer=Adam(learning_rate=0.0001),
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])

# # Model summary
# model.summary()

# # Training the model
# epochs = 10
# history = model.fit(
#     train_generator,
#     epochs=epochs,
#     steps_per_epoch=train_generator.samples // batch_size
# )

# # Save the model
# model.save('potato_disease_vgg19_model_with_not_leaf.h5')
# print("Model saved as 'potato_disease_vgg19_model_with_not_leaf.h5'")

# # Plot training accuracy and loss
# plt.figure(figsize=(12, 4))

# # Plot training accuracy
# plt.subplot(1, 2, 1)
# plt.plot(history.history['accuracy'], label='Training Accuracy')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.legend()
# plt.title('Training Accuracy')

# # Plot training loss
# plt.subplot(1, 2, 2)
# plt.plot(history.history['loss'], label='Training Loss')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.legend()
# plt.title('Training Loss')

# plt.show()
