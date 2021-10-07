import tensorflow as tf


def create_model(LOSS_FUNCTION,OPTIMIZER,METRICS,NUM_CLASSES):

    LAYERS=[tf.keras.layers.Flatten(input_shape=[28,28],name='inputLayer'),
        tf.keras.layers.Dense(300,activation='relu',name='hiddenlayer1'),
        tf.keras.layers.Dense(100,activation='relu',name='hiddenlayer2'),
        tf.keras.layers.Dense(NUM_CLASSES,activation='softmax',name='outpytlayer')]

    model_clf=tf.keras.models.Sequential(LAYERS)

    model_clf.summary()

    LOSS_FUNCTION='sparse_categorical_crossentropy' # tf.losses.sparce_categorical_crossentropy
    OPTIMIZER='SGD' # tf.keras.optimizers.SGD(0.02)
    METRICS=['accuracy']
    model_clf.compile(loss=LOSS_FUNCTION,optimizer=OPTIMIZER,metrics=METRICS)

    return model_clf ## <<< untrained model