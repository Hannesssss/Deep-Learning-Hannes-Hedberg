import tensorflow as tf
from tensorflow import keras

# Define a neural network model with hidden layers
model = keras.Sequential([
    keras.layers.Dense(units=8, input_dim=2, activation='relu'),  # Hidden layer with 8 units and ReLU activation
    keras.layers.Dense(units=1, activation='sigmoid')            # Output layer with 1 unit and sigmoid activation
])

# Compile the model
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

# Toy XOR data
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

# Train the model
model.fit(X, y, epochs=1000)

# Make predictions
predictions = model.predict(X)
print(predictions)
